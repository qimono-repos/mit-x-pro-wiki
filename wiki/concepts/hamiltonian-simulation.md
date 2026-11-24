---
title: Hamiltonian simulation
type: concept
---

# Hamiltonian simulation

Hamiltonian simulation implements the unitary evolution

$$
U(t) = e^{-iHt}
$$

of a quantum system whose Hamiltonian $H$ is a sum of local terms, to accuracy $\varepsilon$, on a gate-model computer. It is the primitive underneath quantum chemistry and underneath [[concepts/phase-estimation]].

**What a Hamiltonian is.** "The Hamiltonian is a physical quantity that represents the total energy of a system." For a closed system it is kinetic plus potential energy, $\hat H = \hat p^2/2m + \hat V$; its eigenvalues and expectation values are energies. It also "enables one to find the time evolution" through the Schrödinger equation, $\psi(t) = e^{-i\hat H t/\hbar}\psi(0)$ ([raw week 4](/mit-raw/week4.md), "What is a Hamiltonian?", ~line 1050). The lecture adds that "with a Hamiltonian in hand ... one can simulate the Hamiltonian dynamics using universal gates" (transcript, ~0:25). *Background, not a course quote:* physical gates are themselves implemented by letting qubits evolve under controlled Hamiltonians, so gate operators are built from Hamiltonian terms. The degree of entanglement is a property of a *state*, not something the Hamiltonian "gives". ^what-is-a-hamiltonian

The course's running illustration is a particle in a box. The particle is described by a wavefunction and is generally delocalized, not at one point. Its Hamiltonian has *both* a kinetic term ($\hat p^2/2m$, with $\hat p = -i\hbar\,\partial/\partial x$) and the potential $V(x)$ (0 inside the box, $\infty$ outside). Simulation starts by discretizing: the continuous position becomes a superposition over a discrete set of grid states ([raw week 4](/mit-raw/week4.md), particle-in-a-box Learn and transcript ~1:11). ^particle-in-a-box

In more detail: discretize the line, write the kinetic term as a finite-difference second derivative (a sparse circulant-like matrix on the grid), and the potential as a diagonal. The resulting $H$ is sparse and Hermitian, so it has a unitary exponential, but the exponential of the sum is not the product of the exponentials. That is the gap [[concepts/trotterization]] fills.

Chemistry problems in the same week are the same task with $H$ the electronic Hamiltonian in a chosen basis (Jordan–Wigner or similar maps turn fermionic terms into Pauli strings).

## Research papers

- [[papers/kandala-2017-hardware-efficient-vqe|Kandala 2017 (BeH₂)]]: Hamiltonians as sums of 100+ Pauli terms on 6 qubits.

## Sources

- [What is a Hamiltonian?](../sources/week-4-01-what-s-a-hamiltonian.md)
- [Particle in a box](../sources/week-4-02-simulation-example-particle-in-a-box.md)
- [Simulation of chemistry problems](../sources/week-4-04-simulation-of-chemistry-problems.md)
- Raw: [week 4](/mit-raw/week4.md)
