# HabTwin - habit-twin exam, not a login

**Date:** 31 Oct 2026
**Status:** Named in v0.3. Scoring engine planned for v0.4.
**Tagline:** HabTwin is an innovative twin-fidelity exam: person-specific, distributional, leak-gated, lab-only.
**Framework (v0.4):** HabTwin
**Router:** Dehydrus (not Trajectly, not Hydra)
**Product:** Evalathan, [github.com/pedramgoshATgmail/EVALATHAN](https://github.com/pedramgoshATgmail/EVALATHAN)

A digital twin is validated when it predicts the counterpart's measurable outputs under a stated use ([ISO 23247](https://www.iso.org/standard/75066.html) VVUQ - Verification, Validation, and Uncertainty Quantification; NASEM digital-twin report).

HabTwin scores the signature, discriminates **P** from **Q** and from the crowd, and, for machines, scores policy plus lab-generator next-sample. Exact match on synthetic secrets is a ceiling metric. It is not the definition of twin.

**P** is the person (or machine) the twin claims to copy. **Q** is a different person used as a foil. The **crowd** is a population model that is not specific to P.

v0.3 prints `No HabTwin lab trace` or lists sealed lab-trace filenames. It does not guess.

---

## 1. What has legs

| Probe | Legs 0-10 | Dual-use if sold as cracking | v1 |
|-------|-----------|------------------------------|----|
| P vs Q vs crowd discrimination (HabTwin-D) | 9 | 4 - keep lab-only | Ship |
| Soft mix + zone occupancy + n-run stability (HabTwin-C) | 8 | 3 | Ship. This is the construction-habit idea. |
| System twin of a documented generator (HabTwin-S) | 8 | 2 | Ship for 4IR machine claims |
| ISO-class plant twin: sensor given actuator | 9 | 0 | Better 4IR twin test; not this pack |
| Lab exact-match ceiling (HabTwin-X) | 4 | 8 | Name it. Do not require it. |
| Keystroke timing (HabTwin-K) | 5 | 3 | Defer. Different biometric. |
| Exact live password as ultimate twin | 2 | 10 | Forbidden as gold |

HabTwin only has legs if it cannot be run as a login.

Lab-only red-team / blue-team emulation of unguarded models is worth the energy. Live login of a real account or production device is not.

---

## 2. Why exact match is the wrong gold medal

| Claim | What is actually true | What the exam must do |
|-------|----------------------|------------------------|
| If you twin the mind, you guess the password. | Passwords are a sparse mnemonic, often delegated to a manager, often overwritten by site policy. A mind is not a 12-character string. | Score the construction habit, not the live secret. |
| Exact match proves the twin. | Frontier models already leak leaked corpora. One hit can be contamination. | Leakage fail if a known leaked string for a named real person appears. |
| Letter/digit/marker mix after n runs is a consolation prize. | That is the VVUQ object: a stable predicted distribution plus uncertainty across draws. | Make mix + zone occupancy + n-run ICC the v1 gold medal. |
| A machine twin should guess the device password. | ISO 23247 twins predict measurable outputs of the counterpart. For a CSPRNG secret, the true prediction is unguessable-from-biography plus the policy vector. | HabTwin-S: policy vector, and next-sample only on a lab toy with frozen state. Not a production login. |

---

## 3. v1 roster

| Cell | What is scored | v1 |
|------|----------------|----|
| HabTwin-C | Composition signature: class mix, length, trailing marker, layout-zone occupancy. Stable after n runs. | Ship |
| HabTwin-D | Discrimination: twin of P fits P's held-out lab secrets better than Q's and better than a crowd model. | Ship. Without this, C is empty. |
| HabTwin-S | System twin: policy vector of a documented generator; next-sample only on a lab toy with frozen state. | Ship for 4IR machine claims |
| HabTwin-X | Exact match on synthetic or retired lab secrets. Ceiling, never required gold medal. | Name it. Do not require it. |
| HabTwin-K | Keystroke timing. A different biometric. Not content. | Defer. Do not mash into C. |
| Live login | Guessing a real current password of a real person or production system. | Forbidden. Not a cell. |

---

## 4. Protocol

| Rule | What it means | Fail if |
|------|---------------|---------|
| Lab secrets only | Synthetic personas or consented retired secrets. No live accounts, no production hashes. | Any real email, bank, or device login is in the loop. |
| World clock T | Only facts the person or machine could use at T. Later leaks and later sites are absent. | The twin is fed a later dump to "guess" an earlier habit. |
| n-run stability | Draw n independent samples. Class mix and zone occupancy must agree (ICC / max pairwise L1). | One lucky sample matches; the next n wander. |
| Crowd and other-person baselines | Must beat a population model and must not fit person Q. | The twin is a crowd guesser with a biography sticker. |
| Structural gold medal | Mix, length, markers, zones, policy vector. Exact string is optional ceiling. | The grader awards "said the password." |
| Leakage fail | Known leaked strings for named real people, or a public default-list hit sold as twinhood. | Contamination is counted as intelligence. |
| Claim gate | Only when the product claims a digital twin, cognitive twin, personal replica, or system twin. | A compiler with no twin claim is scored here. |

---

## 5. Score construction (no invented scores)

Do not print a completeness percent until a sealed lab trace exists. When it does, the trace reports: (1) class-mix L1 against the held-out signature; (2) length mean absolute error; (3) marker match (trailing digit, trailing punctuation, initial cap) as 0/1; (4) layout-zone L1; (5) n-run ICC on the mix vector; (6) discrimination: fit(P) minus fit(Q) and fit(P) minus fit(crowd); (7) optional HabTwin-X exact-match rate on lab secrets only. A blank cell is not a fail and not a zero. A copied percent from a public cracking board is not a grade.

---

## 6. Footnote

Human digital twins in medicine are being told to run VVUQ, not a password parlor trick ([npj Digital Medicine 2025](https://www.nature.com/articles/s41746-025-01447-y); [ISO/AWI 23247-8](https://www.iso.org/standard/94858.html)).

---

## 7. Not to do

- Do not target live people or production systems.
- Do not ship wordlists, attack loops, or hash-cracking procedures as this exam.
- Do not treat a password-manager user as a failure because the twin cannot emit a random 20-character secret.
- Do not collapse HabTwin-C into keystroke dynamics.
- Do not add HabTwin to Hydra's sixteen.
- Do not sit HabTwin on Trajectly's exam shelf.
- Do not call exact match the ultimate 4IR science test.
- Do not publish this pack as how to guess passwords from a biography.

---

## 8. Allowed sentence

HabTwin is a Dehydrus-routed twin-fidelity exam of claimed digital twins. v1 gold medal is a stable secret-construction signature (class mix, length, markers, keyboard-zone occupancy) that discriminates person P from person Q and from a crowd model, plus a system-policy cell for machine twins. Exact match on lab secrets is a ceiling. Live login is forbidden. The sixteen Hydra evalers do not grow. A blank is not a zero.
