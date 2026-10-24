<p align="center">
  <img src="assets/evalathan-logo.png" alt="Evalathan logo: a red dragon curled into an e" width="280">
</p>

<h1 align="center">E V A L A T H A N</h1>
<p align="center"> Making your PLGs (product-lead-growth) more superb and user centric

<p align="center"> The one-stop evaluation platform for software, languages, compilers, and engines.

Evalathan grades a product across its life cycle. Evalathan is one evaluation harness; Hydra is the conductor - she orchestrates sixteen evaluators ('evalers'); each evaluator reports against a life-cycle gate.

**v0.2** is a local runner. It does not award a state-of-the-art stamp. A deferred cell is not a fail and not a zero.

```bash
pip install -e ".[dev]"
evalathan scan path\to\tree
evalathan scan path\to\tree --json report.json
```

## What v0.2 runs

Sixteen evalers always appear. Hydra is the conductor and is not a seventeenth score. Point the scan at the tree you want graded. A record that lives in another repository is read when that repository is the path you pass.

| Evaler | What it runs |
|--------|----------------|
| [Devly](GLOSSARY.md#devly) | Counts how many times this project has been saved in git. That is a history fact. It does not grade the programmer. |
| [Archly](GLOSSARY.md#archly) | Looks for an architecture write-up. If it finds one, it records that the write-up is there. It does not grade that write-up again on this run. |
| [Codely](GLOSSARY.md#codely) | Counts the places where the code chooses, such as an if or a loop, in the programming language this scan can measure. A language it cannot measure stays blank. That blank is not a pass. |
| [Refactorly](GLOSSARY.md#refactorly) | Finds files that are copies of each other, code that nothing else uses, and the files that have been changing the most. |
| [Mixly](GLOSSARY.md#mixly) | Shows what share of the project is written in each programming language. It does not tell you to rewrite anything. |
| [Runly](GLOSSARY.md#runly) | Times a short run on this machine when the project contains code it can time. It reads a saved speed-test file only when that file is already in the folder. |
| [Levi](GLOSSARY.md#levi) | Reads a saved user-first scorecard, when the project includes one, and reports that scorecard's own result. A kind sentence in the README is not the score. |
| [Menschly](GLOSSARY.md#menschly) | Looks for a real timer in the program that asks a person to stop. Words about breaks in a README are not a timer. [FUSS](fuss/README.md) is one optional timer you can drop in. |
| [Tokely](GLOSSARY.md#tokely) | Reads a saved before-and-after token count. The saving is the drop from before to after. A measured zero is a real result. If the pair was never saved, the cell stays blank. |
| [Pressly](GLOSSARY.md#pressly) | Reads a picture-quality number, a video-quality number, or a file size that a tool already printed in a log. It does not run the compressor itself. |
| [Triadly](GLOSSARY.md#triadly) | Records the order a team wrote down for cost, speed, and impact. Writing the order down is the result. Proving the build followed it is a later check. |
| [Chorely](GLOSSARY.md#chorely) | Counts the agent roster and how many rows say what that agent does. A person still decides whether the roster is right. |
| [Trajectly](GLOSSARY.md#trajectly) | Counts the saved steps of an agent run that is already in the folder. A screenshot of someone else's scoreboard is not a run. |
| [Warrantly](GLOSSARY.md#warrantly) | Checks that each saved claim points at a source, a recipe, or other evidence. A claim with nothing behind it does not pass. |
| [Domly](GLOSSARY.md#domly) | Counts a list of questions shipped with the project, and matches answers when a second file is there. A language test suite is a different station. |
| [Stackly](GLOSSARY.md#stackly) | Writes what ran, what passed, and what stayed blank. It does not mash those lines into one number. |

Each name opens its glossary entry. An entry has three parts: what is counted, simplespeak, and techspeak. Public agent exams, and why they are not pasted in, are in the [glossary](GLOSSARY.md#agentic-exams-that-are-not-on-the-vector-yet).

## SELFBELT

[SELFBELT](docs/SELFBELT.md) is the seatbelt write-up for people who sit with software for a long time. The practice on that page is called SELFBELTING. The PDF itself is too large for GitHub to open in the browser, so the link shows the pages. It is not a seventeenth score. [Menschly](GLOSSARY.md#menschly) is the evaler that can see a timer. The analogy is the early car: lights and laws arrived before the belt. FUSS is a belt a developer can clip into a product.

## FUSS

[FUSS](fuss/README.md) (For-User Session Switch) is a small panel. The logo sits in the center. It asks whether to time this sitting, then lets a person set minutes, reminder spacing, days, and an optional end date. Copy the `fuss` folder into a web page or a desktop web view. The same files run on Windows and Mac. FUSS is optional. A sentence that merely names it is not a timer.

## License

Apache-2.0 for this runner and these rules. The name Evalathan is the product name. Hosted runs are not part of v0.2.

## Not in this version

No hosted site, no invented token percent, no leaderboard copied from somewhere else, and no grade for a tree that is not on disk.
