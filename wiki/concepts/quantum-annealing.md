---
title: Quantum annealing
type: concept
---

# Quantum annealing

A quantum annealer is the open-system cousin of [[concepts/adiabatic-quantum-computing]]. It is aimed at classical optimization (a cost function encoded as $E(z)$ on bitstrings) and it is allowed to leave the ground state.

Kadowaki and Nishimori (1998) proposed using quantum tunneling together with dissipation — relaxation back toward low energy — so the device can fall back into the ground state, or at least a lower state, after crossing a small avoided crossing. That sidesteps the strict adiabatic requirement that the system never leave the ground state. ^tunneling-relaxation

The course states: "to date, there is no evidence that quantum annealing computers feature quantum enhancement" ([raw week 5](/mit-raw/week5.md), AQC concept Learn). ^no-enhancement-evidence

**Encoding.** "A cost function is encoded into a Hamiltonian using a prescribed approach": in practice an Ising-type $H_p = \sum_i h_iZ_i + \sum_{i<j}J_{ij}Z_iZ_j$ whose ground state is the optimum (see [[concepts/adiabatic-quantum-computing#^ising]]). The word "Ising" appears in the course only inside quiz stems; the hardware fact comes from an [external source](/mit-raw/external/quantum-annealing-ising.md). Gap logic carries over from AQC: a *smaller* minimum gap, not a larger one, forces slower evolution through the gap region (see [[concepts/adiabatic-quantum-computing#^minimum-gap]]). ^encoding-and-gap

The same problem Hamiltonian and transverse driver appear on the adiabatic slides; what changes is the role of the bath.

## Sources

- [Introduction to quantum optimization](../sources/week-5-01-introduction-to-quantum-optimization.md)
- Raw: [week 5](/mit-raw/week5.md)
