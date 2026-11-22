# Log

Append-only. One operation per entry. Prefix format: `## [YYYY-MM-DD] op | title`.

## [2026-11-20] ingest | MIT xPRO QCFx1 course capture

Initial vault. Five week files moved from the student's Google Doc export into `mit-raw/week1.md` … `mit-raw/week5.md`, with slide PNGs under `mit-raw/weekN/media/media/`.

- 288 slide frames transcribed. 153 of them carried a player clock and were inserted on the matching SRT cue (week 1: 59, week 2: 8, week 3: 27, week 4: 35, week 5: 24). Week 2 is mostly text-unit slides without a video clock, so those stay in the page rather than inside a transcript.
- Equation frames are display math. About 800 `$$` blocks across the five weeks. Diagrams and quizzes keep the image, with a text transcription under it. 11 non-teaching photos were dropped.
- Image embeds are vault-absolute `/mit-raw/weekN/media/media/...`. No `/workspace` paths remain.
- Wiki layer opened: source notes generated from each course page's Learn section, concept notes for Shor, period finding, Simon, QFT, Grover, adiabatic QC, annealing, BB84, E91, Bell, teleportation, Hamiltonian simulation, Trotter, phase estimation, and VQE.
- Schema: `AGENTS.md`.

## [2026-11-20] lint | open questions

- Week 2 headings do not all follow the week-1 "Page Title" pattern. Source notes depend on level-1 headings; confirm the week 2 list in `wiki/index.md` after the first Obsidian open.
- Some frames have no player chrome (text units, quiz slides). Those stay in the Images section of the page as LaTeX or as an image.
- Transcription of ~290 frames was automatic. Spot-check one equation per concept against the PNG before citing a formula in a new note.

## [2026-11-21] lint | first lint pass (Claude)

Run by Claude (Opus 5.5) on the vault at `fadbf85`. Checks: link resolution, orphans, unsourced claims, raw/official structure. Fixed in the wiki layer only. Raw files untouched.

**Fixed**
- `concepts/shors-algorithm.md`: removed a stray backtick line that commit `fadbf85` added under the frontmatter. Replaced the "if that source note exists" hedge with real links. Linked the Week 1 demonstration notes, which had been orphans.
- `concepts/period-finding.md`: register size corrected to the course's $N^2 \le 2^l \le 2N^2$ (the page said $2^q \ge 2r_{\max}$). Added the course's worked example $11^x \bmod 21$ ($l=9$, $r=6$), plus a caveat that $2^9/6$ is not an integer, so the course's final line is the idealized case.
- `concepts/quantum-fourier-transform.md`: added the missing Sources section. Gate counts restated as the lecture gives them: exact $\sim(\log c)^2$, approximate $\sim \log c \log\log c$.
- `concepts/bb84.md`: replaced the "filename may differ" hedge with links.
- 9 broken `[[...]]` links in week-2 source notes. These were pandoc `[[text]{.underline}](url)` spans that Obsidian treated as wikilinks to nonexistent pages, which put ghost nodes in the graph. They are now plain markdown links. The same spans are still in `mit-raw/week2.md` and `week3.md` (raw is immutable).

**Ingested** (four course pages the first build skipped because their `Page Title` was blank or level 2)
- `sources/week-3-01a-post-quantum-cryptography.md`, `week-3-01b-single-photon-sources-and-detectors.md`, `week-3-08a-quantum-repeaters.md`, `week-4-00-introduction-quantum-simulation.md`.

**Added**
- `analyses/course-map.md`: official QCFx2 weeks mapped to raw files and source notes in reading order.

**Conflicts (recorded, not resolved)**
- *Course identity.* `AGENTS.md`, `README.md` and the first log entry call this vault QCFx1 (*Introduction to Quantum Computing*). The capture is QCFx2 (*Quantum Algorithms for Cybersecurity, Chemistry, and Optimization*): raw week 2 says "Welcome to Course 2". The index title is now corrected. `AGENTS.md` and `README.md` are the human's and were left alone.
- *Week numbering.* 5 raw files vs. 4 official weeks. Official Week 1 = raw week 2 then raw week 1. Official weeks 2/3/4 = raw weeks 3/4/5. Source-note filenames keep the raw numbering; the course map translates.

**Open, not fixed**
- Dropped inline math in the Google-Doc export. Example: post-quantum page, Mosca's RSA-2048 odds read "constructed by and at and respectively", with the numbers missing. Similar gaps are in the RSA/Fermat text ("periodic in , then ..."). Do not fill these from memory. Re-capture the page or check on the platform.
- 33 of the original 47 source notes are stubs with no Learn prose (video-only pages). Three show `{width=...}` image residue where images were lost (`week-1-05`, `week-2-03`, `week-2-08`).
- `tools/build_wiki.py` hard-codes `ROOT = /workspace/mit-x-pro-wiki` and regenerates source notes. Re-running it would overwrite this pass's edits and drop the four new notes. Treat source notes as hand-maintained from now on, or make the tool merge instead of overwrite.
- Still unverified concept-page claims, background rather than course: BB84 "abort threshold / privacy amplification" detail, the teleportation correction order $X^{m_0}Z^{m_1}$, and the Kadowaki–Nishimori dissipation framing (the 1998 proposal itself is in raw week 5).

**Next:** supervised ingest of official Week 1 in course order. Start with `week2.md`: RSA → Shor → QFT. Then expand the stubs from the transcripts, one page at a time.

## [2026-11-21] query | are all quizzes captured?

Albert asked whether every quiz made it into the notes. I compared the official outline (2026-11-09 screenshot) and the five source Google Docs with `mit-raw/`, matching each `PRACTICE (n questions)` block and each "point(s) (graded)" frame. The result is filed as [quiz inventory](analyses/quiz-inventory.md): 52 of 57 outline questions are captured. Missing: Week 1 case-study Q2 (absent in the source doc screenshots), Week 3 Reflect and Review, Week 4 third adiabatic CYU, and the two annealing CYUs (the annealing page itself is not in the capture). Post-Assessment not captured yet. The source docs confirm that the 5 raw files are 4 official weeks: Week 1 was saved as two docs.

Also noted: `AGENTS.md` line 5 still says "QCFx1 (Introduction to Quantum Computing)"; the title line was fixed in `73cded6`. That is the human's file to change.

## [2026-11-22] ingest | concept: RSA cryptosystem

Albert asked why there is no RSA concept page. RSA gets a full lesson in official Week 1, a 4-point CYU and two of the five Week 1 quiz questions, and it is the reason Shor matters, so it gets a page. New `concepts/rsa-cryptosystem.md` is built from the Modern Cryptography and RSA pages of raw week 2. Formulas come from the slides, because the Learn prose lost its inline math. It includes a toy example ($N=33$, own numbers, deliberately not the graded $p=101, q=113, e=3533$) and a Shor run on $N=33$ showing both the success case ($g=5$) and the $g^{r/2}\equiv-1$ failure case ($g=2$). It also flags that the course uses $r$ for both the RSA totient and the Shor order.

Backlinks added from `shors-algorithm`, `period-finding` and source notes `week-2-04`, `-05`, `-06`. Indexed.

**Conflict (course-internal, recorded on the concept page):** the "Determining e and d" slide gives $3 \le e \le r$; the key-generation summary slide gives $3 \le e \le N-1$. Both require $\gcd(e, r)=1$.

## [2026-11-22] query + ingest | test question: Week 4 Quiz Q5 "Exactly-1 3-SAT Problem II"

Albert tested the vault against a live question. The screenshot matches `mit-raw/week5.md:5180` word for word (quiz inventory row: Week 4 quiz, Q5). The course covers all four statements in the "Introduction to Grover's Algorithm on the Quantum Experience" transcript and slide legend (~lines 3780–3840). The one gap: the course never defines **"satisfiable"** or CNF formally. It only uses "satisfies" and the truth table.

**Policy:** the repo is **public**, so graded-quiz answers are discussed in chat and *not* filed here. Filed instead: the knowledge needed to answer.

- Added external source `mit-raw/external/boolean-satisfiability.md`. Paraphrased definitions with links to Wikipedia, UIUC CS/ECE 374 and arXiv. Marked as not course material.
- New concept `concepts/exactly-1-3-sat.md`: vocabulary, 3-SAT vs. Exactly-1 3-SAT, the course instance and truth table, the oracle construction (XOR parity + CCCX built from 3 Toffolis), Grover iterations (2 → ≈95%, 3 → ≈32%). Backlinked from `grovers-algorithm` and source notes `week-5-05`, `-06`, `-08`. Indexed.
- Schema note: `mit-raw/external/` is a new folder for outside sources. AGENTS.md doesn't mention it yet (human's file).

## [2026-11-22] query + ingest | quiz → concept map (all 52 questions)

Albert asked for every quiz question in the course to link to the concept item(s) it tests, as precisely as Obsidian allows. Output: `analyses/quiz-concept-map.md`. Each of the 52 captured questions links to a raw location plus one to three **block references** (`[[concepts/x#^block]]`) that land on the exact paragraph. It also has a reverse index by concept. Rows for the 4 uncaptured items are kept. **No answers are filed** (the repo is public).

Building the map exposed gaps. I filled each from the raw capture, with locations cited:
- **New concept pages (9):** `modern-cryptography`, `shor-demonstrations`, `post-quantum-cryptography`, `photon-sources-and-detectors`, `photon-polarization-qubits`, `quantum-repeaters`, `quantum-simulation`, `quantum-chemistry`, `openqasm`.
- **Extended pages:** `bell-inequality` (local realism, three loopholes), `ekert91` (two parties, trusted source, no Bell measurement, CHSH $S=-2\sqrt2$), `quantum-fourier-transform` (binary-fraction product form, 2-qubit circuit), `adiabatic-quantum-computing` (definition/universality, minimum gap, Landau–Zener, thermal noise, Ising), `quantum-annealing`, `hamiltonian-simulation` (what a Hamiltonian is, particle in a box), `trotterization` (exact vs product, non-commuting rotations), `grovers-algorithm` (register size, two reflections, iteration bound), `bb84` (polarization sifting), `quantum-teleportation` (photonic protocol), `period-finding`, `phase-estimation`, `vqe`, `rsa-cryptosystem`, `exactly-1-3-sat`, `shors-algorithm`.
- Block IDs were added across these pages; all 95 block links validated. Source notes are backlinked to the new pages, and the index is updated.

**Honesty labels.** Three statements are background, not course content, and are marked inline: AQC as "analog" (the word appears only in a quiz option), Hamiltonians as the physical basis of gates, and the "what to do about a small gap" list (own reasoning). The polarizer Born-rule paragraph is also marked as standard background.

**Data gaps noted on pages:** Chuang's "Ideas and Issues" item 2 is not captured (`quantum-simulation`). Mosca's RSA-2048 odds lost their numbers (`post-quantum-cryptography`).

## [2026-11-22] lint | conflict: polarizer "registers" wording (entanglement questions)

While building Albert's Anki deck v2 (kept outside this public repo because it holds answers), three items came out ambiguous. Recorded so the wiki doesn't silently pick a side:
- **Entanglement questions** (pre-Q4, Week 2 CYU Entanglement I, Week 2 quiz Q2): the collapse reading and the strict optics reading select different options. Note added to `concepts/photon-polarization-qubits.md`.
- **Week 1 quiz Q4 (QFT III):** controlled-phase gates are symmetric, so two of the drawn circuits are the same unitary (checked numerically). The textbook drawing is the intended one. Already reflected in `concepts/quantum-fourier-transform.md`.
- **Week 4 quiz Q1 (Adiabatic Evolution):** whether "requires infinite coherence times" counts as a reason. The lecture says it "will work, for sure, if you go infinitely slowly… not a practical algorithm." Judgment call; see `concepts/adiabatic-quantum-computing.md#^minimum-gap`.

## [2026-11-22] query | test question: Week 4 Quiz Q4 "Grover Operator"

Matches `mit-raw/week5.md:5159` verbatim. Fully covered by the course: the quantum search transcript (~6:37–8:41) and the "Number of Iterations" slide (line 3317). No external source needed. Extended `concepts/grovers-algorithm.md#^iteration-bound` with the slide's exact R formula, the ceiling form of the bound, and the "CI" = ψ caption note. Answer kept out of the repo (it's in the private Anki deck v2).

## [2026-11-22] ingest | quiz layer: wiki/quizzes (markdown transcription + progress)

At Albert's request, every graded question is now available as clean markdown in a new layer, `wiki/quizzes/` (`index.md` + one page per section). `mit-raw/` stays immutable per the schema, so this is a cleaned transcription, not an edit of raw. Per question: the title, status, type, attempts, raw line, title-level concept links, the stem, the options as `- [ ] **A.** …` (letters added to match the Anki deck, not on eDX), and the original screenshot(s) in a folded `[!info]-` callout.
- **Status convention:** `✅ CHECKED in eDX` (progress only, no answer) / `⏳ pending` / `⚠️ not captured`. Currently 12/52 checked: the Pre-Assessment (9) plus Week 4 quiz Q3, Q4 and Q5.
- **Transcription fixes vs raw:** the VQE CYU stem was completed from its screenshot (raw cut short). The cow-rotation options were rebuilt from the four tile labels. Trotterization option C was restored in full. Stray figure-label math and `#` headings were dropped from stems. `\( \)` was converted to `$ $` for Obsidian.
- **Test question this session:** Week 4 quiz Q3 (Ising). Matches `mit-raw/week5.md:5119`. Covered by `concepts/adiabatic-quantum-computing#^ising`. The stem's sum $J\sum_{i\neq j}Z^iZ^{j+1}$ mixes indices; it means nearest neighbours.
- Schema note for the human: AGENTS.md doesn't list `wiki/quizzes/` yet.

## [2026-11-22] query + ingest | test question: Week 4 Quiz Q2 "Quantum Annealing III"

Matches `mit-raw/week5.md:5095` verbatim. Options A and C are stated in the AQC concept Learn text (Kadowaki–Nishimori: tunneling + relaxation; "no evidence" of enhancement). B is contradicted by the minimum-gap paragraph: a smaller gap requires slower evolution. D's "Ising" is never named by the course outside quiz stems, so I added the external source `mit-raw/external/quantum-annealing-ising.md` (arXiv:2001.00234, arXiv:2112.07491) and linked it from `concepts/quantum-annealing.md#^encoding-and-gap`. Status set to ✅ CHECKED in eDX in `quizzes/week-4.md` (now 13/52).

## [2026-11-22] query | test question: Week 4 Quiz Q1 "Adiabatic Evolution" + Week 4 review

Matches `mit-raw/week5.md:5076`. Options A and C are backed by the AQC concept Learn text: the thermal environment drives transitions once the gap is below $k_BT$; Landau–Zener for fast evolution. B is the plain false one. D ("infinite coherence times") is not addressed by the course; the nearest line is the expert view's "will work, for sure, if you go infinitely slowly… not a practical algorithm". Recorded as a judgment call (already noted in the 2026-11-22 conflict entry).

Week 4 quiz is now fully reviewed: Q1–Q5 ✅ CHECKED in eDX (14/52 overall). Clarified the status convention in `quizzes/index.md`: CHECKED = reviewed, **not** submitted. Albert is running an independent 3-way assessment (Albert, Claude, ChatGPT) before submitting. The answer sheets stay outside this public repo.

Open structural gap, top priority before submitting Week 4: the "Quantum Annealing & Polynomial-Speedup" page and its 2 CYUs, plus a 3rd adiabatic CYU, are not in the capture.

## [2026-11-22] ingest | external: adiabatic computation and finite coherence

Albert asked whether the AQC II stem ("coherence time is limited… close to the time set by the minimum gap") bears on the Adiabatic Evolution "infinite coherence" option. It does: the course models finite coherence as hard-but-workable, and the Learn text only ever requires a *sufficiently* slow, gap-limited runtime. Added `mit-raw/external/adiabatic-decoherence.md` (Childs–Farhi–Preskill 2001; Albash–Lidar 2015; Campos Venuti et al. 2016) and linked it from `concepts/adiabatic-quantum-computing.md#^minimum-gap`. This supersedes the "judgment call" framing in the earlier conflict entry: the course plus the literature now favour reading "requires infinite coherence" as an overstatement.
