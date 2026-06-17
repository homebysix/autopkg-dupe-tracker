from collections import Counter
from datetime import datetime, timezone
from html import escape
from pathlib import Path

from .io import write_json

CSS = """
:root {
  --bg: #f4f5f7; --bg-surface: #fff; --bg-surface-alt: #f8f9fb; --bg-hover: #f0f1f4;
  --border: #e0e3e8; --border-light: #eef0f3;
  --text: #1a1d23; --text-secondary: #5a6070; --text-muted: #8891a0; --link: #2563eb;
  --header-gradient: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
  --header-text: #fff; --header-muted: rgba(255,255,255,.6); --header-bg: #1e293b;
  --high-bg: #fde8e8; --high-text: #991b1b; --high-border: #fca5a5;
  --med-bg: #fef3c7; --med-text: #854d0e; --med-border: #fcd34d;
  --low-bg: #e0f2fe; --low-text: #0c4a6e; --low-border: #7dd3fc;
  --none-bg: #f1f5f9; --none-text: #64748b; --none-border: #cbd5e1;
  --review-bg: #f5f3ff; --review-text: #6d28d9; --review-border: #c4b5fd;
  --keep-bg: #dcfce7; --keep-text: #166534; --keep-border: #86efac;
  --depr-bg: #fee2e2; --depr-text: #991b1b; --depr-border: #fca5a5;
  --info-bg: #eff6ff; --info-text: #1e40af; --info-border: #bfdbfe;
  --warn-bg: #fefce8; --warn-text: #854d0e; --warn-border: #fde68a;
  --done-bg: #dcfce7; --done-text: #166534; --done-border: #86efac;
  --shadow-sm: 0 1px 2px rgba(0,0,0,.04); --shadow-md: 0 2px 8px rgba(0,0,0,.06);
  --radius: 8px; --radius-sm: 5px;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #0f1117; --bg-surface: #1a1d26; --bg-surface-alt: #22252f; --bg-hover: #272b36;
    --border: #2e3340; --border-light: #252830;
    --text: #e4e6eb; --text-secondary: #a0a6b4; --text-muted: #6b7280; --link: #60a5fa;
    --header-gradient: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
    --header-text: #e4e6eb; --header-muted: rgba(228,230,235,.5); --header-bg: #0f172a;
    --high-bg: #450a0a; --high-text: #fca5a5; --high-border: #7f1d1d;
    --med-bg: #451a03; --med-text: #fcd34d; --med-border: #78350f;
    --low-bg: #0c4a6e; --low-text: #bae6fd; --low-border: #075985;
    --none-bg: #1e293b; --none-text: #94a3b8; --none-border: #334155;
    --review-bg: #2e1065; --review-text: #c4b5fd; --review-border: #4c1d95;
    --keep-bg: #052e16; --keep-text: #86efac; --keep-border: #166534;
    --depr-bg: #450a0a; --depr-text: #fca5a5; --depr-border: #7f1d1d;
    --info-bg: #172554; --info-text: #93c5fd; --info-border: #1e3a5f;
    --warn-bg: #422006; --warn-text: #fcd34d; --warn-border: #78350f;
    --done-bg: #052e16; --done-text: #86efac; --done-border: #166534;
    --shadow-sm: 0 1px 2px rgba(0,0,0,.2); --shadow-md: 0 2px 8px rgba(0,0,0,.3);
  }
}
*, *::before, *::after { box-sizing: border-box; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  margin: 0; padding: 0; background: var(--bg); color: var(--text);
  -webkit-font-smoothing: antialiased; line-height: 1.5;
}
a { color: var(--link); text-decoration: none; }
a:hover { text-decoration: underline; }

.header { background: var(--header-gradient); color: var(--header-text); padding: 1.25rem 1rem; }
.header-inner { max-width: 960px; margin: 0 auto; }
.header h1 { margin: 0; font-size: 1.2rem; font-weight: 700; }
.header .subtitle { color: var(--header-muted); font-size: .8rem; margin-top: .15rem; }
.stat-row { display: flex; flex-wrap: wrap; gap: .5rem 1.25rem; margin-top: .6rem; font-size: .8rem; }
.stat-item { display: flex; align-items: center; gap: .3rem; }
.stat-num { font-weight: 700; font-size: 1rem; }
.stat-num-high { color: var(--high-border); }
.stat-num-review { color: #c4b5fd; }

.info-bar { background: var(--info-bg); border-bottom: 1px solid var(--info-border); padding: .5rem 1rem; font-size: .78rem; color: var(--info-text); }
.info-bar-inner { max-width: 960px; margin: 0 auto; display: flex; align-items: center; gap: .4rem; flex-wrap: wrap; }
.info-toggle { cursor: pointer; text-decoration: underline; font-weight: 600; }
.info-panel { display: none; background: var(--info-bg); padding: .75rem 1rem; font-size: .78rem; color: var(--info-text); border-bottom: 1px solid var(--info-border); line-height: 1.6; }
.info-panel-inner { max-width: 960px; margin: 0 auto; }
.info-panel.visible { display: block; }
.info-panel ul { margin: .3rem 0; padding-left: 1.3rem; }
.info-panel li { margin-bottom: .2rem; }
.info-panel code { background: rgba(127,127,127,.18); padding: .05rem .25rem; border-radius: 3px; font-size: .95em; }

.controls { background: var(--bg-surface); border-bottom: 1px solid var(--border); position: sticky; top: 0; z-index: 20; padding: .5rem 1rem; }
.controls-inner { max-width: 960px; margin: 0 auto; }
.search-row { display: flex; gap: .5rem; align-items: center; }
.search-row input { flex: 1; min-width: 0; padding: .45rem .7rem; border: 1px solid var(--border); border-radius: var(--radius-sm); font-size: .85rem; background: var(--bg); color: var(--text); outline: none; }
.search-row input:focus { border-color: var(--link); box-shadow: 0 0 0 2px rgba(37,99,235,.2); }
.search-row input::placeholder { color: var(--text-muted); }
.filter-toggle { display: none; padding: .4rem .6rem; border: 1px solid var(--border); border-radius: var(--radius-sm); background: var(--bg); color: var(--text-secondary); cursor: pointer; font-size: .85rem; white-space: nowrap; line-height: 1; }
.filter-toggle.active { background: var(--link); color: #fff; border-color: var(--link); }

.tab-line { display: flex; align-items: center; gap: .5rem; margin-top: .5rem; }
.tab-label { font-size: .75rem; font-weight: 600; color: var(--text-secondary); white-space: nowrap; }
.tab-strip { display: flex; gap: 0; overflow-x: auto; -webkit-overflow-scrolling: touch; scrollbar-width: none; }
.tab-strip::-webkit-scrollbar { display: none; }
.tab { padding: .35rem .7rem; border: 1px solid var(--border); cursor: pointer; font-size: .75rem; font-weight: 500; background: var(--bg-surface); color: var(--text-muted); white-space: nowrap; transition: all .12s; flex-shrink: 0; }
.tab:first-child { border-radius: var(--radius-sm) 0 0 var(--radius-sm); }
.tab:last-child { border-radius: 0 var(--radius-sm) var(--radius-sm) 0; }
.tab:not(:first-child) { border-left: none; }
.tab[data-tab="HIGH"] { color: var(--high-border); }
.tab[data-tab="MEDIUM"] { color: var(--med-border); }
.tab[data-tab="LOW"] { color: var(--low-border); }
.tab[data-tab="REVIEW"] { color: var(--review-text); }
.tab[data-tab="SKIP"] { color: var(--none-text); }
.tab[data-tab="DONE"] { color: var(--done-text); }
.tab.active { font-weight: 700; }
.tab.active[data-tab="ALL"] { background: var(--header-bg); color: #fff; border-color: var(--header-bg); }
.tab.active[data-tab="HIGH"] { background: var(--high-bg); color: var(--high-text); border-color: var(--high-border); }
.tab.active[data-tab="MEDIUM"] { background: var(--med-bg); color: var(--med-text); border-color: var(--med-border); }
.tab.active[data-tab="LOW"] { background: var(--low-bg); color: var(--low-text); border-color: var(--low-border); }
.tab.active[data-tab="REVIEW"] { background: var(--review-bg); color: var(--review-text); border-color: var(--review-border); }
.tab.active[data-tab="SKIP"] { background: var(--none-bg); color: var(--none-text); border-color: var(--none-border); }
.tab.active[data-tab="DONE"] { background: var(--done-bg); color: var(--done-text); border-color: var(--done-border); }
.tab-sep { width: 1px; background: var(--border); align-self: stretch; margin: 2px 3px; flex-shrink: 0; }
.tab .cnt { margin-left: .25rem; opacity: .6; font-weight: 400; }
@media (max-width: 520px) { .tab .cnt { display: none; } }

.filter-row { display: flex; gap: .5rem; margin-top: .5rem; flex-wrap: wrap; }
.filter-row select { padding: .35rem .45rem; border: 1px solid var(--border); border-radius: var(--radius-sm); font-size: .78rem; background: var(--bg); color: var(--text); outline: none; min-width: 0; flex: 1; }
@media (max-width: 640px) {
  .filter-toggle { display: block; }
  .filter-row { display: none; }
  .filter-row.visible { display: flex; }
}

.content { max-width: 960px; margin: 0 auto; padding: .75rem 1rem 3rem; }
.set-count { font-size: .75rem; color: var(--text-muted); margin-bottom: .5rem; }

.card { background: var(--bg-surface); border: 1px solid var(--border); border-radius: var(--radius); margin-bottom: .5rem; box-shadow: var(--shadow-sm); transition: box-shadow .12s; overflow: hidden; border-left: 3px solid var(--border); }
.card.dup-high { border-left-color: var(--high-border); }
.card.dup-medium { border-left-color: var(--med-border); }
.card.dup-low { border-left-color: var(--low-border); }
.card.verdict-skip { border-left-color: var(--none-border); opacity: .7; }
.card.verdict-skip[open] { opacity: 1; }
.card.verdict-done { border-left-color: var(--done-border); opacity: .75; }
.card.verdict-done[open] { opacity: 1; }
.card:hover { box-shadow: var(--shadow-md); }
.card.hidden { display: none; }

.card-hd { display: flex; align-items: center; gap: .5rem; padding: .6rem .75rem; cursor: pointer; user-select: none; min-height: 44px; list-style: none; }
.card-hd::-webkit-details-marker { display: none; }
.card-hd:hover { background: var(--bg-hover); }
.expand-arrow { font-size: .65rem; color: var(--text-muted); transition: transform .15s; flex-shrink: 0; width: 1rem; text-align: center; }
.card[open] .expand-arrow { transform: rotate(90deg); }
.card-app { font-weight: 700; font-size: .9rem; flex: 1; min-width: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.card-meta { display: flex; gap: .35rem; align-items: center; flex-shrink: 0; flex-wrap: wrap; justify-content: flex-end; }

.badge { font-size: .6rem; font-weight: 700; padding: .15rem .4rem; border-radius: 3px; white-space: nowrap; line-height: 1.3; border: 1px solid transparent; }
.badge-prio-high { background: var(--high-bg); color: var(--high-text); border-color: var(--high-border); }
.badge-prio-medium { background: var(--med-bg); color: var(--med-text); border-color: var(--med-border); }
.badge-prio-low { background: var(--low-bg); color: var(--low-text); border-color: var(--low-border); }
.badge-prio-none { background: var(--none-bg); color: var(--none-text); border-color: var(--none-border); }
.badge-review { background: var(--review-bg); color: var(--review-text); border-color: var(--review-border); }
.badge-skip { background: var(--none-bg); color: var(--none-text); border-color: var(--none-border); }
.badge-done { background: var(--done-bg); color: var(--done-text); border-color: var(--done-border); }
.badge-conf-high { background: var(--high-bg); color: var(--high-text); }
.badge-conf-medium { background: var(--med-bg); color: var(--med-text); }
.badge-conf-low { background: var(--low-bg); color: var(--low-text); }
.badge-conf-none { background: var(--none-bg); color: var(--none-text); }

.card-body { padding: 0 .75rem .75rem; border-top: 1px solid var(--border-light); }
.match { font-size: .72rem; color: var(--text-muted); padding: .5rem 0 .15rem; }

.recipe-row { display: flex; gap: .5rem; padding: .6rem 0; border-bottom: 1px solid var(--border-light); align-items: flex-start; }
.role-tag { font-size: .6rem; font-weight: 700; padding: .15rem .35rem; border-radius: 3px; white-space: nowrap; flex-shrink: 0; margin-top: .1rem; line-height: 1.3; text-transform: uppercase; letter-spacing: .02em; min-width: 3.1rem; text-align: center; }
.role-keep { background: var(--keep-bg); color: var(--keep-text); }
.role-deprecate { background: var(--depr-bg); color: var(--depr-text); }
.role-member { background: var(--bg-surface-alt); color: var(--text-muted); }
.recipe-info { flex: 1; min-width: 0; }
.recipe-path { font-size: .8rem; font-weight: 600; word-break: break-all; line-height: 1.35; }
.recipe-path a { color: var(--text); }
.recipe-path a:hover { color: var(--link); }
.recipe-path .path-rest { color: var(--text-muted); font-weight: 500; }
.recipe-reason { font-size: .75rem; color: var(--text-secondary); margin-top: .2rem; line-height: 1.4; }
.feature-tags { display: flex; flex-wrap: wrap; gap: .25rem; margin-top: .3rem; }
.ftag { font-size: .6rem; padding: .1rem .3rem; border-radius: 3px; font-weight: 500; line-height: 1.3; }
.ftag-pos { background: var(--keep-bg); color: var(--keep-text); }
.ftag-neutral { background: var(--bg-surface-alt); color: var(--text-muted); border: 1px solid var(--border-light); }
.ftag-warn { background: var(--warn-bg); color: var(--warn-text); border: 1px solid var(--warn-border); }
.dep-count { font-size: .7rem; color: var(--text-muted); white-space: nowrap; flex-shrink: 0; margin-top: .1rem; }

.set-info { padding-top: .5rem; }
.set-info-row { display: flex; gap: .35rem; padding: .15rem 0; font-size: .75rem; line-height: 1.5; color: var(--text-secondary); align-items: flex-start; }
.set-info-icon { flex-shrink: 0; width: .9rem; text-align: center; font-size: .65rem; margin-top: .2rem; }
.si-shared .set-info-icon { color: var(--text-muted); }
.si-artifact .set-info-icon { color: var(--med-text); }
.si-keep .set-info-icon { color: var(--keep-text); }
.si-depr .set-info-icon { color: var(--depr-text); }

.banner { border-radius: var(--radius-sm); padding: .45rem .65rem; margin-top: .5rem; font-size: .75rem; line-height: 1.4; border: 1px solid; }
.banner-warn { background: var(--warn-bg); color: var(--warn-text); border-color: var(--warn-border); }
.banner-done { background: var(--done-bg); color: var(--done-text); border-color: var(--done-border); }
.notes { margin-top: .5rem; font-size: .72rem; color: var(--text-muted); line-height: 1.5; }

.empty { text-align: center; padding: 2rem; color: var(--text-muted); font-size: .85rem; }
.footer { max-width: 960px; margin: 0 auto; padding: 0 1rem 2rem; font-size: .7rem; color: var(--text-muted); text-align: center; line-height: 1.5; }

@media (min-width: 641px) {
  .header { padding: 1.25rem 1.5rem; }
  .controls { padding: .5rem 1.5rem; }
  .content { padding: .75rem 1.5rem 3rem; }
  .info-bar, .info-panel { padding-left: 1.5rem; padding-right: 1.5rem; }
}
@media print {
  .controls, .info-bar, .info-panel, .footer { display: none; }
  .card-body { display: block !important; }
  .card { break-inside: avoid; }
}
"""


JS = """
var activeTab = "ALL";
var searchQuery = "";
var keeperFilter = "";
var repoFilter = "";

function formatGenTime() {
  var el = document.getElementById("genTime");
  if (!el) return;
  var iso = el.dataset.iso;
  if (!iso) return;
  var d = new Date(iso);
  if (isNaN(d)) { el.textContent = iso; return; }
  el.textContent = "Updated " + d.toLocaleDateString() + " " +
    d.toLocaleTimeString([], {hour: "numeric", minute: "2-digit", timeZoneName: "short"});
}

function buildTabs() {
  var cards = document.querySelectorAll(".card");
  var counts = {ALL: 0, HIGH: 0, MEDIUM: 0, LOW: 0, REVIEW: 0, SKIP: 0, DONE: 0};
  cards.forEach(function(c) {
    counts.ALL++;
    var t = c.dataset.tab;
    if (counts[t] !== undefined) counts[t]++;
  });
  var defs = [
    {key: "ALL", label: "All"},
    {key: "HIGH", label: "High"},
    {key: "MEDIUM", label: "Med"},
    {key: "LOW", label: "Low"},
    {sep: true},
    {key: "REVIEW", label: "Review"},
    {key: "SKIP", label: "Skip"},
    {key: "DONE", label: "Done"}
  ];
  var el = document.getElementById("tabs");
  el.innerHTML = defs.map(function(t) {
    if (t.sep) return '<div class="tab-sep" aria-hidden="true"></div>';
    return '<div class="tab' + (t.key === activeTab ? ' active' : '') + '" data-tab="' +
      t.key + '">' + t.label + '<span class="cnt">(' + (counts[t.key] || 0) + ')</span></div>';
  }).join("");
  el.querySelectorAll(".tab").forEach(function(tab) {
    tab.addEventListener("click", function() {
      activeTab = tab.dataset.tab;
      el.querySelectorAll(".tab").forEach(function(t) { t.classList.remove("active"); });
      tab.classList.add("active");
      applyFilters();
    });
  });
}

function buildRepoFilter() {
  var counts = {};
  document.querySelectorAll(".card").forEach(function(c) {
    (c.dataset.repos || "").split("|").filter(Boolean).forEach(function(r) {
      counts[r] = (counts[r] || 0) + 1;
    });
  });
  var sel = document.getElementById("repoFilter");
  Object.keys(counts).sort(function(a, b) {
    return counts[b] - counts[a] || a.localeCompare(b);
  }).forEach(function(r) {
    var o = document.createElement("option");
    o.value = r; o.textContent = r + " (" + counts[r] + ")";
    sel.appendChild(o);
  });
}

function applyFilters() {
  var cards = document.querySelectorAll(".card");
  var shown = 0;
  cards.forEach(function(c) {
    var ok = true;
    if (activeTab !== "ALL" && c.dataset.tab !== activeTab) ok = false;
    if (ok && keeperFilter && c.dataset.keep !== keeperFilter) ok = false;
    if (ok && repoFilter) {
      var repos = (c.dataset.repos || "").split("|");
      if (repos.indexOf(repoFilter) === -1) ok = false;
    }
    if (ok && searchQuery && (c.dataset.search || "").indexOf(searchQuery) === -1) ok = false;
    c.classList.toggle("hidden", !ok);
    if (ok) shown++;
  });
  document.getElementById("setCount").textContent =
    "Showing " + shown + " of " + cards.length + " candidate sets";
  document.getElementById("emptyState").style.display = shown ? "none" : "block";
}

function init() {
  formatGenTime();
  buildTabs();
  buildRepoFilter();
  applyFilters();

  var debounce;
  document.getElementById("searchInput").addEventListener("input", function(e) {
    searchQuery = e.target.value.toLowerCase();
    clearTimeout(debounce);
    debounce = setTimeout(applyFilters, 120);
  });
  document.getElementById("keeperFilter").addEventListener("change", function(e) {
    keeperFilter = e.target.value; applyFilters();
  });
  document.getElementById("repoFilter").addEventListener("change", function(e) {
    repoFilter = e.target.value; applyFilters();
  });
  document.getElementById("infoToggle").addEventListener("click", function() {
    document.getElementById("infoPanel").classList.toggle("visible");
  });
  document.getElementById("filterToggle").addEventListener("click", function() {
    this.classList.toggle("active");
    document.getElementById("filterRow").classList.toggle("visible");
  });
}

init();
"""


def ordered_counts(values, order):
    counts = Counter(values)
    result = {key: counts[key] for key in order if counts[key]}
    for key in sorted(counts):
        if key not in result:
            result[key] = counts[key]
    return result


def summarize(evaluations, scan_stats):
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "scan": scan_stats,
        "total_sets": len(evaluations),
        "verdicts": ordered_counts(
            (e["verdict"] for e in evaluations),
            ("recommend", "review", "skip"),
        ),
        "duplicate_confidence": ordered_counts(
            (e["duplicate_confidence"] for e in evaluations),
            ("HIGH", "MEDIUM", "LOW", "NONE"),
        ),
        "keeper_confidence": ordered_counts(
            (e["keeper_confidence"] for e in evaluations),
            ("HIGH", "MEDIUM", "LOW", "NONE"),
        ),
    }


def dashboard_data(evaluations, scan_stats):
    return {
        "summary": summarize(evaluations, scan_stats),
        "sets": evaluations,
    }


# HEAD resolves to each repo's default branch (autopkg repos mix main/master).
GITHUB_BLOB = "https://github.com/autopkg/{repo}/blob/HEAD/{path}"


_VERDICT_TAB = {"skip": "SKIP", "review": "REVIEW", "done": "DONE"}
_VERDICT_BADGE = {
    "skip": '<span class="badge badge-skip">Skip</span>',
    "review": '<span class="badge badge-review">Review</span>',
    "done": '<span class="badge badge-done">Done</span>',
}


def tab_group(entry):
    verdict = entry.get("verdict")
    return _VERDICT_TAB.get(verdict) or entry.get("duplicate_confidence") or "NONE"


def status_badge(entry):
    return _VERDICT_BADGE.get(entry.get("verdict"), "")


def conf_badges(entry):
    out = []
    dup = entry.get("duplicate_confidence")
    if dup:
        out.append(
            f'<span class="badge badge-conf-{dup.lower()}" title="Duplicate confidence">'
            f"Dup&nbsp;{escape(dup.title())}</span>"
        )
    keep = entry.get("keeper_confidence")
    if keep and keep != "NONE":
        out.append(
            f'<span class="badge badge-conf-{keep.lower()}" title="Keeper confidence">'
            f"Keep&nbsp;{escape(keep.title())}</span>"
        )
    return "".join(out)


def feature_tags(member, expected_formats=None):
    tags = []
    if member.get("has_codesig"):
        tags.append(("CodeSig", "pos"))
    if member.get("has_endofcheck"):
        tags.append(("EndOfCheck", "pos"))
    if member.get("has_arch_var"):
        tags.append(("Multi-arch", "pos"))
    if member.get("has_release_var"):
        tags.append(("Channel", "pos"))
    source = member.get("source_type")
    if source and source != "unknown":
        tags.append((source, "neutral"))
    member_formats = member.get("artifact_formats") or []
    if expected_formats and not member_formats:
        tags.append(("format unknown", "warn"))
    else:
        for fmt in member_formats:
            cls = "warn" if expected_formats and fmt not in expected_formats else "neutral"
            tags.append((fmt, cls))
    if not tags:
        return ""
    chips = "".join(f'<span class="ftag ftag-{cls}">{escape(label)}</span>' for label, cls in tags)
    return f'<div class="feature-tags">{chips}</div>'


def render_member(member, role, reason, expected_formats=None):
    role_tag = {
        "keep": '<span class="role-tag role-keep">Keep</span>',
        "deprecate": '<span class="role-tag role-deprecate">Depr</span>',
    }.get(role, '<span class="role-tag role-member">&mdash;</span>')

    path = member.get("rel_path", "")
    repo = member.get("repo", "")
    url = GITHUB_BLOB.format(repo=repo, path=path)
    reason_html = f'<div class="recipe-reason">{escape(reason)}</div>' if reason else ""
    deps = member.get("dependent_count", 0)
    return f"""
      <div class="recipe-row">
        {role_tag}
        <div class="recipe-info">
          <div class="recipe-path"><a href="{escape(url)}" target="_blank" rel="noopener">{escape(repo)}<span class="path-rest">/{escape(path)}</span></a></div>
          {reason_html}
          {feature_tags(member, expected_formats)}
        </div>
        <div class="dep-count" title="Dependent recipes">&#8595;{deps}</div>
      </div>"""


RATIONALE_ICONS = {
    "duplicate": ("●", "shared"),
    "artifact": ("◆", "artifact"),
    "keeper": ("✓", "keep"),
    "deprecate": ("✗", "depr"),
}


def render_rationale(entry):
    rationale = entry.get("rationale") or []
    if not rationale:
        return ""
    rows = []
    for item in rationale:
        cat = item.get("category", "")
        text = item.get("text", "")
        if not text:
            continue
        icon, cls = RATIONALE_ICONS.get(cat, ("●", "shared"))
        rows.append(
            f'<div class="set-info-row si-{cls}"><span class="set-info-icon">{icon}</span>'
            f"<span><strong>{escape(cat.title())}:</strong> {escape(text)}</span></div>"
        )
    return f'<div class="set-info">{"".join(rows)}</div>' if rows else ""


def _set_expected_formats(entry):
    """Return the single agreed-upon artifact format for the set, or empty set."""
    known = [
        set(m.get("artifact_formats") or [])
        for m in entry.get("members", [])
        if m.get("artifact_formats")
    ]
    if not known:
        return set()
    union = set().union(*known)
    return union if len(union) == 1 else set()


def render_set(entry):
    keep_lookup = {(item["repo"], item["rel_path"]): item for item in entry.get("keep", [])}
    dep_lookup = {(item["repo"], item["rel_path"]): item for item in entry.get("deprecate", [])}
    expected_formats = _set_expected_formats(entry)
    members_html = []
    for member in entry["members"]:
        key = (member["repo"], member["rel_path"])
        if key in keep_lookup:
            members_html.append(
                render_member(member, "keep", keep_lookup[key].get("reason"), expected_formats)
            )
        elif key in dep_lookup:
            members_html.append(
                render_member(member, "deprecate", dep_lookup[key].get("reason"), expected_formats)
            )
        else:
            members_html.append(render_member(member, None, None, expected_formats))

    banner = ""
    verdict = entry.get("verdict")
    prs = entry.get("prs") or []
    pr_links = " ".join(
        f'<a href="{escape(url)}" target="_blank" rel="noopener">PR</a>' for url in prs
    )
    if verdict == "done":
        banner = (
            f'<div class="banner banner-done"><strong>Resolved.</strong> Merged: {pr_links}</div>'
        )
    elif entry.get("skip_reason"):
        label = "Needs review" if verdict == "review" else "Skipped"
        extra = f" {pr_links}" if pr_links else ""
        banner = f'<div class="banner banner-warn"><strong>{label}:</strong> {escape(entry["skip_reason"])}{extra}</div>'

    match = entry.get("match_reasons", [])
    match_html = f'<div class="match">Matched by: {escape("; ".join(match))}</div>' if match else ""

    repos = sorted({m["repo"] for m in entry["members"]})
    search_terms = [entry.get("app_name", "")]
    for m in entry["members"]:
        search_terms.append(f"{m['repo']}/{m.get('rel_path', '')}")
    search_blob = escape(" ".join(search_terms).lower())

    confcls = (entry.get("duplicate_confidence") or "none").lower()

    return f"""
    <details class="card verdict-{escape(entry["verdict"])} dup-{confcls}"
      data-tab="{tab_group(entry)}"
      data-dup="{escape(entry.get("duplicate_confidence") or "NONE")}"
      data-keep="{escape(entry.get("keeper_confidence") or "NONE")}"
      data-repos="{escape("|".join(repos))}"
      data-search="{search_blob}">
      <summary class="card-hd">
        <span class="expand-arrow">&#9654;</span>
        <span class="card-app">{escape(entry["app_name"])}</span>
        <span class="card-meta">{status_badge(entry)}{conf_badges(entry)}</span>
      </summary>
      <div class="card-body">
        {match_html}
        <div class="members">{"".join(members_html)}</div>
        {render_rationale(entry)}
        {banner}
      </div>
    </details>"""


def render_html(data):
    cards = "\n".join(render_set(entry) for entry in data["sets"])
    summary = data["summary"]
    verdicts = summary.get("verdicts", {})
    dup_conf = summary.get("duplicate_confidence", {})
    scan = summary.get("scan", {})
    repos_involved = len({m["repo"] for s in data["sets"] for m in s["members"]})

    stats = (
        f'<div class="stat-item"><span class="stat-num">{verdicts.get("recommend", 0)}</span> recommendations</div>'
        f'<div class="stat-item"><span class="stat-num stat-num-high">{dup_conf.get("HIGH", 0)}</span> high dup. confidence</div>'
        f'<div class="stat-item"><span class="stat-num stat-num-review">{verdicts.get("review", 0)}</span> to review</div>'
        f'<div class="stat-item"><span class="stat-num">{repos_involved}</span> repos</div>'
        f'<div class="stat-item" style="margin-left:auto" id="genTime" data-iso="{escape(summary.get("generated_at", ""))}"></div>'
    )

    scanned = scan.get("download_recipes", 0)
    total_files = scan.get("total_recipe_files", 0)

    head = (
        '<!doctype html>\n<html lang="en">\n<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        "<title>AutoPkg Duplicate Recipe Review</title>\n"
        "<style>" + CSS + "</style>\n</head>\n<body>\n"
    )

    body = f"""
<div class="header">
  <div class="header-inner">
    <h1>AutoPkg Recipe Deduplication Dashboard</h1>
    <div class="subtitle">Potentially duplicated recipes across the AutoPkg org, categorized and quantified for review.</div>
    <div class="stat-row" id="stats">{stats}</div>
  </div>
</div>

<div class="info-bar">
  <div class="info-bar-inner">
    Maintain a recipe repo?
    <span class="info-toggle" id="infoToggle">See how you can help</span>
  </div>
</div>
<div class="info-panel" id="infoPanel">
  <div class="info-panel-inner">
    <p><strong>Understanding the confidence scores:</strong></p>
    <ul>
      <li><strong>Duplicate confidence</strong> — how certain we are these recipes download the same app from the same source. <em>High:</em> matched on source URL or code-signing identity. <em>Medium:</em> name match plus one corroborating signal. <em>Low:</em> name match only.</li>
      <li><strong>Keeper confidence</strong> — how clearly one recipe outscores the others on quality signals (CodeSignatureVerifier, EndOfCheckPhase, source resilience, architecture support). <em>High:</em> clear winner (score gap ≥ 3). <em>Medium:</em> moderate gap. <em>Low:</em> too close to call — needs human review.</li>
    </ul>
    <p><strong>How recipe maintainers can help:</strong></p>
    <ul>
      <li><strong>Filter by your repo</strong> to find candidate sets that include your recipes.</li>
      <li><strong>Add <code>CodeSignatureVerifier</code> and <code>EndOfCheckPhase</code></strong> so quality signals are explicit.</li>
      <li><strong>Prefer durable providers</strong> (GitHub releases, Sparkle appcasts) over brittle scrape/download URLs.</li>
      <li><strong>Add a description</strong> when a recipe is intentionally distinct (fork, enterprise, portable, rebrand).</li>
      <li><strong>Deprecate duplicates</strong> with a message pointing to the recommended keeper.</li>
    </ul>
    <p>Recommendations are advisory. Always read the actual recipes before acting.</p>
  </div>
</div>

<div class="controls">
  <div class="controls-inner">
    <div class="search-row">
      <input type="text" id="searchInput" placeholder="Search by app name, repo, or path...">
      <button class="filter-toggle" id="filterToggle" aria-label="Toggle filters">&#9776; Filters</button>
    </div>
    <div class="tab-line">
      <span class="tab-label">Dup. confidence</span>
      <div class="tab-strip" id="tabs"></div>
    </div>
    <div class="filter-row" id="filterRow">
      <select id="keeperFilter" aria-label="Filter by keeper confidence">
        <option value="">All keeper confidence</option>
        <option value="HIGH">Keeper: High</option>
        <option value="MEDIUM">Keeper: Medium</option>
        <option value="LOW">Keeper: Low</option>
      </select>
      <select id="repoFilter" aria-label="Filter by repo">
        <option value="">All repos</option>
      </select>
    </div>
  </div>
</div>

<div class="content">
  <div class="set-count" id="setCount"></div>
  <div id="setList">{cards}</div>
  <div class="empty" id="emptyState" style="display:none">No matching sets found.</div>
</div>

<div class="footer">
  Scanned {scanned} download recipes out of {total_files} recipe files.
  Recommendations are AI-free and deterministic, intended as a basis for human review.
  Always read the actual recipes before acting on any recommendation.
</div>
"""

    return head + body + "<script>" + JS + "</script>\n</body>\n</html>\n"


def write_dashboard(output_dir, evaluations, scan_stats):
    output_dir = Path(output_dir)
    data = dashboard_data(evaluations, scan_stats)
    write_json(output_dir / "dashboard.json", data)
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "index.html").write_text(render_html(data), encoding="utf-8")
    return data
