---
title: "O'Malley et al. 2016: scalable quantum simulation of molecular energies (H₂)"
type: paper
aliases: [O'Malley 2016, Google H2, Babbush H2, Martinis H2]
citation: "P. J. J. O'Malley et al. (Google / UCSB), Phys. Rev. X 6, 031007 (2016)"
arxiv: "1512.06860"
local_pdf: "mit-raw/external/papers/omalley-2016-h2-molecular-energies-arxiv-1512.06860.pdf"
assigned_by: "[[sources/week-4-08-reflect-and-review]]"
---

# O'Malley et al. 2016: H₂ on superconducting qubits

**Local PDF:** [[mit-raw/external/papers/omalley-2016-h2-molecular-energies-arxiv-1512.06860.pdf|open the paper]] · arXiv [1512.06860](https://arxiv.org/abs/1512.06860) · compared in [[analyses/reflect-rev-draft-002]]

## In two sentences
The first electronic-structure calculation on a programmable superconducting processor without exponentially costly precompilation: the H₂ bond-dissociation curve computed **two ways**, VQE with unitary coupled cluster and Trotterized phase estimation. VQE reached chemical accuracy and turned out more robust to certain errors.

## Where to look in the PDF
| What | Page |
|---|---|
| Abstract: VQE vs phase estimation, "chemical accuracy" | [[mit-raw/external/papers/omalley-2016-h2-molecular-energies-arxiv-1512.06860.pdf#page=1\|p.1]] |
| Fig. 1, the H₂ circuits | [[mit-raw/external/papers/omalley-2016-h2-molecular-energies-arxiv-1512.06860.pdf#page=2\|p.2]] |
| Fig. 3, the VQE energy curve vs exact; chemical accuracy | [[mit-raw/external/papers/omalley-2016-h2-molecular-energies-arxiv-1512.06860.pdf#page=4\|p.4]] |
| Fig. 4, the phase-estimation results | [[mit-raw/external/papers/omalley-2016-h2-molecular-energies-arxiv-1512.06860.pdf#page=5\|p.5]] |

## How it connects to our wiki
- **The two algorithms we studied in Week 3**, side by side: [[concepts/vqe#^hybrid-loop|VQE's hybrid loop]] vs [[concepts/phase-estimation|phase estimation]], whose precision limit is in [[concepts/phase-estimation#^precision]] and whose Qiskit demo is [[concepts/phase-estimation#^qiskit-demo]].
- **Trotterization in practice.** The phase-estimation run uses a Trotterized e^{-iHt}: [[concepts/trotterization#^trotter-formula]], [[concepts/trotterization#^exact-vs-product]] and the course's BCH sign slip [[concepts/trotterization#^bch-sign]].
- **The molecular Hamiltonian** it starts from: [[concepts/quantum-chemistry#^molecular-hamiltonian]] (5 terms, V_ne).
- **Graded questions it illuminates:** [[quizzes/week-3#Q1: Variational Quantum Eigensolver]], [[quizzes/week-3#Q1: Phase Estimation Algorithm]], [[quizzes/week-3#Q1: Trotterization]], [[quizzes/week-3#Q1: Simulation of Chemistry Problems]].
- **Course pages:** [[sources/week-4-05-phase-estimation]], [[sources/week-4-06-variational-quantum-eigensolver]], [[sources/week-4-07-vqe-in-practice]].
- **Circuit:** [phase estimation, generated with Qiskit](/wiki/media/circuits/phase-estimation.svg).
