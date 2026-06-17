from dataclasses import dataclass, field


@dataclass
class RecipeRecord:
    repo: str
    rel_path: str
    identifier: str
    display_name: str
    name_key: str
    description: str
    parent_recipe: str
    source_type: str | None
    source_key: str | None
    source_domain: str | None
    processors: list[str]
    input_vars: list[str]
    has_codesig: bool
    has_endofcheck: bool
    has_arch_var: bool
    has_release_var: bool
    codesig_authorities: list[str] = field(default_factory=list)
    artifact_formats: list[str] = field(default_factory=list)
    first_commit: str | None = None
    dependent_count: int = 0
    dependent_repos: list[str] = field(default_factory=list)
    skip_reason: str | None = None


@dataclass
class CandidateSet:
    id: str
    display_name: str
    members: list[RecipeRecord]
    match_reasons: list[str]
    match_strength: str
