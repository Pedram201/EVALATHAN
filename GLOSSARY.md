<h1><img src="assets/glossary/title.png" alt="Evalathan glossary" height="33"></h1>

Evalathan is one evaluation harness. Hydra is the conductor. She governs and calls sixteen evaluators, short name evalers. Each entry below has the same three parts.

<img src="assets/glossary/score-constitution-dot.png" alt="Score constitution." height="14"> What is counted, whether that count is a yes-or-no pass, and the three endings a cell can have. Measured means the file or the code was there and a result was written. Claim means a sentence is on disk and this run did not re-check it. Blank means the needed record is missing. A blank is not a fail and not a zero.

<img src="assets/glossary/simplespeak-dot.png" alt="Simplespeak." height="17"> The same job in ordinary words.

<img src="assets/glossary/techspeak-dot.png" alt="Techspeak." height="17"> What the code actually reads, and the standard it cites when that standard is really in play. A link is the public text of that standard. Citing it is not a certificate.

The life-cycle gate on each evaler (G0 through G12) is the station's place in the life of a product. There are not sixteen gates. There are sixteen evalers.


<p><img src="assets/term-rule.png" alt="" width="100%" height="18"></p>

<a id="devly" name="devly"></a>
<h2><img src="assets/glossary/devly.png" alt="Devly" height="25"></h2>

<h3><img src="assets/glossary/score-constitution.png" alt="Score constitution" height="17"></h3>

Devly counts commits in git. The count is a measurement. It is not a yes-or-no pass, because a long history is not a skill grade. No claim-only state: either the git history is there, or the cell is blank.

<h3><img src="assets/glossary/simplespeak.png" alt="Simplespeak" height="21"></h3>

Devly tells you how many times this project has been saved in git. That is a fact about the history. It does not grade the programmer, and it does not hand out a job level.

<h3><img src="assets/glossary/techspeak.png" alt="Techspeak" height="21"></h3>

The scan runs `git rev-list --count HEAD` when a `.git` folder is present and writes that integer. `passed` stays empty. If there is no git history, the cell is blank. Skills Framework for the Information Age (SFIA, a job-skill scale for technology work) is named so that nobody reads a level into the commit count. Devly does not award an SFIA level. The public framework is at [sfia-online.org](https://sfia-online.org/en/about-sfia).


<p><img src="assets/term-rule.png" alt="" width="100%" height="18"></p>

<a id="archly" name="archly"></a>
<h2><img src="assets/glossary/archly.png" alt="Archly" height="25"></h2>

<h3><img src="assets/glossary/score-constitution.png" alt="Score constitution" height="17"></h3>

Archly asks one question on this run: is there a written description of how the software is shaped? A README, or a document in a docs folder, counts as that write-up. The cell then says the write-up is present. It does not grade the 97 principles. If no write-up is in the folder, the cell is blank. A blank means the document is missing. It is not a bad grade.

<h3><img src="assets/glossary/simplespeak.png" alt="Simplespeak" height="21"></h3>

Before anyone scores a design, they need a shared list of what a good design explanation covers. That list is the 97 principles. They come from a book, *97 Things Every Software Architect Should Know*. More than 50 working architects wrote it. In this project that author group is called MoE: many expert practitioners, fifty-plus of them, each writing one lesson they had learned on real systems.

A principle here is a short lesson, not a law. One lesson might say: name the tradeoff. Another might say: the diagram is for the people who will live with the system, not for the person who drew it. Another might say: do not invent a part you cannot explain. Read one after another and you get a picture of how an architect is supposed to think.

You use the 97 like a checklist next to a write-up. Does this README say how the parts divide? Does it say what was left out, and why? Does it match the stage the team claims, a sketch or a system that already runs? Archly's job today is the step before that checklist. It looks for the write-up. It does not walk all 97 lessons and hand out a mark.

<h3><img src="assets/glossary/techspeak.png" alt="Techspeak" height="21"></h3>

The public contents of the 97 principles are listed at [97 Things Every Software Architect Should Know](https://yoshi389111.github.io/kinokobooks/soft_en/index.html). MoE means that panel of expert authors, more than 50 of them. Their published lessons are the checklist. They do not log in and score the repository.

The scan treats these as a write-up: a README, or markdown inside a folder named `docs`, `doc`, or `architecture`, or a saved architecture review already sitting in the tree. In every case the status is a claim. The document is on disk. This run does not score the 97 lines. The international description of an architecture review is [ISO/IEC/IEEE 42030](https://www.iso.org/standard/73436.html). Archly does not issue that certificate. Five public standards sit beside the 97 as extra reading, not as a grade this scan computes: [NASA Technology Readiness Level](https://www.nasa.gov/directorates/somd/space-communications-navigation-program/technology-readiness-level/), [ISO/IEC 25010](https://www.iso.org/standard/78176.html), ISO/IEC/IEEE 42030, [SEI ATAM](https://en.wikipedia.org/wiki/Architecture_tradeoff_analysis_method), and [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected/).


<p><img src="assets/term-rule.png" alt="" width="100%" height="18"></p>

<a id="codely" name="codely"></a>
<h2><img src="assets/glossary/codely.png" alt="Codely" height="25"></h2>

<h3><img src="assets/glossary/score-constitution.png" alt="Score constitution" height="17"></h3>

Codely counts decision points in source that this version can parse. The count is a measurement, not a pass, because a branch count has no winner line. A language this version does not measure is a blank, and that blank is not a pass. A README claim about code quality is not read as a score.

<h3><img src="assets/glossary/simplespeak.png" alt="Simplespeak" height="21"></h3>

Codely looks through the code and counts the places where the program chooses, such as an if, a loop, or a catch. It reports the programming language it was able to measure. If it cannot measure the language you used, it says so and leaves the cell blank. That blank is not a gold star.

<h3><img src="assets/glossary/techspeak.png" alt="Techspeak" height="21"></h3>

The Python pack walks the syntax tree and counts `if`, `for`, `while`, `except`, `with`, and `assert` nodes inside functions. Named packs that are not executed in this version: JavaScript, TypeScript, C, C++, Rust, Go, and Java. An unknown suffix is a blank whose summary says it is not a pass. pytest, coverage, radon, and ISO/IEC 5055 are not launched. [ISO/IEC 5055](https://www.iso.org/standard/80623.html) is automated source-code quality measures. A radon run is not a 5055 result, and this scanner does not produce one.


<p><img src="assets/term-rule.png" alt="" width="100%" height="18"></p>

<a id="refactorly" name="refactorly"></a>
<h2><img src="assets/glossary/refactorly.png" alt="Refactorly" height="25"></h2>

<h3><img src="assets/glossary/score-constitution.png" alt="Score constitution" height="17"></h3>

Refactorly writes three measurements: copied files, unused names, and recent change. None of the three is a yes-or-no pass. There is no claim-only state. A folder with no files to hash is a blank.

<h3><img src="assets/glossary/simplespeak.png" alt="Simplespeak" height="21"></h3>

Refactorly looks for files that are copies of each other, for code that nothing else uses, and for the files that have been changing the most. It reports those facts. It does not order you to rewrite the project.

<h3><img src="assets/glossary/techspeak.png" alt="Techspeak" height="21"></h3>

Identical-byte groups are SHA-256 matches among files between 1 and 200,000 bytes. Unused names are Python functions and classes that are defined and never referenced, skipping names that start with `_` or `test`. Change is `git log --numstat` over the last 40 commits when git exists. The unused-name walk is the one language-specific check in this version. The copy check and the change check apply to whatever files are in the tree.


<p><img src="assets/term-rule.png" alt="" width="100%" height="18"></p>

<a id="mixly" name="mixly"></a>
<h2><img src="assets/glossary/mixly.png" alt="Mixly" height="26"></h2>

<h3><img src="assets/glossary/score-constitution.png" alt="Score constitution" height="17"></h3>

Mixly writes the share of files by programming language. The share is the result. It is not a pass, and it is not an order to rewrite. A tree with no recognized source is a blank. There is no claim-only state.

<h3><img src="assets/glossary/simplespeak.png" alt="Simplespeak" height="21"></h3>

Mixly tells you what portion of the project is written in each programming language it recognizes. The number is the mix. What you do with that mix stays with the maintainer.

<h3><img src="assets/glossary/techspeak.png" alt="Techspeak" height="21"></h3>

Suffixes map to a language name: Python, JavaScript, TypeScript, C, C++, Rust, Go, Java, Kotlin, Ruby, PHP, C#, Swift, MEL, and VEX. The summary is a percentage of recognized files. Mixly does not parse those files and does not rank the languages.


<p><img src="assets/term-rule.png" alt="" width="100%" height="18"></p>

<a id="runly" name="runly"></a>
<h2><img src="assets/glossary/runly.png" alt="Runly" height="25"></h2>

<h3><img src="assets/glossary/score-constitution.png" alt="Score constitution" height="17"></h3>

When the tree can be timed, Runly writes a duration. That duration is a measurement, not a pass, because a stopwatch has no winner line of its own. A published suite file is reported when the file is present. Runly does not launch SPEC or the LLVM test suite. A tree with nothing to time and no suite file is a blank.

<h3><img src="assets/glossary/simplespeak.png" alt="Simplespeak" height="21"></h3>

Runly times a short piece of work on this machine when the project contains code it can time. If the folder also contains a saved speed-test file, Runly says that file is there. It does not pretend a missing lab benchmark was run.

<h3><img src="assets/glossary/techspeak.png" alt="Techspeak" height="21"></h3>

Any tree with Python source gets a local microbench: 200,000 integer steps, reported in milliseconds, labeled as an Evalathan microbench. Files whose names contain `pyperformance`, `spec2017`, or `llvm-test-suite` are noted and not executed. SPEC CPU is the industry suite at [spec.org](https://www.spec.org/cpu2017/). The LLVM test suite is a compiler project, not a file this scanner invents. [ISO/IEC 25010](https://www.iso.org/standard/78176.html) describes product quality, including performance efficiency. Runly does not compute a 25010 score.


<p><img src="assets/term-rule.png" alt="" width="100%" height="18"></p>

<a id="levi" name="levi"></a>
<h2><img src="assets/glossary/levi.png" alt="Levi" height="20"></h2>

<h3><img src="assets/glossary/score-constitution.png" alt="Score constitution" height="17"></h3>

Levi scores only a 4Uvals record that already contains a gate. If that gate says PASS, this cell passes. If it says FAIL, this cell fails. Any other gate text is a measurement with no pass flag. A README that merely uses user-interest words is a claim, not a score. No record and no such words is a blank.

<h3><img src="assets/glossary/simplespeak.png" alt="Simplespeak" height="21"></h3>

Levi reads a saved user-first scorecard if the project includes one. It reports that scorecard's own result, including the mean and the pass or fail. It does not invent the scorecard. A friendly sentence in the README is not the score.

<h3><img src="assets/glossary/techspeak.png" alt="Techspeak" height="21"></h3>

The file must be JSON whose family or brand contains `4uval`, with a `gate` object. The summary prints `gate.mean` and `gate.result`. 4Uvals (Ultimate User-User-User evaluations) is the ten-check user-first scorecard. [ISO/IEC 42001](https://www.iso.org/standard/81230.html) is an AI management system for a firm. Levi names it as a wrapper beside the sitting. It is not the grade.


<p><img src="assets/term-rule.png" alt="" width="100%" height="18"></p>

<a id="menschly" name="menschly"></a>
<h2><img src="assets/glossary/menschly.png" alt="Menschly" height="25"></h2>

<h3><img src="assets/glossary/score-constitution.png" alt="Score constitution" height="17"></h3>

A real timer in the source is a pass. The timer can be FUSS or any other real stop. A README that only talks about breaks is a claim, and `passed` stays empty. No timer and no such sentence is a blank. A compiler or a batch tool with no sitting stays blank, which is the honest ending.

<h3><img src="assets/glossary/simplespeak.png" alt="Simplespeak" height="21"></h3>

Menschly asks whether the program can tell a person to stop. A timer in the code counts. A paragraph in the README does not. FUSS is one timer you can drop in. It is optional. The full habit write-up is [SELFBELT](docs/SELFBELT.pdf).

<h3><img src="assets/glossary/techspeak.png" alt="Techspeak" height="21"></h3>

A Python function named `bind_fuss` or `bindfuss`, or an assignment to `session_limit_minutes`, is a timer. In JavaScript, `function bindFuss` is a timer, including the copy in [fuss/fuss.js](fuss/fuss.js). A file whose name is `fuss` is a timer. The provisional phrases are "take a break", "session limit", and "time budget". The bare word fuss is not enough. FUSS (For-User Session Switch) is the drop-in panel in [fuss/README.md](fuss/README.md). This is not a medical device and not an ISO certificate.


<p><img src="assets/term-rule.png" alt="" width="100%" height="18"></p>

<a id="tokely" name="tokely"></a>
<h2><img src="assets/glossary/tokely.png" alt="Tokely" height="25"></h2>

<h3><img src="assets/glossary/score-constitution.png" alt="Score constitution" height="17"></h3>

Tokely writes before, after, and savings from a sealed pair. Savings are `max(0, before - after)`. A measured zero is a legal result. `passed` stays empty, because a token drop is not a yes-or-no gate. No sealed pair is a blank. A product that computes tokens in memory and never writes the pair stays blank.

<h3><img src="assets/glossary/simplespeak.png" alt="Simplespeak" height="21"></h3>

Tokely reads a before-and-after token count that was saved in the project. It subtracts and keeps the drop. Zero is a real answer. If nobody saved the pair, Tokely stays blank rather than guessing.

<h3><img src="assets/glossary/techspeak.png" alt="Techspeak" height="21"></h3>

JSON may use `before` and `after`, or `total_tokex` and `tokex_this_run`, including those keys inside a `tokex` object. TOKEX (Token Expenditure) is the name of that count. Tokely does not import a tokenizer and does not call a model. Pressly's byte counts are a different measurement.


<p><img src="assets/term-rule.png" alt="" width="100%" height="18"></p>

<a id="pressly" name="pressly"></a>
<h2><img src="assets/glossary/pressly.png" alt="Pressly" height="25"></h2>

<h3><img src="assets/glossary/score-constitution.png" alt="Score constitution" height="17"></h3>

Pressly writes a quality number or a size that a tool already printed. The number is a measurement, not a pass. A byte figure in a text file is not treated as a video grade and not as a token saving. No such printout is a blank.

<h3><img src="assets/glossary/simplespeak.png" alt="Simplespeak" height="21"></h3>

Pressly looks for a picture-quality number, a video-quality number, or a file size that some tool already wrote into a log. It does not run the compressor itself. If the log is not there, the cell stays blank.

<h3><img src="assets/glossary/techspeak.png" alt="Techspeak" height="21"></h3>

Logs, text, JSON, and markdown are scanned for `ssim`, `vmaf`, or `bytes`/`size` followed by a colon or an equals sign and a number. SSIM (structural similarity, a picture-likeness score) is described at [Wikipedia](https://en.wikipedia.org/wiki/Structural_similarity). VMAF (Video Multi-Method Assessment Fusion, Netflix's video-quality score) is at [Netflix/vmaf](https://github.com/Netflix/vmaf). A match is reported as a printed figure. It is not a TOKEX result.


<p><img src="assets/term-rule.png" alt="" width="100%" height="18"></p>

<a id="triadly" name="triadly"></a>
<h2><img src="assets/glossary/triadly.png" alt="Triadly" height="26"></h2>

<h3><img src="assets/glossary/score-constitution.png" alt="Score constitution" height="17"></h3>

A declared order of cost, speed, and impact is a measurement of the declaration. `passed` stays empty, because this run does not check that the build followed the order. The six-letter codes are the declaration. The bare letters M3 in a sentence are not. No code is a blank.

<h3><img src="assets/glossary/simplespeak.png" alt="Simplespeak" height="21"></h3>

Triadly records the priority order a team wrote down: what they put first among cost, speed, and impact. Writing the order down is the result. Proving the build followed it needs a second artifact that repeats the same order.

<h3><img src="assets/glossary/techspeak.png" alt="Techspeak" height="21"></h3>

The accepted compact orders are `mcmemi`, `mcmime`, `memcmi`, `memimc`, `mimcme`, and `mimemc`, read from the README and from markdown, JSON, and text. The scan looks for those codes with spaces removed. It does not treat the word M3, by itself, as an order.


<p><img src="assets/term-rule.png" alt="" width="100%" height="18"></p>

<a id="chorely" name="chorely"></a>
<h2><img src="assets/glossary/chorely.png" alt="Chorely" height="25"></h2>

<h3><img src="assets/glossary/score-constitution.png" alt="Score constitution" height="17"></h3>

Chorely counts roster files and rows. The count is a measurement, not a pass, because a person still decides whether the roster is right. No roster is a blank. There is no claim-only state.

<h3><img src="assets/glossary/simplespeak.png" alt="Simplespeak" height="21"></h3>

Chorely counts the list of agents in the project and how many rows say what that agent does. The count is the result. Judgment stays with a human.

<h3><img src="assets/glossary/techspeak.png" alt="Techspeak" height="21"></h3>

Roster files are `agent_registry.md`, `agents.md`, `agentic_registry.md`, or any markdown file inside a folder named `agents`. Rows that start with a bold table cell are counted. SASPIANT (Specific and Specialized, Pain-In-the-Ass, Non-critical Tasks) is the question the roster is for: is this a narrow chore, or a person-shaped decision. Chorely counts. It does not answer that question for you.


<p><img src="assets/term-rule.png" alt="" width="100%" height="18"></p>

<a id="trajectly" name="trajectly"></a>
<h2><img src="assets/glossary/trajectly.png" alt="Trajectly" height="26"></h2>

<h3><img src="assets/glossary/score-constitution.png" alt="Score constitution" height="17"></h3>

Trajectly counts saved trace steps that are already in the tree. The count is a measurement, not a pass. A public leaderboard percent is not evidence and is not copied. No trace file is a blank. A library or a compiler with no agent loop stays blank.

<h3><img src="assets/glossary/simplespeak.png" alt="Simplespeak" height="21"></h3>

Trajectly looks for a recording of an agent run that was saved in the project, and it counts the steps. A screenshot of someone else's scoreboard is not a recording. If the recording is not in the folder, the cell stays blank.

<h3><img src="assets/glossary/techspeak.png" alt="Techspeak" height="21"></h3>

File names containing `trace`, `trajectory`, or `passk` are read. JSONL lines that parse as JSON are counted as steps. Other matching files count as one step. The summary says the count is from files in the tree.


<p><img src="assets/term-rule.png" alt="" width="100%" height="18"></p>

<a id="warrantly" name="warrantly"></a>
<h2><img src="assets/glossary/warrantly.png" alt="Warrantly" height="25"></h2>

<h3><img src="assets/glossary/score-constitution.png" alt="Score constitution" height="17"></h3>

Warrantly reads a claim list. It passes only when every claim carries a source, a recipe, or an evidence field. A partial list is a measurement with `passed` empty. A README that names a recipe without the register is a measurement with `passed` empty. No register is a blank.

<h3><img src="assets/glossary/simplespeak.png" alt="Simplespeak" height="21"></h3>

Warrantly checks that each claim in a saved list points at something behind it: a source, a recipe, or other evidence. If every claim has that backing, the cell passes. A claim with nothing behind it does not.

<h3><img src="assets/glossary/techspeak.png" alt="Techspeak" height="21"></h3>

JSON may be a list of objects with a `claim` key, or an object with `claims` or `warrants`. Backing is any of `source`, `recipe`, or `evidence`. The pass flag is true only when the backed count equals the claim count and the list is not empty.


<p><img src="assets/term-rule.png" alt="" width="100%" height="18"></p>

<a id="domly" name="domly"></a>
<h2><img src="assets/glossary/domly.png" alt="Domly" height="25"></h2>

<h3><img src="assets/glossary/score-constitution.png" alt="Score constitution" height="17"></h3>

Domly counts questions in a versioned bank, and matches answers when a second file is present. The count is a measurement, not a pass. A language conformance suite is not this bank. No bank is a blank.

<h3><img src="assets/glossary/simplespeak.png" alt="Simplespeak" height="21"></h3>

Domly looks for a list of questions shipped with the project. If a second file holds answers, it says how they line up. A test suite for a programming language is a different station. If the question list is missing, Domly stays blank.

<h3><img src="assets/glossary/techspeak.png" alt="Techspeak" height="21"></h3>

JSON or YAML files whose names contain `question` or `answer` are read. Questions are counted. Answers are matched by `id` when an answers file exists. `passed` stays empty. Runly and Codely remain the stations for a language conformance suite.


<p><img src="assets/term-rule.png" alt="" width="100%" height="18"></p>

<a id="stackly" name="stackly"></a>
<h2><img src="assets/glossary/stackly.png" alt="Stackly" height="25"></h2>

<h3><img src="assets/glossary/score-constitution.png" alt="Score constitution" height="17"></h3>

Stackly runs last. If any other evaler measured or recorded a claim, Stackly writes the vector: how many ran, how many passed, and the names still blank. It does not blend them into one float, and it does not pass or fail the product. If nobody else ran, Stackly itself is blank.

<h3><img src="assets/glossary/simplespeak.png" alt="Simplespeak" height="21"></h3>

Stackly is the cover sheet. It lists what was measured, what passed its own rule, and what was left blank. It refuses to turn that list into a single score.

<h3><img src="assets/glossary/techspeak.png" alt="Techspeak" height="21"></h3>

`ACCEPTS_PRIOR` is set, so Hydra passes the earlier cells in. `passed` stays empty on purpose. The headline of the report is the same vector: ran, passed, deferred.


<p><img src="assets/term-rule.png" alt="" width="100%" height="18"></p>

<a id="selfbelt" name="selfbelt"></a>
<h2><img src="assets/glossary/selfbelt.png" alt="SELFBELT" height="19"></h2>

SELFBELT is the seatbelt write-up for people who sit with software, including AI tools, for a long time. The pages are on [SELFBELT](docs/SELFBELT.md). The practice named inside the document is SELFBELTING. The button name and the page name are SELFBELT.

<h3><img src="assets/glossary/score-constitution.png" alt="Score constitution" height="17"></h3>

SELFBELT is not one of the sixteen evalers and it does not add a seventeenth score. Menschly is the evaler that can see a timer. The PDF is the explanation a developer can read and, if they choose, ship beside their own software.

<h3><img src="assets/glossary/simplespeak.png" alt="Simplespeak" height="21"></h3>

Think of the early car. Lights, signs, and laws showed up before the seatbelt. A lot of software today has the lights: filters, policies, usage caps written by the vendor. The belt is the habit the person puts on. SELFBELT is that write-up. FUSS is a belt you can clip into a product: a small panel that asks whether to time the sitting.

Ralph Nader's *Unsafe at Any Speed* (1965) pushed crash safety into the car instead of leaving it as optional chrome. The analogy stops there. SELFBELT is not a law, not a medical claim, and not a statement that one sitting harms a brain.

<h3><img src="assets/glossary/techspeak.png" alt="Techspeak" height="21"></h3>

Menschly links here. The drop-in timer is [fuss/README.md](fuss/README.md). Installing FUSS is optional. A product can pass Menschly with any real stop, and a product with no sitting stays blank. Nothing in the PDF is scraped into a numeric grade.


<p><img src="assets/term-rule.png" alt="" width="100%" height="18"></p>

<a id="agentic-exams-that-are-not-on-the-vector-yet" name="agentic-exams-that-are-not-on-the-vector-yet"></a>
<h2><img src="assets/glossary/agentic-exams-that-are-not-on-the-vector-yet.png" alt="Agentic exams that are not on the vector yet" height="26"></h2>

These are public exams for coding agents and for chat models. They matter in this period. Evalathan does not run them in the laptop scan, and it does not paste their leaderboards. That is a scope fact, not a dismissal. Trajectly is the station that will count one of them on the day a saved trace from that exam is in the folder you scan. A percent copied from a website is still not a grade.


<p><img src="assets/term-rule.png" alt="" width="100%" height="18"></p>

<a id="swe-bench" name="swe-bench"></a>
<h2><img src="assets/glossary/swe-bench.png" alt="SWE-bench" height="20"></h2>

<h3><img src="assets/glossary/score-constitution.png" alt="Score constitution" height="17"></h3>

No Evalathan score. The public board is someone else's number. The cell stays off the vector until a trace file from a run is in the tree.

<h3><img src="assets/glossary/simplespeak.png" alt="Simplespeak" height="21"></h3>

SWE-bench (Software Engineering Benchmark) is a set of real GitHub issues a coding agent is asked to patch. The full public set is large and is graded in containers. That does not fit a laptop scan of an ordinary folder. Evalathan can say the name. It does not pretend it sat the exam.

<h3><img src="assets/glossary/techspeak.png" alt="Techspeak" height="21"></h3>

The project site is [swebench.com](https://www.swebench.com/). A short public account is on [Wikipedia](https://en.wikipedia.org/wiki/SWE-bench). Trajectly would count a local file whose name contains `trace`, `trajectory`, or `passk`. It will not count a screenshot.


<p><img src="assets/term-rule.png" alt="" width="100%" height="18"></p>

<a id="swe-bench-pro" name="swe-bench-pro"></a>
<h2><img src="assets/glossary/swe-bench-pro.png" alt="SWE-bench Pro" height="20"></h2>

<h3><img src="assets/glossary/score-constitution.png" alt="Score constitution" height="17"></h3>

Same as SWE-bench. Not on the vector. The public slice is still a lab run.

<h3><img src="assets/glossary/simplespeak.png" alt="Simplespeak" height="21"></h3>

SWE-bench Pro is a harder, later set from the same family, with a public slice and private slices. It is the right ambition for a hosted exam on a machine that can run it. It is too much work for the current laptop scan, and a copied percent would not make Evalathan more true.

<h3><img src="assets/glossary/techspeak.png" alt="Techspeak" height="21"></h3>

The paper is [arXiv:2509.16941](https://arxiv.org/abs/2509.16941). Inclusion later means a frozen task folder, the grader that ships with it, and a trace Trajectly can count. It does not mean embedding the live leaderboard.


<p><img src="assets/term-rule.png" alt="" width="100%" height="18"></p>

<a id="deepswe" name="deepswe"></a>
<h2><img src="assets/glossary/deepswe.png" alt="DeepSWE" height="24"></h2>

<h3><img src="assets/glossary/score-constitution.png" alt="Score constitution" height="17"></h3>

Not on the vector. No trace, no cell.

<h3><img src="assets/glossary/simplespeak.png" alt="Simplespeak" height="21"></h3>

DeepSWE is a smaller public agent exam, on the order of a hundred handwritten tasks, at deepswe.datacurve.ai. Smaller does not make it a laptop feature. It joins the same menu as the SWE-bench family: host it when the grader and the trace are yours.

<h3><img src="assets/glossary/techspeak.png" alt="Techspeak" height="21"></h3>

The public page is [deepswe.datacurve.ai](https://deepswe.datacurve.ai/). Evalathan does not download that board and does not average it with anything else.


<p><img src="assets/term-rule.png" alt="" width="100%" height="18"></p>

<a id="aose" name="aose"></a>
<h2><img src="assets/glossary/aose.png" alt="AOSE" height="19"></h2>

<h3><img src="assets/glossary/score-constitution.png" alt="Score constitution" height="17"></h3>

AOSE is a field, not a score Evalathan prints.

<h3><img src="assets/glossary/simplespeak.png" alt="Simplespeak" height="21"></h3>

AOSE (agent-oriented software engineering) is the research tradition of building software as cooperating agents. The Wikipedia page also carries a mixed table of newer benchmarks. Those rows are a catalog. They are not sixteen more evalers, and they are not a grade of the folder you just scanned.

<h3><img src="assets/glossary/techspeak.png" alt="Techspeak" height="21"></h3>

The field overview is [Wikipedia: Agent-oriented software engineering](https://en.wikipedia.org/wiki/Agent-oriented_software_engineering). Names that show up in that public catalog, besides the SWE-bench family, include AgentBench, tau-bench, WebArena, WildBench, and Test of Time. Evalathan does not collapse that table into one number.


<p><img src="assets/term-rule.png" alt="" width="100%" height="18"></p>

<a id="wildbench" name="wildbench"></a>
<h2><img src="assets/glossary/wildbench.png" alt="WildBench" height="20"></h2>

<h3><img src="assets/glossary/score-constitution.png" alt="Score constitution" height="17"></h3>

Not on the vector. WildBench grades chat replies. It is not a trace of a coding agent unless you saved one.

<h3><img src="assets/glossary/simplespeak.png" alt="Simplespeak" height="21"></h3>

WildBench is a public benchmark of hard chat tasks drawn from real use. It is worth knowing about. Evalathan does not host it and does not quote its board. It would show up under Trajectly only if you saved a run in the folder.

<h3><img src="assets/glossary/techspeak.png" alt="Techspeak" height="21"></h3>

The paper is [arXiv:2406.04770](https://arxiv.org/abs/2406.04770). No leaderboard percent from that paper is copied into a cell.
