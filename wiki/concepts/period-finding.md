---
title: Period finding
type: concept
---

# Period finding

Period finding is the quantum subroutine inside [[concepts/shors-algorithm]]. The input is a black-box function on the integers with an unknown period $r$ (the lecture sometimes calls it $c$):

$$
f(x) = f(x + r).
$$

Classically, with only a black box, you walk $f(0), f(1), \ldots$ until the values repeat, which takes on the order of $r$ queries. The quantum algorithm finds $r$ in time polynomial in $\log r$.

## Circuit

1. Start in a uniform superposition on a register large enough that $2^q \ge 2 r_{\max}$. The lecture writes this as $|+\rangle^{\otimes 2\ell}$ tensored with a zeroed output register.
2. Compute $f$ reversibly into the second register: $|x\rangle|0\rangle \mapsto |x\rangle|f(x)\rangle$.
3. Apply the [[concepts/quantum-fourier-transform]] to the first register.
4. Measure, and finish with classical continued-fraction post-processing to extract $r$ from the sampled peak $k / 2^q \approx s / r$.

The second register is required even if it is later ignored. Without computing $f$, the first register is just the Fourier transform of a uniform state and the interference that encodes the period never appears. Measuring the second register and discarding the outcome is optional; it does not change the reduced state of the first register.

## Course sources

- [Period finding algorithm](../sources/week-1-01-period-finding-algorithm.md)
- [Detailed steps of quantum order finding](../sources/week-1-05-shor-s-algorithm-detailed-steps-of-the-quantum-order-finding-algorithm.md) when present
- Raw: [week 1](/mit-raw/week1.md)
