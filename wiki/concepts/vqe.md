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

when $H = \sum_k c_k P_k$ is a linear combination of Pauli strings (the form chemistry Hamiltonians take after a fermion-to-qubit map). A classical optimizer proposes a new $\theta$. **Division of labour:** state preparation and the measurement of expectation values run on the quantum device; *parameter optimization* runs on the classical computer. The variational theorem says $E(\theta) \ge E_0$, so the loop is minimizing an upper bound on the ground energy. ^hybrid-loop

Week 4 contrasts this hybrid loop with Trotter-plus-phase-estimation, then looks at VQE in practice: ansatz choice, measurement grouping, and noise. The same week is the lead-in to week 5's optimization lectures.

## Research papers

- [[papers/omalley-2016-h2-molecular-energies|O'Malley 2016 (H₂)]] (VQE vs phase estimation, H₂) and [[papers/kandala-2017-hardware-efficient-vqe|Kandala 2017 (BeH₂)]] (hardware-efficient ansatz, up to BeH₂). Both show the hybrid loop in their Fig. 1.

## Sources

- [Variational quantum eigensolver](../sources/week-4-06-variational-quantum-eigensolver.md)
- [VQE in practice](../sources/week-4-07-vqe-in-practice.md)
- Raw: [week 4](/mit-raw/week4.md)
