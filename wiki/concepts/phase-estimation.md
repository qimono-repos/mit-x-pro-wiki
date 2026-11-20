---
title: Phase estimation
type: concept
---

# Phase estimation

Quantum phase estimation writes the eigenphase of a unitary into a clock register. Given $U$ and an eigenstate $U|\psi\rangle = e^{2\pi i \varphi}|\psi\rangle$, a $t$-qubit clock estimates $\varphi$ to about $t$ bits.

1. Clock in uniform superposition, target in $|\psi\rangle$.
2. Controlled-$U^{2^k}$ from clock qubit $k$ onto the target. The clock picks up the phase kickback $|k\rangle|\psi\rangle \mapsto e^{2\pi i \varphi k}|k\rangle|\psi\rangle$.
3. Inverse [[concepts/quantum-fourier-transform]] on the clock.
4. Measure the clock. The bits are the binary expansion of $\varphi$.

If the input is a superposition of eigenstates, the measurement both samples an eigenvalue and collapses the target onto the corresponding eigenstate. Shor's period finding is phase estimation applied to the unitary "multiply by $g$ modulo $N$". In week 4 the same routine reads energies: if $U = e^{-iH\tau}$, then $\varphi$ is the energy in units of $2\pi/\tau$.

## Sources

- [Phase estimation](../sources/week-4-05-phase-estimation.md)
- Raw: [week 4](/mit-raw/week4.md), and the order-finding pages in [week 1](/mit-raw/week1.md)
