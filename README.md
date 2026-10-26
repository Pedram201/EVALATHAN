<p align="center">
  <img src="assets/evalathan-logo.png" alt="Evalathan logo: a red dragon curled into an e" width="280">
</p>

<h1 align="center">E V A L A T H A N</h1>
<p align="center"><i>Making your Product-led growth (PLG) more efficient, robust, and user-friendly!</i></p>

<p align="center">The one-stop evaluation platform for software, engines, agentics, codebases, compilers and languages.</p>

Evalathan grades a product across its life cycle. Evalathan is one evaluation harness; Hydra is the conductor - she orchestrates sixteen evaluators ('evalers'); each evaluator reports against a life-cycle gate.

**v0.2** is a local runner. It does not award a state-of-the-art stamp. A deferred cell is not a fail and not a zero.

```bash
[[CURRENTLY ONLY STANDIN]]
pip install -e ".[dev]"
evalathan scan path\to\tree
evalathan scan path\to\tree --json report.json
```

## Overview & Core Philosophy

EVALATHAN is an open-source (Apache-2.0), Python-based (to be refractored for v1 release) evaluation harness designed to audit and score software projects, codebases, compilers, and AI agent pipelines across their entire lifecycle.

The tool positions itself as a local runner (v0.2) aimed at Product-led growth (PLG) and codebase verification. Rather than generating a single aggregated or opaque score, EVALATHAN uses a conductor engine named Hydra to orchestrate 16 distinct evaluators ("evalers") and output a transparent status matrix.

## Architecture & The 16 Evaluators

EVALATHAN evaluates a project by passing a local directory path (`evalathan scan <path> [--json report.json]`). Its 16 evaluators span four distinct operational categories:

| Category | Evalers | Functionality |
| :--- | :--- | :--- |
| Code Health & Repository Metrics | Devly, Archly, Codely, Refactorly, Mixly | Inspects Git history (commits), presence of architectural documentation, cyclomatic/branching complexity, dead code, code churn/duplication, and language breakdown. |
| Performance & Trade-offs | Runly, Pressly, Triadly | Times micro-benchmarks, reads compression and asset quality logs (image/video/file sizes), and documents the project's prioritization order across cost, latency, and impact. |
| AI Agents & LLM Observability | Tokely, Chorely, Trajectly, Domly, Warrantly | Tracks token delta/reduction metrics, maps multi-agent rosters and responsibilities, counts agent trace steps, tests domain-specific Q&A pairs, and audits whether factual claims link to verifiable evidence. |
| Human Ergonomics & Reporting | Levi, Menschly, Stackly | Evaluates user-centric scorecards, checks for built-in user break timers, and produces an itemized report of completed vs. deferred checks. |

### Unique Features: SELFBELT and FUSS

A standout aspect of the project is its integration of developer and user wellness into the evaluation criteria:

SELFBELT / SELFBELTING: A methodology documented in docs/SELFBELT.md addressing developer fatigue and extended screen time.

FUSS (For-User Session Switch): A modular front-end/desktop widget inside the repository (fuss/) that developers can embed into software to enforce scheduled rest breaks.

Menschly: The evaluator specifically tasked with verifying whether a codebase incorporates real session limiters/timers rather than just vague README promises.

## What v0.2 runs

Sixteen evalers always appear. Hydra is the conductor and is not a seventeenth score. Point the scan at the tree you want graded. A record that lives in another repository is read when that repository is the path you pass.

| Evaler | What it runs |
| :--- | :--- |
| [Archly](GLOSSARY.md#user-content-archly) | Checks for explicit system architecture blueprints and design specs to verify that structural documentation exists alongside the source code. |
| [Chorely](GLOSSARY.md#user-content-chorely) | Maps multi-agent AI ecosystems by inventorying agent roles, tool assignments, and explicit task boundaries. |
| [Codely](GLOSSARY.md#user-content-codely) | Measures structural complexity by scanning decision forks (if-statements, loops, conditionals) across supported language files. |
| [Devly](GLOSSARY.md#user-content-devly) | Audits version control activity by tallying commit history, branches, and timeline cadence without making subjective assumptions about programmer skill. |
| [Domly](GLOSSARY.md#user-content-domly) | Evaluates domain competency by matching domain-specific test questionnaires against reference golden-answer datasets. |
| [Levi](GLOSSARY.md#user-content-levi) | Parses verified user-first scorecards to validate that the software meets empirical usability and accessibility criteria. |
| [Menschly](GLOSSARY.md#user-content-menschly) | Inspects the codebase for real, programmable session limiters and rest timers (like FUSS) that promote developer and user well-being. |
| [Mixly](GLOSSARY.md#user-content-mixly) | Catalogs the exact breakdown of programming languages across the repository to reveal stack composition and maintenance footprints. |
| [Pressly](GLOSSARY.md#user-content-pressly) | Audits media and data compression efficiency by extracting perceptual quality scores (SSIM/PSNR) and file size deltas from pre-run logs. |
| [Refactorly](GLOSSARY.md#user-content-refactorly) | Detects codebase friction by identifying duplicated files, unused/dead code segments, and high-frequency churn hotspots. |
| [Runly](GLOSSARY.md#user-content-runly) | Measures runtime execution speed via quick local micro-benchmarks or by parsing pre-recorded benchmark logs. |
| [Stackly](GLOSSARY.md#user-content-stackly) | Synthesizes the full evaluation scan into a transparent status matrix showing passed, failed, and deferred checks without masking data behind an artificial composite number. |
| [Tokely](GLOSSARY.md#user-content-tokely) | Audits LLM prompt and completion token efficiency by calculating measured consumption reductions between baseline and optimized runs. |
| [Trajectly](GLOSSARY.md#user-content-trajectly) | Evaluates AI agent execution trajectories by parsing the step-by-step action logs, tool invocations, and completion paths of recorded runs. |
| [Triadly](GLOSSARY.md#user-content-triadly) | Validates engineering trade-off alignments by confirming that explicit priorities among cost, latency, and impact are formally documented. |
| [Warrantly](GLOSSARY.md#user-content-warrantly) | Verifies factual grounding by validating that assertions and benchmark results cite inspectable source artifacts, reproducible recipes, or citations. |

Each name opens its glossary entry. An entry has three parts: what is counted, simplespeak, and techspeak. Public agent exams, and why they are not pasted in, are in the [glossary](GLOSSARY.md#user-content-agentic-exams-that-are-not-on-the-vector-yet).

Levi reads a [4Uvals](GLOSSARY.md#user-content-4uvals) card when one is in the tree. 4Uvals (Ultimate User-User-User evaluations) is a 10-check list asking whether a session put the person first. The published card, v1.2, is a pass: 9 of 10 checks Solid or Strong, mean 3.4 out of 4.

## Key Strengths

Holistic Lifecycle View: Most evaluation tools are siloed into either static analysis (e.g., SonarQube, flake8), benchmark profiling (e.g., pytest-benchmark), or LLM observability (e.g., Promptfoo, DeepEval). EVALATHAN attempts to unify traditional software metrics, AI agent evaluations, and human-centric design under one roof.

Honest, Uninflated Scoring Methodology: The system adopts a strict policy that "a deferred cell is not a fail and not a zero," refusing to synthesize dissimilar metrics into an artificial 0–100 score. It reports what was actually measured versus what was skipped.

Clean Packaging: Structured as a modern Python package (pyproject.toml, src/evalathan, tests/), with CLI support and JSON export options for pipeline integration.

Attention to Ergonomics/Ethics: Bringing developer wellness (FUSS/SELFBELT) into code grading is novel and addresses a real blind spot in typical CI/CD quality gates.

## Current Limitations & Areas for Growth

Early Stage (v0.2): The repository has around 27 commits and no public releases or distribution yet (e.g., not yet packaged on PyPI). It is in early development.

Passive Log Parsing vs. Active Execution: Several AI and performance evaluators (e.g., Tokely, Trajectly, Pressly) rely on reading pre-existing log files and saved run artifacts rather than executing live tracing or active benchmarking. If a project lacks standardized log outputs, those cells will simply remain blank/deferred.

AST and Language Parsing Depth: Running branching/decision checks (Codely) across arbitrary compilers and languages is non-trivial; depending on the parsers implemented in src/evalathan/, support for languages outside Python may be basic.

DevOps & Community Infrastructure: The repository would benefit from automated GitHub Actions workflows (CI for linting and running the test suite), documentation generation (Sphinx/MkDocs), and automated release pipelines.

## Current Assessment

Pedram201/EVALATHAN is an ambitious, conceptually fresh evaluation harness. While still in its early stages (v0.2), it stands out for its balanced philosophy: it bridges modern AI agent auditing with classic static analysis while introducing thoughtful developer wellness checks (FUSS/Menschly). For production use, it is best treated as an experimental framework or early-stage evaluation baseline that will mature as active log integrations and language parsers expand.

## SELFBELT

[SELFBELT](docs/SELFBELT.md) (aks Self-Safety or Self-Safetying) is the seatbelt write-up for people who sit with software for a long time. Self-check based ( motto: "It's up to YOU!"). The practice on that page is called SELFBELTING. The PDF itself is too large for GitHub to open in the browser, so the link shows the pages. It is not a seventeenth score. [Menschly](GLOSSARY.md#user-content-menschly) is the evaler that can see a timer. The analogy is the early car: lights and laws arrived before the belt. FUSS is a belt a developer can clip into a product.

## FUSS

[FUSS](fuss/README.md) (For-User Session Switch) is a small panel. The logo sits in the center. It asks whether to time this sitting, then lets a person set minutes, reminder spacing, days, and an optional end date. Copy the `fuss` folder into a web page or a desktop web view. The same files run on Windows and Mac. FUSS is optional. A sentence that merely names it is not a timer.

## License

Apache-2.0 for this runner and these rules. The name Evalathan is the product name. Hosted runs are not part of v0.2.

## Not in this version

No hosted site, no invented token percent, no leaderboard copied from somewhere else, and no grade for a tree that is not on disk.
