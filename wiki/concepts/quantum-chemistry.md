---
title: Quantum chemistry simulation
type: concept
aliases: [chemistry simulation, molecular Hamiltonian, Haber-Bosch, nitrogenase]
---

# Quantum chemistry simulation

Chemistry is the flagship application of [[concepts/quantum-simulation]]. The molecular Hamiltonian is known exactly, but solving it for many interacting electrons and nuclei is classically intractable, so we often can't predict what a reaction or catalyst will do.

## The molecular Hamiltonian

$$
H = T_{nuc} + T_{elec} + V_{nn} + V_{ne} + V_{ee}
$$

Here $T$ are the kinetic energies of nuclei and electrons, and the $V$ terms are the Coulomb interactions nucleus–nucleus, nucleus–electron and electron–electron. An exact treatment needs *all* the interaction terms, not just the kinetic ones (raw week 4, Chuang's board ~8:08–8:27, line ~4929; raw week 2, pre-assessment Q7, eq. 9). **Notation conflict:** the pre-assessment writes the nucleus–electron term as $V_{nc}$; the lecture board and the Week 3 graded feedback write $V_{ne}$. Same term, and $V_{ne}$ is the consistent spelling. ^molecular-hamiltonian

## Known Hamiltonian, unknown answer

"Although the Hamiltonian that describes a chemical reaction might be well known, we do not necessarily know how to solve it, or if it can be solved at all." This sentence appears among the course's own quiz options and matches the lecture's framing. ^known-but-unsolved

**The motivating example.** The Haber–Bosch process makes ammonia ($N_2 + 3H_2 \to 2NH_3$) with metal catalysts at about 450 °C and high pressure (the Learn note corrects the lecture's "200 MPa" to 200 atm ≈ 20 MPa). Nature does the same with the **nitrogenase** enzyme in bacteria *at room temperature and pressure*, "in a remarkably different way, which we do not understand today." The point of simulation is to understand such low-energy routes, *not* to find how to raise the temperature ([raw week 4](/mit-raw/week4.md), chemistry transcript ~2:52–4:31). ^haber-bosch-nitrogenase

## How the course reads out energies

Two pathways: [[concepts/phase-estimation]] (deep circuits, precise eigenvalues) and [[concepts/vqe]] (short circuits with a classical optimizer). ^two-pathways

## Research papers

- [[papers/omalley-2016-h2-molecular-energies|O'Malley 2016 (H₂)]] and [[papers/kandala-2017-hardware-efficient-vqe|Kandala 2017 (BeH₂)]]: molecular energy curves on superconducting qubits; investment and press context in [[analyses/reflect-rev-draft-002]].

## Sources

- [Simulation of chemistry problems](../sources/week-4-04-simulation-of-chemistry-problems.md)
- [Phase estimation](../sources/week-4-05-phase-estimation.md), [VQE](../sources/week-4-06-variational-quantum-eigensolver.md)
