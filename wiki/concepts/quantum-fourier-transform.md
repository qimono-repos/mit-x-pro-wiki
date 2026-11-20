---
title: Quantum Fourier transform
type: concept
---

# Quantum Fourier transform

The quantum Fourier transform (QFT) is the change of basis that makes periodicity visible as peaks. On $n$ qubits, with $Q = 2^n$ and $|x\rangle$ the computational-basis state for the integer $x$,

$$
\mathrm{QFT}|x\rangle = \frac{1}{\sqrt{Q}} \sum_{k=0}^{Q-1} \omega^{xk} |k\rangle, \qquad \omega = e^{2\pi i / Q}.
$$

The inverse QFT uses $\omega^{-1}$.

## Where the course uses it

- [[concepts/simons-algorithm]] uses the $n=1$ case, the Hadamard, copied across $n$ qubits. That is the Fourier transform of bitwise XOR.
- [[concepts/period-finding]] and [[concepts/shors-algorithm]] use the QFT over a large cyclic group so that a state which is periodic in the time domain becomes peaked at multiples of $Q/r$.
- [[concepts/phase-estimation]] uses the same transform to read a binary expansion of an eigenphase out of a clock register.
- The lecture notes that an approximate QFT (dropping the tiniest controlled-phase gates) is enough for factoring and costs about $O(n \log n)$ gates rather than the exact transform's $O(n^2)$.

A text unit in week 2 derives the classical DFT beside the quantum circuit (Hadamards and controlled phase rotations $R_k = \mathrm{diag}(1, e^{2\pi i / 2^k})$). See [week 2 raw](/mit-raw/week2.md).
