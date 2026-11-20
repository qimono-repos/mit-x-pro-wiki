---
title: Variational quantum eigensolver
type: concept
---

# Variational quantum eigensolver

VQE estimates the ground-state energy of a Hamiltonian with a short parameterized circuit and a classical optimizer. It is the near-term alternative to [[concepts/phase-estimation]], which needs deep controlled time-evolution.

Prepare $|\psi(\theta)\rangle = U(\theta)|0\rangle$ on the device. Measure enough Pauli expectations to assemble

$$
E(\theta) = \langle \psi(\theta) | H | \psi(\theta) \rangle = \sum_k c_k \langle P_k \rangle_\theta
$$

when $H = \sum_k c_k P_k$ is a linear combination of Pauli strings (the form chemistry Hamiltonians take after a fermion-to-qubit map). A classical optimizer proposes a new $\theta$. The variational theorem says $E(\theta) \ge E_0$, so the loop is minimizing an upper bound on the ground energy.

Week 4 contrasts this hybrid loop with Trotter-plus-phase-estimation, then looks at VQE in practice: ansatz choice, measurement grouping, and noise. The same week is the lead-in to week 5's optimization lectures.

## Sources

- [Variational quantum eigensolver](../sources/week-4-06-variational-quantum-eigensolver.md)
- [VQE in practice](../sources/week-4-07-vqe-in-practice.md)
- Raw: [week 4](/mit-raw/week4.md)
