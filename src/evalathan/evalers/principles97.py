"""Titles of the 97 architecture principles, and the evidence Archly can cite.

The essays are not copied. A principle with no file to cite stays unscored.
"""

from __future__ import annotations

from dataclasses import dataclass

TITLES: dict[int, str] = {
    1: "Don't put your resume ahead of the requirements",
    2: "Simplify essential complexity; diminish accidental complexity",
    3: "Chances are your biggest problem isn't technical",
    4: "Communication is King; Clarity and Leadership its humble servants",
    5: "Application architecture determines application performance",
    6: "Seek the value in requested capabilities",
    7: "Stand Up!",
    8: "Everything will ultimately fail",
    9: "You're negotiating more often than you think.",
    10: "Quantify",
    11: "One line of working code is worth 500 of specification",
    12: "There is no one-size-fits-all solution",
    13: "It's never too early to think about performance",
    14: "Architecting is about balancing",
    15: "Commit-and-run is a crime.",
    16: "There Can be More than One",
    17: "Business Drives",
    18: "Simplicity before generality, use before reuse",
    19: "Architects must be hands on",
    20: "Continuously Integrate",
    21: "Avoid Scheduling Failures",
    22: "Architectural Tradeoffs",
    23: "Database as a Fortress",
    24: "Use uncertainty as a driver",
    25: "Warning, problems in mirror may be larger than they appear",
    26: "Reuse is about people and education, not just architecture",
    27: "There is no 'I' in architecture",
    28: "Get the 1000ft view",
    29: "Try before choosing",
    30: "Understand The Business Domain",
    31: "Programming is an act of design",
    32: "Give developers autonomy",
    33: "Time changes everything",
    34: "Software Architect has only lowercase a's; deal with it",
    35: "Scope is the enemy of success",
    36: "Value stewardship over showmanship",
    37: "Software architecture has ethical consequences",
    38: "Skyscrapers aren't scalable",
    39: "Heterogeneity Wins",
    40: "It's all about performance",
    41: "Engineer in the white spaces",
    42: "Talk the Talk",
    43: "Context is King",
    44: "Dwarves, Elves, Wizards, and Kings",
    45: "Learn from Architects of Buildings",
    46: "Fight repetition",
    47: "Welcome to the Real World",
    48: "Don't Control, but Observe",
    49: "Janus the Architect",
    50: "Architects focus is on the boundaries and interfaces",
    51: "Empower developers",
    52: "Record your rationale",
    53: "Challenge assumptions - especially your own",
    54: "Share your knowledge and experiences",
    55: "Pattern Pathology",
    56: "Don't Stretch The Architecture Metaphors",
    57: "Focus on Application Support and Maintenance",
    58: "Prepare to pick two",
    59: "Prefer principles, axioms and analogies to opinion and taste",
    60: "Start with a Walking Skeleton",
    61: "It is all about the data",
    62: "Make sure the simple stuff is simple",
    63: "Before anything, an architect is a developer",
    64: "The ROI variable",
    65: "Your system is legacy, design for it.",
    66: "If there is only one solution, get a second opinion",
    67: "Understand the impact of change",
    68: "You have to understand Hardware too",
    69: "Shortcuts now are paid back with interest later",
    70: "Perfect is the Enemy of Good Enough",
    71: "Avoid Good Ideas",
    72: "Great content creates great systems",
    73: "The Business Vs. The Angry Architect",
    74: "Stretch key dimensions to see what breaks",
    75: "If you design it, you should be able to code it.",
    76: "A rose by any other name will end up as a cabbage",
    77: "Stable problems get high quality solutions",
    78: "It Takes Diligence",
    79: "Take responsibility for your decisions",
    80: "Don't Be Clever",
    81: "Choose your weapons carefully, relinquish them reluctantly",
    82: "Your Customer is Not Your Customer",
    83: "It will never look like that",
    84: "Choose Frameworks that play well with others",
    85: "Make a strong business case",
    86: "Control the data, not just the code",
    87: "Pay down your technical debt",
    88: "Don't Be a Problem Solver",
    89: "Build Systems to be Zuhanden",
    90: "Find and retain passionate problem solvers",
    91: "Software doesn't really exist",
    92: "Learn a new language",
    93: "You can't future-proof solutions",
    94: "The User Acceptance Problem",
    95: "The Importance of Consomme",
    96: "For the end-user, the interface is the system",
    97: "Great software is not built, it is grown",
}

# A needle has to name the topic. Broad words such as "code" and "system" are omitted.
PROBES: dict[int, tuple[str, ...]] = {
    1: ("requirement", "requirements", "user story", "acceptance criteria"),
    2: ("accidental complexity", "essential complexity"),
    3: ("stakeholder", "not a technical problem"),
    4: ("communication", "leadership"),
    5: ("performance", "latency", "throughput"),
    6: ("capability", "capabilities"),
    7: ("stand-up", "standup", "daily scrum"),
    8: ("failover", "fault toleran", "will fail", "error handling"),
    9: ("negotiat",),
    10: ("quantif", "metric", "benchmark"),
    11: ("working code",),
    12: ("one-size", "one size fits"),
    13: ("latency budget", "performance budget", "slo"),
    14: ("trade-off", "tradeoff", "balancing"),
    16: ("more than one", "second implementation", "alternative provider"),
    17: ("business domain", "the business"),
    18: ("use before reuse", "simplicity before generality"),
    19: ("hands-on", "hands on"),
    21: ("schedule", "milestone", "roadmap"),
    22: ("trade-off", "tradeoff"),
    24: ("uncertainty",),
    25: ("on call", "incident", "larger than they appear"),
    26: ("onboarding", "office hours"),
    27: ("collaborat", "the team"),
    29: ("prototype", "spike"),
    30: ("business domain", "domain model"),
    32: ("autonomy", "code owners"),
    35: ("out of scope", "scope creep"),
    36: ("stewardship",),
    37: ("ethic", "privacy", "harm"),
    38: ("horizontal scale", "shard"),
    41: ("handoff", "white space"),
    42: ("ubiquitous language", "glossary"),
    43: ("bounded context",),
    46: ("duplication", "don't repeat", "dry "),
    47: ("production", "real world"),
    48: ("observability", "monitoring", "telemetry"),
    50: ("interface", "api boundary", "contract"),
    51: ("empower",),
    53: ("assumption",),
    54: ("share your knowledge", "design doc"),
    55: ("pattern",),
    57: ("maintenance", "on-call", "support"),
    58: ("pick two",),
    59: ("axiom", "principle"),
    60: ("walking skeleton", "end to end", "end-to-end"),
    62: ("keep it simple", "simple stuff"),
    64: ("return on investment", "roi"),
    65: ("legacy", "backward compatible", "migration"),
    66: ("second opinion", "design review"),
    67: ("impact of change", "changelog"),
    68: ("hardware", "cpu", "memory"),
    69: ("technical debt",),
    70: ("good enough",),
    72: ("content model",),
    73: ("business case",),
    74: ("load test", "stress test", "chaos"),
    76: ("naming", "ubiquitous language"),
    77: ("stable problem",),
    79: ("decision record", "responsible"),
    80: ("don't be clever", "straightforward"),
    81: ("framework choice", "library choice"),
    82: ("end user", "end-user"),
    83: ("will not match the mock", "mock"),
    84: ("framework",),
    85: ("business case",),
    87: ("technical debt",),
    90: ("hiring", "maintainers"),
    93: ("future-proof", "future proof"),
    94: ("user acceptance", "uat"),
    96: ("user interface", "command line", "the interface"),
}

assert len(TITLES) == 97


@dataclass(frozen=True)
class Row:
    n: int
    title: str
    score: int | None
    cite: str


def _find(chunks: list[tuple[str, str, str]], needles: tuple[str, ...], kind: str) -> str:
    if not needles:
        return ""
    for rel, text, chunk_kind in chunks:
        if chunk_kind != kind:
            continue
        if any(needle in text for needle in needles):
            return rel
    return ""


def _structural(rels: list[str], lang_count: int, commit_count: int | None) -> dict[int, str]:
    hits: dict[int, str] = {}

    def first(*parts: str) -> str:
        for rel in rels:
            if any(part in rel for part in parts):
                return rel
        return ""

    test = first("/tests/", "/test/", "test_", "_test.", "tests.cs")
    if test:
        hits[15] = test
        hits[78] = test
    ci = first(".github/workflows", "jenkinsfile", ".gitlab-ci", "azure-pipelines")
    if ci:
        hits[20] = ci
    data = first(".sql", "/schema", "migration", ".db")
    if data:
        hits[23] = data
        hits[61] = data
        hits[86] = data
    overview = first("architecture.md", "/adr/", "/adrs/", "/docs/")
    if overview:
        hits[28] = overview
        hits[52] = overview
        hits[75] = overview
    if lang_count >= 2:
        hits[39] = f"{lang_count} languages"
        hits[92] = f"{lang_count} languages"
    if commit_count is not None and commit_count >= 2:
        hits[33] = f"{commit_count} commits"
        hits[97] = f"{commit_count} commits"
    return hits


def infer(
    chunks: list[tuple[str, str, str]],
    rels: list[str],
    lang_count: int,
    commit_count: int | None,
) -> list[Row]:
    """Score each principle from files in this tree. No evidence leaves the score empty."""
    structural = _structural(rels, lang_count, commit_count)
    rows: list[Row] = []
    for n in range(1, 98):
        needles = PROBES.get(n, ())
        doc = _find(chunks, needles, "doc")
        readme = _find(chunks, needles, "readme")
        artifact = structural.get(n, "")
        if doc and artifact:
            score, cite = 4, doc
        elif doc or artifact:
            score, cite = 3, doc or artifact
        elif readme:
            score, cite = 2, readme
        else:
            score, cite = None, ""
        rows.append(Row(n, TITLES[n], score, cite))
    return rows
