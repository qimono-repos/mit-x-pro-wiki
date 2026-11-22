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

1. Start the first register in a uniform superposition. The course sizes it as $N^2 \le 2^l \le 2N^2$, so the register is long enough to hold many periods of any $r < N$. The output register starts at $|0\rangle$.
2. Compute $f$ reversibly into the second register: $|x\rangle|0\rangle \mapsto |x\rangle|f(x)\rangle$.
3. Apply the [[concepts/quantum-fourier-transform]] to the first register.
4. Measure, and finish with classical continued-fraction post-processing to extract $r$ from the sampled peak $C / 2^l \approx z / r$.

The second register is required even if it is later ignored. Without computing $f$, the first register is just the Fourier transform of a uniform state and the interference that encodes the period never appears. Measuring the second register and discarding the outcome is optional; it does not change the reduced state of the first register.

## Worked example from the course: $f(x) = 11^x \bmod 21$

$N = 21$, so $441 \le 2^l \le 882$ gives $l = 9$ (512 basis states). After the Hadamards and the reversible $f$:

$$
\frac{1}{\sqrt{2^{9}}}\sum_{x=0}^{511}|x\rangle|11^{x}\bmod 21\rangle .
$$

Measuring the output register (say it reads 16) leaves the first register as a comb with spacing $r$, offset 2:

$$
\frac{1}{\sqrt{2^{9}/r}}\sum_{y=0}^{2^{9}/r-1}|yr+2\rangle|16\rangle .
$$

The QFT turns the comb into peaks at multiples of $2^9/r$, and the offset becomes only a phase:

$$
\rightarrow \frac{1}{\sqrt{r}}\sum_{z=0}^{r-1}\exp\!\left(2\,\frac{2\pi i}{r}z\right)\left|z\,\frac{2^{9}}{r}\right\rangle .
$$

That last line is the whole trick: **the offset (which value of $x$ you happened to land on) goes into the phase, and the period goes into the position of the peaks.** Measurement only sees the positions.

One honest caveat: here $r = 6$ ($11^6 = 1771561 \equiv 1 \pmod{21}$), and $2^9/6 \approx 85.3$ is not an integer. The course's last line is the idealized case where $r$ divides $2^l$. In reality the peaks are sharp but sit *near* $z \cdot 85.3$, and that is exactly why the classical step uses continued fractions (convergents $z_n/r_n$) instead of plain division. Source: [raw week 1](/mit-raw/week1.md), first page.

## Related

- [[concepts/rsa-cryptosystem]]: the same periodicity of $x^i \bmod N$ is what makes RSA decryption work; Alice knows the period's multiple $(p-1)(q-1)$, Eve has to measure an order.

## Course sources

- [Period finding algorithm](../sources/week-1-01-period-finding-algorithm.md)
- [Detailed steps of quantum order finding](../sources/week-1-05-shor-s-algorithm-detailed-steps-of-the-quantum-order-finding-algorithm.md)
- [Measurement result as a geometric sum](../sources/week-1-06-shor-s-algorithm-order-finding-algorithm-measurement-result-as-a-geometric-sum.md)
- Raw: [week 1](/mit-raw/week1.md)
