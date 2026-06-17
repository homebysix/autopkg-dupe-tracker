import hashlib
from collections import Counter, defaultdict
from difflib import SequenceMatcher

from .models import CandidateSet, RecipeRecord


def set_id(members):
    raw = "|".join(sorted(m.identifier for m in members))
    return hashlib.sha256(raw.encode()).hexdigest()[:12]


def display_name_for(members):
    names = [m.display_name for m in members if m.display_name]
    if not names:
        return members[0].name_key
    counts = Counter(names)
    return sorted(counts, key=lambda name: (-counts[name], name.lower(), name))[0]


def repos_count(members):
    return len({m.repo for m in members})


def add_group(groups, key, members, reason, strength):
    if len(members) < 2 or repos_count(members) < 2:
        return
    groups[key].append((members, reason, strength))


def compatible_name_group(members):
    by_name = defaultdict(list)
    for member in members:
        by_name[member.name_key].append(member)
    return by_name


def source_groups(records):
    groups = defaultdict(list)
    for record in records:
        if record.source_type and record.source_key and record.source_type != "unknown":
            groups[f"{record.source_type}:{record.source_key}"].append(record)
    return groups


def name_groups(records):
    groups = defaultdict(list)
    for record in records:
        if record.name_key:
            groups[record.name_key].append(record)
    return groups


def authority_fingerprint(record):
    return "|".join(record.codesig_authorities)


def authority_name_groups(records):
    groups = defaultdict(list)
    for record in records:
        fingerprint = authority_fingerprint(record)
        if fingerprint and record.name_key:
            groups[f"{record.name_key}|{fingerprint}"].append(record)
    return groups


def source_domain_name_groups(records):
    groups = defaultdict(list)
    for record in records:
        if record.source_domain and record.name_key:
            groups[f"{record.name_key}|{record.source_domain}"].append(record)
    return groups


def similarity_groups(records):
    grouped = []
    records = [r for r in records if r.name_key]
    used = set()
    for i, left in enumerate(records):
        if i in used:
            continue
        group = [left]
        for j, right in enumerate(records[i + 1 :], start=i + 1):
            if j in used or left.repo == right.repo:
                continue
            if not weak_identity_match(left, right):
                continue
            if SequenceMatcher(None, left.name_key, right.name_key).ratio() >= 0.9:
                group.append(right)
                used.add(j)
        if repos_count(group) >= 2:
            used.add(i)
            grouped.append(group)
    return grouped


def weak_identity_match(left: RecipeRecord, right: RecipeRecord):
    if left.source_domain and left.source_domain == right.source_domain:
        return True
    if left.codesig_authorities and left.codesig_authorities == right.codesig_authorities:
        return True
    return False


def merge_overlapping(raw_groups):
    parent = {}

    def find(key):
        parent.setdefault(key, key)
        while parent[key] != key:
            parent[key] = parent[parent[key]]
            key = parent[key]
        return key

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    path_to_keys = defaultdict(list)
    group_by_key = {}
    for key, payload in raw_groups.items():
        members, reason, strength = payload
        group_by_key[key] = payload
        for member in members:
            path_to_keys[(member.repo, member.rel_path)].append(key)

    for keys in path_to_keys.values():
        for key in keys[1:]:
            union(keys[0], key)

    components = defaultdict(list)
    for key in raw_groups:
        components[find(key)].append(key)

    merged = []
    strength_order = {"HIGH": 3, "MEDIUM": 2, "LOW": 1}
    for keys in components.values():
        members_by_path = {}
        reasons = []
        strengths = []
        for key in keys:
            members, reason, strength = group_by_key[key]
            reasons.append(reason)
            strengths.append(strength)
            for member in members:
                members_by_path[(member.repo, member.rel_path)] = member
        members = sorted(members_by_path.values(), key=lambda m: (m.name_key, m.repo, m.rel_path))
        if repos_count(members) < 2:
            continue
        strength = max(strengths, key=lambda s: strength_order[s])
        merged.append(
            CandidateSet(
                id=set_id(members),
                display_name=display_name_for(members),
                members=members,
                match_reasons=sorted(set(reasons)),
                match_strength=strength,
            )
        )
    return sorted(merged, key=lambda c: (c.display_name.lower(), c.id))


def build_candidates(records):
    raw = {}

    for key, members in source_groups(records).items():
        for name_key, subgroup in compatible_name_group(members).items():
            if repos_count(subgroup) < 2:
                continue
            raw[f"source:{key}|{name_key}"] = (
                subgroup,
                f"same {key.split(':', 1)[0]} source",
                "HIGH",
            )

    for key, members in authority_name_groups(records).items():
        if repos_count(members) < 2:
            continue
        raw[f"authority:{key}"] = (
            members,
            "same normalized name and code signing authority",
            "MEDIUM",
        )

    for key, members in source_domain_name_groups(records).items():
        if repos_count(members) < 2:
            continue
        raw[f"domain:{key}"] = (
            members,
            "same normalized name and source domain",
            "MEDIUM",
        )

    for key, members in name_groups(records).items():
        if repos_count(members) < 2:
            continue
        raw[f"name:{key}"] = (members, "same normalized recipe name", "LOW")

    for idx, members in enumerate(similarity_groups(records)):
        raw[f"similar:{idx}"] = (members, "similar name plus weak identity match", "LOW")

    return merge_overlapping(raw)
