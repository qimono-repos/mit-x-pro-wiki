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
- In the Shor deep dive, Shor says the exact QFT costs on the order of $(\log c)^2$ gates, and the approximate QFT, which is enough for factoring, needs about $\log c \cdot \log\log c$. Here $c$ is the period bound, so $\log c$ is the register width $n$. That is $O(n^2)$ versus $O(n \log n)$. The "drop the tiniest controlled-phase gates" mechanism is standard background, not quoted from the lecture.

A text unit in week 2 derives the classical DFT beside the quantum circuit (Hadamards and controlled phase rotations $R_k = \mathrm{diag}(1, e^{2\pi i / 2^k})$). See [week 2 raw](/mit-raw/week2.md).

## Sources

- [Quantum Fourier Transform (optional reading)](../sources/week-2-08-quantum-fourier-transform.md)
- [How Shor's algorithm works](../sources/week-2-07-factoring-with-a-quantum-computer-how-shor-s-algorithm-works.md)
- [Shor: introduction to the quantum factoring algorithm](../sources/week-1-03-shor-s-algorithm-introduction-to-the-short-quantum-factorization-algorithm.md): gate-count remark
- Raw: [week 1](/mit-raw/week1.md), [week 2](/mit-raw/week2.md)
