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

Albert asked whether every quiz made it into the notes. I compared the official outline (2026-11-09 screenshot) and the five source Google Docs with `mit-raw/`, matching each `PRACTICE (n questions)` block and each "point(s) (graded)" frame. The result is filed as [quiz inventory](analyses/quiz-inventory.md): 51 of 56 outline questions are captured. Missing: Week 1 case-study Q2 (absent in the source doc screenshots), Week 3 Reflect and Review, Week 4 third adiabatic CYU, and the two annealing CYUs (the annealing page itself is not in the capture). Post-Assessment not captured yet. The source docs confirm that the 5 raw files are 4 official weeks: Week 1 was saved as two docs.

Also noted: `AGENTS.md` line 5 still says "QCFx1 (Introduction to Quantum Computing)"; the title line was fixed in `73cded6`. That is the human's file to change.
