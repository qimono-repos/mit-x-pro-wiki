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

## [2026-11-22] ingest | hints for math-based quiz questions

Added a folded `> [!tip]- 💡 Hint` callout to 30 math or derivation questions in `wiki/quizzes/` (RSA, QFT, period finding, BB84 sifting, polarization and Malus' law, half-wave plate matrix, fiber dB loss, SPDC conservation laws, particle in a box, molecular Hamiltonian, Trotter and BCH, rotations, phase estimation, adiabatic condition $T \gg 1/\Delta_{min}^2$, Grover register and reflections, Exactly-1 3-SAT literal evaluation, Ising energies). Hints point at the method or first step, never the answer. The full worked developments (wrong path marked `← ✗`, then the right path) live only in the private Anki deck.

## [2026-11-22] update | Week 4 practice: 3-SAT I graded 1/1, Grover's Algorithm checked
Exactly-1 3-SAT Problem I graded 1/1 (3rd graded practice, after N=512 and Syntax Error). Grover's Algorithm CYU captured and checked against raw week 5 (lines 3194–3198, 4945: oracle = first reflection about $|\alpha\rangle$, $W$ = second reflection about $|\psi\rangle$). The eDX explanations revealed after grading go into the private Anki deck only. 18 / 52 checked.

## [2026-11-22] update | Grover's Algorithm graded; Quantum Annealing II captured from screenshot; Grover angle convention fixed
- Grover's Algorithm CYU graded 1/1 (4 of 4 practice questions graded so far).
- Quantum Annealing II (CYU on the "Quantum Annealing: Expert View" page) was never in the raw capture. Transcribed from Albert's eDX screenshot into `wiki/quizzes/week-4.md`, with the screenshot in `wiki/quizzes/media/`. `mit-raw/` left untouched; that page still needs a proper capture (prose + SRT). The outline's other annealing CYU (I) and the 3rd adiabatic CYU are still missing. 19 / 53 checked.
- Lint fix on [[concepts/grovers-algorithm]]: the page mixed two angle conventions (sin θ = 1/√N with a 2θ step, then the course's CI(arccos√(M/N)/θ)). Rewritten in the course's convention (raw week 5, "Geometric Interpretation"): |ψ⟩ = cos(θ/2)|α⟩ + sin(θ/2)|β⟩, each iterate rotates by θ.
- Conflict noted: the course's graded explanations count Grover's register differently: n qubits in one, n + 1 (index + oracle ancilla) in another. Not a real contradiction; the concept page already says "n index qubits plus the oracle's ancilla".

## [2026-11-22] ingest | Two missing Week 4 annealing transcripts
- New raw files (the pages were missing from `week5.md`; transcripts downloaded by Albert, verbatim SRT):
  - `mit-raw/week5-quantum-annealing.md`: the Quantum Annealing lecture (Gabriel Samach), Q2W4V4.
  - `mit-raw/week5-quantum-annealing-expert-view.md`: the classroom D-Wave talk, Q2W4V5 (lecturer identified by Albert as Peter Shor). This is the page with CYU Quantum Annealing II.
- Source notes `week-5-03a`, `week-5-03b`; index and course map updated.
- [[concepts/quantum-annealing]] rewritten from the course itself. New blocks `^thermal-excitation` (thermal photons vs gap, 10 mK vs 5 GHz ≈ 250 mK), `^protocol`, `^dwave`. "Ising" is now course-sourced (lecture ~7:14), so the external source is supporting detail rather than the only basis.
- [[concepts/adiabatic-quantum-computing]]: "analog" is now course-sourced (was flagged *Background*); added `^local-schedule` (slow down only at the avoided crossing; adiabatic Grover's gap ~1/√N).
- Quiz impact: Quantum Annealing III and Adiabatic Evolution are now backed almost verbatim by the lecture. Quantum Annealing II graded 1/1. Still missing: the annealing lecture page's own CYU (likely Annealing I), its Learn prose, and the 3rd adiabatic CYU.

## [2026-11-22] ingest | Learn text for the Quantum Annealing page (screenshot)
The page's Learn text, "Introduction to Quantum Annealing (QA)", was missing. It is now stored as Albert's screenshot in `mit-raw/week5/media/annealing/` and embedded in `mit-raw/week5-quantum-annealing.md` with a short text description. It is not retyped verbatim: an attempt to transcribe it word for word was blocked by a content filter on reproducing long copyrighted text, so the wiki carries summaries in my words. [[concepts/quantum-annealing]] gains `^simulated-annealing`, `^quantum-fluctuations`, the $A(t)/B(t)$ schedule, and `^dwave-hardware` (2000+ qubits, chimera graph, ZZ-only, low coherence).

## [2026-11-22] update | Quantum Annealing I captured from screenshot
CYU Quantum Annealing I (on the Quantum Annealing lecture page) transcribed into `wiki/quizzes/week-4.md` with its screenshot and a hint; concept map updated. Both annealing CYUs are now in. Week 4 is missing only the 3rd adiabatic CYU. 20 / 54 checked.

## [2026-11-22] ingest | QAOA video (Farhi), Q2W4V3
- New raw file `mit-raw/week5-qaoa.md`: Eddie Farhi's QAOA video, verbatim SRT. It was missing from `week5.md`, which mentions QAOA only in the intro (line 32). The eDX page title and Learn prose are not captured, and the position in the course map is a guess (video number 3, so after the adiabatic concept video).
- New concept [[concepts/qaoa]] (blocks `^problem`, `^circuit`, `^depth`, `^track-record`) and source note `week-5-02a`; index, course map and the AQC page link to it. Lines marked *Background* (2β Bloch-sphere convention, Trotter/VQE analogy) are not course content.
- Quantum Annealing I graded 1/1 (6 of 6 Week 4 practice questions graded correct).

## [2026-11-22] update | QAOA page title + its CYU captured
Albert confirmed the page title, "Quantum Approximate Optimization Algorithm"; raw header and source note renamed (file names unchanged). Its CYU was transcribed from his screenshot into `wiki/quizzes/week-4.md` with a hint; concept map updated. Possible tension, noted on the card: one option generalizes "better than random on every instance", which Farhi states for restricted MAX-CUT. 21 / 55 checked.

## [2026-11-22] update | QAOA CYU graded 1/1
QAOA CYU graded 1/1 (7 of 7 Week 4 practice questions). The graded result settles the risky option: the course treats "always better than random" as true, although the lecture proves it for restricted MAX-CUT. [[concepts/qaoa]]: E3LIN2 spelled out as Max-E3LIN2 (background gloss: 3-variable linear equations mod 2).

## [2026-11-22] update | AQC II graded 1/1; 8 of 8 Week 4 practice
AQC II graded 1/1. [[concepts/adiabatic-quantum-computing]] `^gap-strategies`: added why pure decay fails (it gets stuck in a local minimum), linked to simulated annealing. Pattern across the graded explanations: they justify only the options to be marked, and say nothing about the rest.

## [2026-11-22] update | Week 4 practice complete: 9 of 9 graded correct
AQC I graded 1/1. All Week 4 practice questions are now graded: N=512, Syntax Error, 3-SAT I, Grover's Algorithm, Quantum Annealing I and II, QAOA, AQC I, AQC II. Next: the one-attempt Quantum Optimization Quiz (5 questions).

## [2026-11-22] update | First one-shot Week 4 quiz answer graded: Ising Model 1/1
Quantum Optimization Quiz Q3 (Ising Model) submitted and graded 1/1. Background note added to [[concepts/adiabatic-quantum-computing]]: the two degenerate Néel states and the global spin-flip symmetry ∏X.

## [2026-11-22] update | Week 3 quiz Q4 (Evolution of a State) graded 1/1
The course's solution matches [[concepts/trotterization#^exact-vs-product]], including the $n \to \infty$ limit. It writes the Trotter product without $\hbar$ (implicitly $\hbar = 1$), as our page does.

## [2026-11-22] update | Week 3 quiz Q3 (Non-Commuting Terms) graded 1/1
The course's solution states that rotations about different axes don't commute. Small slip in its wording: it describes the reversed order as "45° about x, then 90° about y", but the figure captions (and the logic) swap the order of the same two rotations: 45° about y, then 90° about x.

## [2026-11-22] update | Week 3 quiz Q2 graded 1/1; how the course writes its explanations
Ideas and Issues of Quantum Simulation graded 1/1. Pattern across all 13 graded explanations seen today: an explanation only addresses the *false* statements (why a distractor is wrong, or why a "not valid" option is not valid). The true statements are never commented on, and a question whose options are all true shows no explanation at all. Corollary: an explanation is not a paraphrase of the right answer, and its examples can come from the author's own head (see the Non-Commuting Terms slip).

## [2026-11-22] ingest | External: DMRG for Dummies (course-recommended reading); Week 3 one-shot quiz complete
- Week 3 quiz Q1 (Quantum-Inspired Approximations) graded 1/1, completing the Week 3 one-shot quiz (4 of 4 graded correct; with Week 4 Q3, 5 of 5 one-shot answers correct so far).
- Its explanation links De Chiara et al., *DMRG for Dummies* (arXiv cond-mat/0603842). Added as `mit-raw/external/dmrg-for-dummies.md` (summary, not the PDF). [[concepts/quantum-simulation]] `^quantum-inspired` now records the history (Wilson's NRG → White's DMRG, 1992), 1D vs 2D (area law), and t-DMRG's Trotter link. This resolves the lecture's loose "Ken Wilson" attribution without contradicting it.
- [[concepts/adiabatic-quantum-computing]]: background note that the Sipser in Farhi–Goldstone–Gutmann–Sipser (2000) is MIT's Michael Sipser (theory of computation).

## [2026-11-22] update | Week 3 VQE CYU graded 1/1; refinement of the explanation pattern
VQE CYU graded 1/1 with no explanation shown, although three options are false. So a missing explanation does not prove that every option was true: some questions simply have none (this one repeats a pre-assessment item). The earlier rule, "explanations address only the false statements", still holds whenever an explanation does appear.

## [2026-11-22] update | Phase estimation: reconstructed derivation + first Qiskit-generated circuit diagram
- [[concepts/phase-estimation]] `^derivation`: the inverse-QFT step whose left-hand side is broken on the eDX page itself (and recorded as unreadable in raw week 4) is reconstructed in LaTeX and marked as my derivation.
- New convention for circuit diagrams: generator scripts in `tools/circuits/`, outputs committed to `wiki/media/circuits/` as SVG (rendered) plus `.txt` (Qiskit text drawer, embedded in a `text` code block). First one: `phase_estimation.py`, which also simulates exact vs inexact phases (`^qiskit-demo`).
- Week 3 CYU Phase Estimation Algorithm checked.

## [2026-11-22] update | Week 3 Phase Estimation CYU graded 1/1; notation conflict recorded
Conflict noted on [[concepts/phase-estimation]] `^notation`: the course uses $u$ both for the eigenvector $|u\rangle$ (circuit, derivation) and for the eigenvalue $u = e^{i2\pi\theta}$ (graded feedback), and writes the phase as both $\phi$ and $\theta$.

## [2026-11-22] update | Qiskit circuits for QFT, Grover, BB84, teleportation, Shor
Added `tools/circuits/circuits.py` (+ README) generating SVG + text diagrams, each verified by simulation, and embedded them as `^circuit-qiskit` sections:
- [[concepts/quantum-fourier-transform]]: 3-qubit QFT gate by gate; equals `QFTGate(3)` as an operator.
- [[concepts/grovers-algorithm]]: N = 8, marked |101⟩. P = 0.781 / 0.945 / 0.330 after 1 / 2 / 3 iterations, matching sin²((2R+1)θ/2).
- [[concepts/bb84]]: four rounds; matching bases are deterministic, mismatched ones 50/50.
- [[concepts/quantum-teleportation]]: dynamic circuit with classically controlled X/Z; fidelity 1.000000 (deferred-measurement check).
- [[concepts/shors-algorithm]]: order finding for N = 15, a = 7, readouts 0, 4, 8, 12 → r = 4 → factors 3, 5.

## [2026-11-22] update | Week 3 chemistry CYU graded 1/1; V_nc vs V_ne
Graded 1/1. Its feedback writes the molecular Hamiltonian with $V_{ne}$, matching Chuang's board; the pre-assessment's $V_{nc}$ is the same nucleus–electron term. [[concepts/quantum-chemistry]] `^molecular-hamiltonian` now uses $V_{ne}$ and records the conflict.

## [2026-11-22] lint | Course BCH formula has a sign error
Raw week 4 (~line 3146) gives $e^{A+B}=e^Ae^Be^{+\frac12[A,B]}$. The correct second-order factor is $e^{-\frac12[A,B]}$ (Zassenhaus), and it is exact only when $[A,B]$ commutes with $A$ and $B$. Verified numerically. Recorded on [[concepts/trotterization]] `^bch-sign`, along with `^many-terms` (the Lie product formula covers $\sum_n H_n$). Week 3 Trotterization CYU checked.

## [2026-11-22] status | End of day: official Weeks 3 and 4 practice complete; eDX at 42%
- eDX weighted grade 42% (pass 60%, due Dec 14, 2026). Official Week 3: every CYU and the quiz graded full marks (4/4). Official Week 4: all practice 9/9, quiz 1/5 submitted (Q3).
- **Gap with the biggest weight:** Week 3 "Reflect and Review Activity" (Reflect/Review bucket = 10% of the grade) is still not captured in `mit-raw/`.
- Remaining capture/review: official Week 2 (raw week3) and Week 1 (raw week1 + week2), the Week 1 case study, the post-assessment.
- The private Anki build kit (answers) is kept outside this repo.

## [2026-11-22] update | CLAUDE.md added (at Albert's request)
`CLAUDE.md` points Claude Code to AGENTS.md and documents what AGENTS.md doesn't yet cover: the folders added since (`mit-raw/external/`, `wiki/quizzes/`, `wiki/media/circuits/`, `tools/circuits/`), raw-vs-official week numbering, the no-answers rule for this public repo, the 5-point drill, and the raw-string LaTeX gotcha. Week 2 quiz reviewed (answers saved on eDX, not submitted); Week 2 CYU Entanglement I (3 attempts) is the planned tie-breaker for quiz Q2.

## [2026-11-22] update | Week 2 quiz: 3 of 4 graded full marks; eDX at 54%
BB84 Protocol II, Quantum Teleportation and Half-Wave Plate submitted and graded 1/1. Quantum Entanglement II is saved but not submitted, pending the tie-breaker (CYU Quantum Entanglement I, 3 attempts). eDX weighted grade: 54% (pass 60%). Quantum Repeaters CYU checked; its fiber-loss option matches the Learn text (raw week3 ~l.11095).

## [2026-11-22] update | Teleportation: photon labels differ across course sources; metaphor; derivation verified
[[concepts/quantum-teleportation]] gains `^labels` (input photon is C in the Learn text and quiz figure, A in the lecture, 1 in the pre-assessment), `^metaphor` (Remus and Romulus), and `^derivation-check` (the Learn page's Bell-basis regrouping verified numerically). The Quantum Repeaters CYU was graded full marks.

## [2026-11-22] update | Collapse-vs-polarizer conflict resolved; Week 4 quiz: 3 of 5 graded
- [[concepts/photon-polarization-qubits]] `^collapse-vs-polarizer`: the course's feedback on the Entanglement CYU (graded on the 2nd attempt) uses the polarizer rule: Bob's photon leaves a +45° polarizer as $|D\rangle$, and an H/V detector after it reads 50/50. The pre-assessment's collapse-only wording has no detector stage, so the two don't conflict. Added a note on the course's four names for the diagonal states. Also fixed an unsupported `psmallmatrix` in the half-wave-plate line.
- Learned about grading: edX gives partial credit on select-all questions (0.5) and shows no explanation for partial answers.
- Week 4 quiz: Q2 and Q5 submitted, graded full marks (with Q3, 3 of 5 done).

## [2026-11-22] status | PASSING: eDX at 64%
Week 4 quiz Q4 graded full marks (4 of 5; Q1 pending), Week 2 quiz 3 of 4 (Q2 pending). eDX weighted grade 64% ("You're currently passing this course"). Still at 0: Reflect/Review (10%), Case Study (5%), Post-Assessment (5%), plus the official Week 1 and Week 2 CYUs.

## [2026-11-22] ingest | Week 3 Reflect & Review Activity captured (screenshot + summary) and its three papers
- `mit-raw/week4-reflect-review.md` (screenshot + description) and source note `week-4-08-reflect-and-review`. This closes the biggest capture gap: the Reflect/Review bucket is 10% of the grade.
- `mit-raw/external/reflect-review-papers.md`: own-words summaries of Zhang 2017 (53 ions), O'Malley 2016 (H₂, Google/UCSB) and Kandala 2017 (BeH₂, IBM), linked to the VQE, phase estimation, Trotterization and quantum simulation concepts.
- Requirement noted: the journal box takes 150–300 words. Albert's ~3,200-word draft is working notes, condensed privately.

## [2026-11-23] analysis | Reflect & Review draft 002 (brainstorm)
New `wiki/analyses/reflect-rev-draft-002.md`: answers to the three prompts on Zhang et al. 2017, with sources checked on 2026-11-23. Findings: the paper shared Nature 551 with Lukin's 51-atom simulator and came three weeks after IBM's 50-qubit press release; its descendants are in Nature 2026 (Haghshenas et al. digital quantum magnetism; Helios 98-qubit all-to-all); 2026 listings (IONQ, QBTS, INFQ on NYSE; QNT, RGTI on Nasdaq); IBM QDC 2026 roadmap (Nighthawk r3, Starling 2029, Blue Jay 2033+); the AI-assisted Riemann Hypothesis claim (20 Nov 2026, unconfirmed) and why it doesn't break RSA. Items marked [to verify] aren't publishable yet; the IBM YouTube video couldn't be fetched.

## [2026-11-23] update | Papers layer + draft 002 wired into the wiki graph
- New `wiki/papers/`: one note per Reflect & Review paper, each with a page-by-page guide pointing to the local PDF (`#page=N`) and links into concepts, quizzes and course pages. New finding: Zhang 2017's Fig. 2 discusses the Ising model's Z₂ spin-flip symmetry, the same symmetry as `^ising` on the AQC page and the graded Week 4 Ising question.
- PDFs are in `mit-raw/external/papers/`, **gitignored** (arXiv default license; no open license shown), with a README of download links. Obsidian links work locally.
- [[analyses/reflect-rev-draft-002]]: paper links now point to the local notes and PDFs; each section has a "🔗 Wiki connections" callout (65 wikilinks, all validated). Backlinks ("Research papers") added on 8 concept pages. Index has a Papers section, and CLAUDE.md documents the new folders.

## [2026-11-24] query | Extend Reflect & Review draft 002 and correct course identity

Extended [[analyses/reflect-rev-draft-002]] in place with Albert's XYZ impact framework, sourced 2017–2026 hardware comparisons, nitrogenase and fertilizer economics, classical FeMoco challenge, capital and hiring evidence, and illustrative staged funding/Qimono consultancy. Distinguishes released systems from roadmap, physical from logical metrics, financing from revenue, and personal observation from verified hiring trend. Updated index and corrected QCFx2 course title in root schema/README at Albert's request; preserved historical log and authentic Course 1 references in course material. No quiz answers or raw changes. Media ranking, historical vacancy trend and full FeMoco paper review remain open.

## [2026-11-24] query | XYZ normalization and Qimono venture sprint

Added three benchmark anchors to reflection; linked FeMoco journal and preprint analysis, alternative $250k pilot budgets, four proposed roles, ISO readiness, Gantt, pitch and seven-slide Markdown deck. Store QR codes pending real listings; no hires, funding or subscriptions confirmed. Public repository contains proposal only, no private learner identities.

## [2026-11-24] query | Bloch impact visualization and live delivery model

Added Bloch-inspired raw/unit geometry, expanded founder stack and PROXORA packaging evidence, revised alternative budgets to $275k with $25k conditional SpinQ acquisition, retained Mermaid baseline and added twelve-sprint live delivery model. No live project, equipment purchase or email sent; user-reported $19k quote unverified. Confidential evidence must remain private.
