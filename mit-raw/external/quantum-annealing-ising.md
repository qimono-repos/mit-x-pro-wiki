---
title: "External: quantum annealing and Ising Hamiltonians"
type: external-source
added: 2026-11-22
added_by: Claude (Opus 5.5), on request
reason: The course says a cost function "is encoded into a Hamiltonian using a prescribed approach" (raw week 5, introduction to quantum optimization), but never names the Ising form that annealers actually use, except inside quiz stems. This file fills that gap from outside sources. It is NOT course material.
---

# External source: quantum annealing uses Ising Hamiltonians

Paraphrased, with links.

- **Problem encoding.** To run a problem on a D-Wave annealer you define an Ising Hamiltonian, $H = \sum_i h_i\sigma^z_i + \sum_{i<j} J_{ij}\sigma^z_i\sigma^z_j$, whose ground state represents the solution. The device takes the coefficients $h$ and $J$ and returns the spin vector that minimizes the energy. ([Ayanzadeh et al., arXiv:2001.00234](https://arxiv.org/pdf/2001.00234), Introduction)
- **Same story as AQC.** Prepare the ground state of a simple driver Hamiltonian, then evolve toward a final Hamiltonian whose ground state encodes the optimization problem's solution. Annealing is a heuristic version of this, used to find ground states of Ising models. ([Yarkoni et al., "Quantum Annealing for Industry Applications", arXiv:2112.07491](https://arxiv.org/abs/2112.07491))
- **QUBO ↔ Ising.** Quadratic unconstrained binary optimization (QUBO) problems map one-to-one onto Ising problems (spin $s = 2x-1$). That's why "QUBO" and "Ising" are used interchangeably in annealing papers. (same sources)

## Relation to the course

It matches the course's adiabatic slides ($H(t)=(1-t/T)B+(t/T)H_p$, $B=-\sum_j\sigma_x^j$, $H_p|z\rangle=E(z)|z\rangle$, raw week 5 ~line 1038): an Ising $H_p$ is just a diagonal $E(z)$ written with $Z$ operators. The course quiz's Ising-chain question uses exactly this form.
