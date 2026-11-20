---
title: Quantum annealing
type: concept
---

# Quantum annealing

A quantum annealer is the open-system cousin of [[concepts/adiabatic-quantum-computing]]. It is aimed at classical optimization (a cost function encoded as $E(z)$ on bitstrings) and it is allowed to leave the ground state.

Kadowaki and Nishimori (1998) proposed using quantum tunneling together with dissipation — relaxation back toward low energy — so the device can fall back into the ground state, or at least a lower state, after crossing a small avoided crossing. That sidesteps the strict adiabatic requirement that the system never leave the ground state. The course states that, as of the lecture, there is still no evidence that annealing hardware shows a quantum enhancement over classical heuristics.

The same problem Hamiltonian and transverse driver appear on the adiabatic slides; what changes is the role of the bath.

## Sources

- [Introduction to quantum optimization](../sources/week-5-01-introduction-to-quantum-optimization.md)
- Raw: [week 5](/mit-raw/week5.md)
