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
