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

The course's running illustration is a particle in a box: discretize the line, write the kinetic term as a finite-difference second derivative (a sparse circulant-like matrix on the grid), and the potential as a diagonal. The resulting $H$ is sparse and Hermitian, so it has a unitary exponential, but the exponential of the sum is not the product of the exponentials. That is the gap [[concepts/trotterization]] fills.

Chemistry problems in the same week are the same task with $H$ the electronic Hamiltonian in a chosen basis (Jordan–Wigner or similar maps turn fermionic terms into Pauli strings).

## Sources

- [What is a Hamiltonian?](../sources/week-4-01-what-s-a-hamiltonian.md)
- [Particle in a box](../sources/week-4-02-simulation-example-particle-in-a-box.md)
- [Simulation of chemistry problems](../sources/week-4-04-simulation-of-chemistry-problems.md)
- Raw: [week 4](/mit-raw/week4.md)
