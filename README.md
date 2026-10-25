<p align="center">
  <img src="assets/evalathan-logo.png" alt="Evalathan logo: a red dragon curled into an e" width="280">
</p>

<h1 align="center">E V A L A T H A N</h1>
<p align="center"><i>Making your Product-led Growth (PLG) more robust and user-friendly!</i></p>

<p align="center">The one-stop evaluation platform for software, engines, codebases, compilers and languages.</p>

Evalathan grades a product across its life cycle. Evalathan is one evaluation harness; Hydra is the conductor - she orchestrates sixteen evaluators ('evalers'); each evaluator reports against a life-cycle gate.

**v0.2** is a local runner. It does not award a state-of-the-art stamp. A deferred cell is not a fail and not a zero.

```bash
pip install -e ".[dev]"
evalathan scan path\to\tree
evalathan scan path\to\tree --json report.json
```

## Overview and core philosophy

Evalathan, developed by Pedram201, is an open-source Apache-2.0 Python harness. It grades a software tree where the artifact is on disk: a product, a language implementation, a compiler, or an engine. Agent records count when those records are in the same tree.

v0.2 is a local runner. Hydra is the conductor. She calls the sixteen evalers and writes a status matrix. A deferred cell is not a fail and not a zero. The report says what ran, what passed its own rule, and what stayed blank. It does not mint one blended score.

The commands above are the whole scan: `evalathan scan` on a folder, with an optional JSON report (JavaScript Object Notation - a text file written next to the terminal output).

## Architecture and the sixteen evalers

The sixteen always appear. Hydra is not a seventeenth score. The lanes below are a reading order. They are not four extra grades.

| Lane | Evalers | What that lane is for |
|------|---------|------------------------|
| Repository and source | Archly, Codely, Devly, Mixly, Refactorly | A commit count, a write-up on disk, decision points this version can parse, copied or unused code, recent change, and the language mix. |
| Speed, a printed size, and a written priority | Pressly, Runly, Triadly | A short local timing, a quality or size figure a tool already printed, and the order a team wrote down for cost, speed, and impact. |
| Tokens, roster, trace, questions, and claims | Chorely, Domly, Tokely, Trajectly, Warrantly | A saved token pair, a roster count, saved agent steps, a question list, and a claim that points at evidence. |
| Scorecard, timer, and the cover sheet | Levi, Menschly, Stackly | A saved user-first scorecard, a real rest timer, and the vector of the other cells. |

## What v0.2 runs

Sixteen evalers always appear. Hydra is the conductor and is not a seventeenth score. Point the scan at the tree you want graded. A record that lives in another repository is read when that repository is the path you pass. The table is alphabetical.

| Evaler | What it runs |
|--------|----------------|
| [Archly](GLOSSARY.md#archly) | Checks that a structural write-up exists alongside the source, such as a README or a document in a docs folder. Finding the write-up is the result. This run does not grade the design. |
| [Chorely](GLOSSARY.md#chorely) | Counts the agent roster and the rows that say what each agent does. A person still decides whether the roster is right. |
| [Codely](GLOSSARY.md#codely) | Counts decision forks, such as an if, a loop, or a catch, in the programming language this scan can measure. A language it cannot measure stays blank. That blank is not a pass. |
| [Devly](GLOSSARY.md#devly) | Tallies commit history. That count is repository activity. It does not grade programmer skill. |
| [Domly](GLOSSARY.md#domly) | Counts a question list shipped with the project, and lines up answers when a second file is there. A language test suite is a different station. |
| [Levi](GLOSSARY.md#levi) | Reads a saved user-first scorecard, when the project includes one, and reports that scorecard's own result. A kind sentence in the README is not the score. |
| [Menschly](GLOSSARY.md#menschly) | Looks for a real, programmable session limiter in the program, such as [FUSS](fuss/README.md) (For-User Session Switch - an optional rest timer). Words about breaks in a README are not a timer. |
| [Mixly](GLOSSARY.md#mixly) | Catalogs the share of recognized source files in each programming language. It reports the mix. It does not tell you to rewrite anything. |
| [Pressly](GLOSSARY.md#pressly) | Reads a picture-quality number, a video-quality number, or a file size that a tool already printed in a log. It does not run the compressor itself. |
| [Refactorly](GLOSSARY.md#refactorly) | Finds duplicated files, unused code, and the files that have been changing the most. It reports those facts. It does not order a rewrite. |
| [Runly](GLOSSARY.md#runly) | Times a short local run when the project contains code it can time. It notes a saved speed-test file only when that file is already in the folder. |
| [Stackly](GLOSSARY.md#stackly) | Writes what ran, what passed its own rule, and what stayed blank. It does not hide that list behind one composite number. |
| [Tokely](GLOSSARY.md#tokely) | Reads a saved before-and-after token count and reports the drop. A measured zero is a real result. If the pair was never saved, the cell stays blank. |
| [Trajectly](GLOSSARY.md#trajectly) | Counts the saved steps of an agent run already in the folder. A screenshot of someone else's scoreboard is not a run. |
| [Triadly](GLOSSARY.md#triadly) | Records the order a team wrote down for cost, speed, and impact. Writing the order down is the result. Proving the build followed it is a later check. |
| [Warrantly](GLOSSARY.md#warrantly) | Checks that each saved claim points at a source, a recipe, or other evidence. A claim with nothing behind it does not pass. No claim list stays blank. |

Each name opens its glossary entry. An entry has three parts: what is counted, simplespeak, and techspeak. Public agent exams, and why they are not pasted in, are in the [glossary](GLOSSARY.md#agentic-exams-that-are-not-on-the-vector-yet).

## Key strengths

The sixteen sit in one harness: repository facts, a speed or size reading, an agent record, a user scorecard, and a timer. A deferred cell is not a fail and not a zero. The report says what was measured and what stayed blank.

The package is a normal Python project: `pyproject.toml`, `src/evalathan`, tests, a command-line scan, and a JSON report.

SELFBELT is the seatbelt write-up for long sittings. FUSS is an optional timer a developer can clip into a product. Menschly is the evaler that can see a real timer. Those three are not a seventeenth score.

## Current limitations and areas for growth

v0.2 is early. It is not on PyPI. Hosted runs are not part of this version. No GitHub Actions workflow is in the tree, so the tests are not run by a remote check yet. A docs generator and a release pipeline are not in this version either.

Tokely, Trajectly, and Pressly read a file the project already saved. If that file is missing, the cell stays blank. Runly also times a short Python loop on this machine when the tree contains Python.

Codely's branch count runs on Python. The other named language packs are not executed in this version. An unknown language stays blank.

## Current assessment

Pedram201/EVALATHAN is a local baseline with a locked rule: score the artifact that is there, and leave the rest blank. It is the right shape for a tree you can point at a folder. It is early for a production gate. Cells that need a saved file stay blank until that file is in the tree. Language packs beyond Python are named and not yet executed.

## SELFBELT

[SELFBELT](docs/SELFBELT.md) is the seatbelt write-up for people who sit with software for a long time. The practice on that page is called SELFBELTING. The PDF itself is too large for GitHub to open in the browser, so the link shows the pages. It is not a seventeenth score. [Menschly](GLOSSARY.md#menschly) is the evaler that can see a timer. The analogy is the early car: lights and laws arrived before the belt. FUSS is a belt a developer can clip into a product.

## FUSS

[FUSS](fuss/README.md) (For-User Session Switch) is a small panel. The logo sits in the center. It asks whether to time this sitting, then lets a person set minutes, reminder spacing, days, and an optional end date. Copy the `fuss` folder into a web page or a desktop web view. The same files run on Windows and Mac. FUSS is optional. A sentence that merely names it is not a timer.

## License

Apache-2.0 for this runner and these rules. The name Evalathan is the product name. Hosted runs are not part of v0.2.

## Not in this version

No hosted site, no invented token percent, no leaderboard copied from somewhere else, and no grade for a tree that is not on disk.
