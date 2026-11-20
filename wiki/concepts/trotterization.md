---
title: Trotterization
type: concept
---

# Trotterization

Trotterization approximates the exponential of a sum by a product of exponentials. For $H = \sum_\ell H_\ell$,

$$
e^{-iHt} = \Bigl(\prod_\ell e^{-i H_\ell t/n}\Bigr)^n + O(t^2/n),
$$

the first-order Lie–Trotter formula. Each $e^{-i H_\ell \Delta t}$ is easy when $H_\ell$ is a Pauli string or another local term: it is a small circuit of basis changes and a diagonal phase. Raising $n$ (more slices) shrinks the error. Higher-order product formulas cancel more commutators and reduce the number of slices needed for a given $\varepsilon$.

This is the concrete algorithm the course uses for [[concepts/hamiltonian-simulation]] before it introduces [[concepts/phase-estimation]] and [[concepts/vqe]] as ways to read energies out.

## Sources

- [Hamiltonian simulation: Trotterization](../sources/week-4-03-hamiltonian-simulation-trotterization.md)
- Raw: [week 4](/mit-raw/week4.md)
