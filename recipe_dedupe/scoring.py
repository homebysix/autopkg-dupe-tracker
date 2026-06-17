from dataclasses import asdict
from datetime import datetime, timezone

from .recipe import normalize_name

DISTINCT_WORDS = (
    "fork",
    "custom",
    "enterprise",
    "variant",
    "branded",
    "rebranded",
    "modified",
    "community edition",
    "portable",
    "rosetta",
)


SOURCE_SCORE = {
    "github": 3.0,
    "sparkle": 2.5,
    "url": 1.5,
    "unknown": 0.5,
    None: 0.0,
}


def parse_date(value):
    if not value:
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def confidence_from_gap(gap):
    if gap >= 3:
        return "HIGH"
    if gap >= 1:
        return "MEDIUM"
    return "LOW"


def distinct_distribution_reason(candidate):
    for member in candidate.members:
        text = (member.description or "").lower()
        for word in DISTINCT_WORDS:
            if word in text:
                return f"{member.repo} description indicates distinct distribution: {word}"
    return None


def artifact_compatibility(candidate):
    all_count = len(candidate.members)
    known = [set(m.artifact_formats) for m in candidate.members if m.artifact_formats]
    if len(known) < 2:
        return True, "artifact formats unknown or not comparable"
    union = set().union(*known)
    if len(union) <= 1:
        fmt = sorted(union)[0]
        if len(known) < all_count:
            n = all_count - len(known)
            suffix = f" ({n} recipe{'s' if n > 1 else ''} format unknown)"
            return True, f"same artifact format: {fmt}{suffix}"
        return True, f"same artifact format: {fmt}"
    return False, "different artifact formats: " + ", ".join(sorted(union))


def duplicate_confidence(candidate, compatible_artifact):
    if not compatible_artifact:
        return "LOW"
    if candidate.match_strength == "HIGH":
        return "HIGH"
    if candidate.match_strength == "MEDIUM":
        return "MEDIUM"
    return "LOW"


def member_score(member, repo_overrides):
    score = 0.0
    reasons = []
    penalties = []

    if repo_overrides.get(member.repo, {}).get("flag") == "never_keep":
        score -= 8
        penalties.append("repo flagged never_keep")

    if member.has_codesig:
        score += 3
        reasons.append("has CodeSignatureVerifier")
    else:
        penalties.append("no CodeSignatureVerifier")

    if member.has_endofcheck:
        score += 2
        reasons.append("has EndOfCheckPhase")
    else:
        penalties.append("no EndOfCheckPhase")

    if member.has_arch_var:
        score += 1.5
        reasons.append("has architecture input")
    if member.has_release_var:
        score += 1
        reasons.append("has release/channel input")

    score += SOURCE_SCORE.get(member.source_type, 0.0)
    if member.source_type:
        reasons.append(f"{member.source_type} source")

    if member.description and len(member.description.strip()) > 20:
        score += 0.5
        reasons.append("has useful description")

    score += min(member.dependent_count * 0.25, 1.25)
    if member.dependent_count:
        reasons.append(f"{member.dependent_count} dependent recipe(s)")

    if member.rel_path.endswith(".recipe"):
        score += 0.1

    return score, reasons, penalties


def sort_scored_members(scored):
    def identity_key(item):
        member = item["member"]
        return (member.repo, member.rel_path, member.identifier)

    def age_key(item):
        parsed = parse_date(item["member"].first_commit)
        return (parsed is None, parsed or datetime.max.replace(tzinfo=timezone.utc))

    scored = sorted(scored, key=lambda item: (-item["score"], age_key(item), identity_key(item)))
    if len(scored) < 2:
        return scored
    top_score = scored[0]["score"]
    close = [
        item
        for item in scored
        if abs(top_score - item["score"]) < 0.5 and parse_date(item["member"].first_commit)
    ]
    if close:
        oldest = min(
            close, key=lambda item: (parse_date(item["member"].first_commit), identity_key(item))
        )
        if oldest is not scored[0]:
            scored.remove(oldest)
            scored.insert(0, oldest)
            scored[0]["tiebreaker"] = "older first commit"
    return scored


def filename_key(rel_path):
    base = rel_path.rsplit("/", 1)[-1]
    for ext in (".recipe.yaml", ".recipe.plist", ".recipe"):
        if base.endswith(ext):
            base = base[: -len(ext)]
            break
    return normalize_name(base)


def mislinked_member(candidate):
    # A member tied to the set only by name_key, whose filename disagrees with
    # that name_key, is usually a copy-pasted NAME masking a different product.
    members = candidate.members
    for member in members:
        others = [other for other in members if other is not member]
        shares = any(
            (member.source_key and member.source_key == other.source_key)
            or (member.source_domain and member.source_domain == other.source_domain)
            or (
                member.codesig_authorities
                and set(member.codesig_authorities) & set(other.codesig_authorities)
            )
            for other in others
        )
        if shares:
            continue
        fkey, nkey = filename_key(member.rel_path), member.name_key
        if fkey and nkey and fkey != nkey and fkey not in nkey and nkey not in fkey:
            return member
    return None


def _exit(base, verdict, keeper_confidence, **kwargs):
    base.update({"verdict": verdict, "keeper_confidence": keeper_confidence, **kwargs})
    return base


def evaluate_candidate(candidate, repo_overrides=None, set_overrides=None):
    repo_overrides = repo_overrides or {}
    set_overrides = set_overrides or {}
    override = set_overrides.get(candidate.display_name.lower())

    distinct_reason = distinct_distribution_reason(candidate)
    compatible_artifact, artifact_reason = artifact_compatibility(candidate)
    dup_conf = duplicate_confidence(candidate, compatible_artifact)

    base = {
        "id": candidate.id,
        "app_name": candidate.display_name,
        "member_count": len(candidate.members),
        "match_reasons": candidate.match_reasons,
        "duplicate_confidence": dup_conf,
        "substitutability": {
            "same_product": distinct_reason is None,
            "compatible_artifact": compatible_artifact,
            "notes": [artifact_reason] + ([distinct_reason] if distinct_reason else []),
        },
        "members": [asdict(m) for m in candidate.members],
    }

    if override and override.get("decision") in ("wont_fix", "exception"):
        return _exit(base, "skip", "NONE", skip_reason=override.get("reason", override["decision"]))

    if override and override.get("prs"):
        if override.get("merged"):
            return _exit(base, "done", "NONE", prs=override["prs"])
        return _exit(base, "skip", "NONE", skip_reason="PR(s) already opened", prs=override["prs"])

    if distinct_reason:
        return _exit(base, "skip", "NONE", skip_reason=distinct_reason)

    mislinked = mislinked_member(candidate)
    if mislinked:
        return _exit(
            base,
            "review",
            "LOW",
            skip_reason=(
                f"possible mis-grouped recipe: {mislinked.rel_path} name does not match its NAME"
            ),
        )

    if not compatible_artifact:
        return _exit(base, "review", "LOW", skip_reason=artifact_reason)

    if dup_conf == "LOW":
        return _exit(
            base, "review", "LOW", skip_reason="low duplicate confidence; needs qualitative review"
        )

    scored = []
    for member in candidate.members:
        score, reasons, penalties = member_score(member, repo_overrides)
        scored.append(
            {
                "member": member,
                "score": score,
                "reasons": reasons,
                "penalties": penalties,
            }
        )
    scored = sort_scored_members(scored)
    best = scored[0]
    rest = scored[1:]
    gap = best["score"] - (rest[0]["score"] if rest else 0)
    keep_conf = confidence_from_gap(gap)

    keep = {
        "repo": best["member"].repo,
        "rel_path": best["member"].rel_path,
        "score": round(best["score"], 2),
        "reason": "; ".join(best["reasons"][:4]) or "best overall score",
    }
    deprecate = [
        {
            "repo": item["member"].repo,
            "rel_path": item["member"].rel_path,
            "score": round(item["score"], 2),
            "dependent_count": item["member"].dependent_count,
            "reason": "; ".join(item["penalties"][:3]) or "weaker duplicate",
        }
        for item in rest
    ]

    rationale = [
        {"category": "duplicate", "text": "; ".join(candidate.match_reasons)},
        {"category": "artifact", "text": artifact_reason},
        {"category": "keeper", "text": keep["reason"]},
    ]
    for item in rest:
        if item["penalties"]:
            rationale.append(
                {
                    "category": "deprecate",
                    "text": f"{item['member'].repo}: " + "; ".join(item["penalties"][:3]),
                }
            )

    base.update(
        {
            "verdict": "recommend",
            "keeper_confidence": keep_conf,
            "keep": [keep],
            "deprecate": deprecate,
            "rationale": rationale,
            "criteria": [
                {"key": "codesig", "label": "CodeSignatureVerifier"},
                {"key": "endofcheck", "label": "EndOfCheckPhase"},
                {"key": "source", "label": "Source resilience"},
                {"key": "arch", "label": "Architecture support"},
                {"key": "release", "label": "Release/channel support"},
                {"key": "history", "label": "First commit tiebreaker"},
            ],
            "deprecation_message": (
                f"Consider switching to {candidate.display_name} recipes in "
                f"the {best['member'].repo} repo. This recipe is deprecated "
                "and will be removed in the future."
            ),
        }
    )
    return base


def rank_key(evaluation):
    conf = {"HIGH": 3, "MEDIUM": 2, "LOW": 1, "NONE": 0}
    return (
        -conf.get(evaluation.get("duplicate_confidence"), 0),
        -conf.get(evaluation.get("keeper_confidence"), 0),
        evaluation.get("app_name", "").lower(),
    )
