# Circuit diagrams

Qiskit scripts that draw the wiki's quantum circuits and check them by simulation.

| Script | Outputs in `wiki/media/circuits/` | Embedded in |
|---|---|---|
| `phase_estimation.py` | `phase-estimation.svg/.txt` | [[concepts/phase-estimation]] |
| `circuits.py` | `qft-3`, `grover-3q`, `bb84-4-rounds`, `teleportation`, `shor-order-finding-15` (`.svg` + `.txt`) | QFT, Grover, BB84, teleportation, Shor concept pages |

Run from the repo root, e.g. `python3 tools/circuits/circuits.py` (needs `qiskit`, `matplotlib`, `pylatexenc`). Each run rewrites the outputs and prints the simulation checks.

Why both formats: the SVG is the rendered diagram Obsidian shows inline. The `.txt` (Qiskit's text drawer) is pasted into a `text` code block on the page, so the circuit is readable in any viewer, searchable, and diffs cleanly in git. Outputs are committed, so reading the vault never needs Python.

Conventions: Qiskit is little-endian ($q_0$ = least significant bit, rightmost in printed bitstrings). Pages say so where it matters.
