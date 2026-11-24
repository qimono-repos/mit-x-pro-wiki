---
title: "Kandala et al. 2017: hardware-efficient VQE for small molecules and quantum magnets"
type: paper
aliases: [Kandala 2017, IBM VQE 2017, BeH2 VQE, hardware-efficient ansatz]
citation: "A. Kandala, A. Mezzacapo, K. Temme, M. Takita, M. Brink, J. M. Chow, J. M. Gambetta (IBM), Nature 549, 242–246 (2017)"
arxiv: "1704.05018"
local_pdf: "mit-raw/external/papers/kandala-2017-hardware-efficient-vqe-arxiv-1704.05018.pdf"
assigned_by: "[[sources/week-4-08-reflect-and-review]]"
---

# Kandala et al. 2017: hardware-efficient VQE (IBM)

**Local PDF:** [[mit-raw/external/papers/kandala-2017-hardware-efficient-vqe-arxiv-1704.05018.pdf|open the paper]] · arXiv [1704.05018](https://arxiv.org/abs/1704.05018) · compared in [[analyses/reflect-rev-draft-002]]

## In two sentences
VQE with trial states built from the chip's **native** entangling interactions ("hardware-efficient" ansatz) on up to 6 superconducting qubits, with Hamiltonians of 100+ Pauli terms. Molecules up to BeH₂, plus a 4-qubit quantum magnet, with results matching a model of the device's noise.

## Where to look in the PDF
| What | Page |
|---|---|
| Abstract: 6 qubits, 100+ Pauli terms, BeH₂ | [[mit-raw/external/papers/kandala-2017-hardware-efficient-vqe-arxiv-1704.05018.pdf#page=1\|p.1]] |
| Fig. 1, hardware and software schematic of VQE (the hybrid loop) | [[mit-raw/external/papers/kandala-2017-hardware-efficient-vqe-arxiv-1704.05018.pdf#page=2\|p.2]] |
| Fig. 3, potential-energy surfaces H₂ / LiH / BeH₂ vs exact | [[mit-raw/external/papers/kandala-2017-hardware-efficient-vqe-arxiv-1704.05018.pdf#page=4\|p.4]] |
| Fig. 4, application to **quantum magnetism**, a 4-qubit Heisenberg/Ising-type model | [[mit-raw/external/papers/kandala-2017-hardware-efficient-vqe-arxiv-1704.05018.pdf#page=5\|p.5]] |

## How it connects to our wiki
- **VQE's classical optimizer.** Fig. 1 *is* our [[concepts/vqe#^hybrid-loop]] and the answer to [[quizzes/week-3#Q1: Variational Quantum Eigensolver]] (parameter optimization runs classically).
- **The Hamiltonian as a sum of Pauli terms**, the input format for both VQE and Trotterization: [[concepts/hamiltonian-simulation#^what-is-a-hamiltonian]], [[concepts/trotterization#^many-terms]].
- **Chemistry:** [[concepts/quantum-chemistry#^molecular-hamiltonian]], [[concepts/quantum-chemistry#^known-but-unsolved]].
- **Its quantum-magnet example (Fig. 4) is the bridge to the chosen paper:** the same family of models as [[papers/zhang-2017-53-ion-dynamical-phase-transition]], approached *digitally* (gates + VQE) instead of *analog* (quench).
- **IBM then and now:** the authors include Jerry Chow and Jay Gambetta, who in 2026 present IBM's QDC/Think roadmap. See [[analyses/reflect-rev-draft-002]] §4.
