---
title: Quantum simulation (approaches and issues)
type: concept
aliases: [analog simulation, digital simulation, analog deformation, quantum-inspired, DMRG, PEPS, MERA, ultracold atoms]
---

# Quantum simulation: approaches and issues

Manin (1980) and Feynman (1982) observed that simulating a quantum system on a classical computer costs time exponential in the number of particles, so the natural simulator is another, well-controlled quantum system. Week 3 (raw week 4) opens with Isaac Chuang's list of the ideas and issues involved.

## Approaches

**Digital simulation:** run the target dynamics on a universal, gate-based quantum computer (see [[concepts/hamiltonian-simulation]] and [[concepts/trotterization]]). **Analog simulation:** map and/or *deform* the Hamiltonian a device naturally has, so it mimics the target system. **Hybrid:** analog elements plus digital gates, often run as a classical–quantum optimization loop; VQE is the example ([source note](../sources/week-4-00-introduction-quantum-simulation.md)). ^approaches

**Analog deformation**, one of the earliest analog techniques: start from the Hamiltonian the hardware gives you and deform it so it looks like the target Hamiltonian. This doesn't need to hold at all times, only **time-averaged** or **stroboscopically** (at $T, 2T, 3T, \dots$). That strategy is used, for example, by **ultracold atom gases / Bose–Einstein condensates** simulating a superconducting system ([raw week 4](/mit-raw/week4.md), Chuang transcript, ~2:24–3:19). ^analog-deformation

## Ideas and issues (Chuang's slide list)

1. **"In-principle simulation":** can the device's available terms $\{H_k^{QC}\}$ generate the target $H_{sys}$?
2. *(slide not captured)*
3. **What to measure?** Even if you can prepare $e^{-iHt}|\psi_0\rangle$, measuring it collapses the state and gives "only one statistical sample of that wave function." Reading out a useful answer is a challenge in itself.
4. **Improve *classical* simulation with quantum-inspired approximations:** DMRG, then PEPS, MERA, ...

([raw week 4](/mit-raw/week4.md), "Ideas and Issues" slides at lines 398 and 1009; transcript ~4:17.) ^ideas-and-issues

**Quantum-inspired classical methods.** "The technique that started all of this in physics was the density matrix renormalization group idea," linked by the lecture to the Nobel prize of Ken Wilson and colleagues. Newer methods include PEPS and MERA. These are *classical* algorithms; neutral-atom hardware is not what PEPS means (same transcript, ~6:48–7:18). The course's further reading, *DMRG for Dummies* ([external source](/mit-raw/external/dmrg-for-dummies.md)), gives the history: Wilson's numerical renormalization group came first, and **Steven White's DMRG (1992)** made it work for strongly interacting chains. DMRG keeps only the most important states of each block (the largest reduced-density-matrix eigenvalues). It excels in 1D, where entanglement is limited, and struggles in 2D (area law), which is where PEPS-type methods come in. Its time-dependent version uses the same Suzuki–Trotter splitting as [[concepts/trotterization]]. ^quantum-inspired

## Research papers

- [[papers/zhang-2017-53-ion-dynamical-phase-transition|Zhang 2017 (53 ions)]]: analog simulation of a long-range Ising magnet with 53 ions; [[papers/omalley-2016-h2-molecular-energies|O'Malley 2016 (H₂)]] and [[papers/kandala-2017-hardware-efficient-vqe|Kandala 2017 (BeH₂)]]: digital simulation of molecules. Discussion: [[analyses/reflect-rev-draft-002]].

## Sources

- [Introduction: quantum simulation](../sources/week-4-00-introduction-quantum-simulation.md)
- See [[concepts/hamiltonian-simulation]], [[concepts/quantum-chemistry]], [[concepts/vqe]]
