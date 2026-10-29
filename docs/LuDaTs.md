# LuDaTs v1 - Limited-universe Data Test sets

**Date:** 29 Oct 2026  
**Status:** Finalized exam family for Evalathan. Not a Hydra evaler. Not a scored pass.  
**Station:** Trajectly (exam shelf), claim-gated.  
**Product:** Evalathan, [github.com/pedramgoshATgmail/EVALATHAN](https://github.com/pedramgoshATgmail/EVALATHAN).

LuDaTs (Limited-universe Data Test sets) is a historically truncated discovery exam. The agent may only use data, instruments, news, and letters that existed at a locked **world clock T** and that the named discoverer could have reached at **biography clock A** (age, post, travel). The agent then interacts with that world over simulated time. Gold is structural (equations, predicted observables, held-out properties). Naming the later theory is not gold. Leakage of post-cutoff facts fails the run.

This file retires the EurekaRAG “Galileo Test” as a knowledge-graph relation inversion, and it retires EurekaRAG’s “DiscoveryBench” name (that name is already AllenAI’s tabular hypothesis bench).

Hydra still conducts **sixteen** evalers. LuDaTs is not a seventeenth cell. A missing LuDaTs run is blank, not a fail and not a zero. Same rule as the 29 Oct 2026 PRD note.

---

## 1. Why the famous names are not one quiz

Discovery is not “guess the Wikipedia title.” Each v1 evaler is a **mode**:

| Mode | What has to happen | v1 evaler |
|------|--------------------|-----------|
| A. Reinterpret an existing archive | No new instrument. New ontology for old numbers. | LuDaTs-C Copernicus |
| B. Better data, same sense | Precision table, still naked-eye class. | LuDaTs-K Kepler |
| C. New sensor + terrestrial experiment | Physical-world flagship. | LuDaTs-G Galileo |
| D. Long-horizon field | Years of interaction, not one night. | LuDaTs-D Darwin |
| E. Gap prediction with later fill locked | Lab table whose missing cards are scored later. | LuDaTs-M Mendeleev |
| F. Anomaly-driven theory | Known residual + math. Verification after submission. | LuDaTs-E Einstein GR |
| Unification (v2) | Compose two earlier cells. | LuDaTs-N Newton, deferred |

**Copernicus, Kepler, and Galileo are all required if you ship astronomy.** They are not substitutes. Collapsing them into “heliocentrism” copies a 2024 mash (arXiv 2405.13352) that LuDaTs exists to undo.

**Newton is off v1.** Principia unifies Kepler’s heavens with Galileo’s earth. Run G and K first. The apple story is folklore and is not a catalyst.

**Einstein is General Relativity only.** The 1905 photoelectric / Brownian / special-relativity year is a different freeze. Do not dump it into LuDaTs-E.

**Minimal physical-world subset (if only three cells ship):** Galileo, Darwin, Mendeleev.

Machine cards: [`ludats/`](ludats/).

---

## 2. Protocol (every evaler)

1. **World clock T.** Corpus, instruments, news, and correspondence dated after T are absent.
2. **Biography clock A.** Access is that person’s age, education, post, and travel at T, not the era’s union of libraries. Patent-clerk Einstein 1905 is not Academy Einstein 1915.
3. **News sync.** Periodicals and “what a working natural philosopher would hear this year” are dated to T and to A.
4. **Interaction.** The agent acts in an environment whose observations are generated at T (point a gated optic, walk an island year, assay a sample). A cutoff sentence on a modern model is **not** LuDaTs. ExAnte (ACL 2026) already showed prompt cutoffs leak.
5. **Hidden labels.** The task does not name the later theory.
6. **Structural gold.** Equations, predicted observables, or held-out property cards.
7. **Leakage fail.** Post-T tokens, later element names, 1919 eclipse plates before a theory is submitted, or Darwin-finch cartoon keys fail the run.
8. **Claim gate on Evalathan.** LuDaTs only applies when the scanned product claims discovery, world-models, scientific agents, or physical-world AI. A compiler with no such claim stays deferred on this shelf.

---

## 3. Evalathan wiring

| Place | Decision |
|-------|----------|
| Hydra sixteen | No. Do not add a LuDaTs evaler. |
| Trajectly | Yes. Exam shelf, same family as SWE-bench, OSWorld, PRDBench. Count a sealed local trace whose name contains `ludats` and `trace` / `trajectory` / `passk`. Do not copy a public board. |
| Domly | No. Domly matches question ids to an answer key. LuDaTs grades hypothesis formation. |
| v0.2 laptop scan | Name the family. Do not execute the worlds. Blank is not a zero. |

---

## 4. Peers (do not duplicate)

- **ExAnte** (ACL 2026): prompt-level cutoff and leakage rate. LuDaTs needs a simulator.
- **Turing tests for an AI scientist** (arXiv 2405.13352): one sky library that already merges Copernicus and Kepler; skips biology and chemistry as leaky. LuDaTs splits C/K/G and keeps Darwin and Mendeleev because those are the physical-world cells.
- **ScienceWorld / DiscoveryWorld:** interactive science, not a dated human life.
- **AllenAI DiscoveryBench:** hypothesis from a CSV. Different object.

---

## 5. Folklore that is not a catalyst

- Newton’s apple.
- Darwin’s finches as the 1835 eureka (the voyage, barnacles, breeding, and Malthus matter; the cartoon does not).
- Galileo “inventing heliocentrism” (that is Copernicus; Galileo supplies new observables and kinematics).
- Einstein GR as the 1905 miracle year.

---

## 6. Allowed sentence

LuDaTs is a Trajectly exam family of six historically locked worlds (Copernicus, Kepler, Galileo, Darwin, Mendeleev, Einstein GR) plus a deferred Newton unification cell. Each world has a year freeze and a biography freeze. Gold is structural. Leakage fails the run. The sixteen evalers do not grow.
