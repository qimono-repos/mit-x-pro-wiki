---
title: Shor's algorithm
type: concept
---
	                                                                                                               ``````                                                                                                               ```
# Shor's algorithm

Shor's algorithm factors an integer by reducing factoring to order-finding, then finding that order with a quantum period-finding routine. The quantum part is not a direct search over factors.

## Reduction

Let $N = pq$ with $p$ and $q$ odd primes (the course treats the two-prime case). The classical trick used by the quadratic sieve, and reused here, is to find $x$ and $y$ such that

$$
x^2 \equiv y^2 \pmod N, \qquad x \not\equiv \pm y \pmod N.
$$

Then $N$ divides $(x-y)(x+y)$ but neither factor, so

$$
\gcd(x-y, N)
$$

yields a nontrivial factor via Euclid's algorithm.

Pick a random base $g$ with $1 < g < N$ and $\gcd(g, N) = 1$. The order $r$ is the period of

$$
f(x) = g^x \bmod N,
$$

i.e. the smallest positive integer with $g^r \equiv 1 \pmod N$. If $r$ is even and $g^{r/2} \not\equiv -1 \pmod N$, then

$$
g^{r/2} - 1 \quad\text{and}\quad g^{r/2} + 1
$$

supply the $x-y$ and $x+y$ above. The course states that a random $g$ succeeds with probability at least $1/2$; otherwise draw another $g$.

Worked modulus in the lecture: $N = 21$, $g = 2$, $2^6 \equiv 1 \pmod{21}$, so $r = 6$ and $\gcd(2^3 - 1, 21) = 7$.

## Quantum part

The circuit is the same shape as [[concepts/simons-algorithm]]: a uniform superposition, a reversible $f$, then a Fourier transform over the domain, then measurement and classical post-processing. Simon uses the Hadamard transform over $(\mathbb{Z}/2\mathbb{Z})^n$. Shor uses the [[concepts/quantum-fourier-transform]] over $\mathbb{Z}/2^q\mathbb{Z}$ with $2^q$ larger than the unknown period.

The period is recovered in time polynomial in $\log r$, not linear in $r$. An approximate QFT is enough and uses fewer gates than the exact one.

## Where this is in the course

- [Reduction of factoring to order finding](../sources/week-1-02-shor-s-algorithm-reduction-of-factoring-to-order-finding.md) (week 1 raw)
- [Introduction to the quantum factoring algorithm](../sources/week-1-03-shor-s-algorithm-introduction-to-the-short-quantum-factorization-algorithm.md)
- [How Shor's algorithm works](../sources/week-2-07-factoring-with-a-quantum-computer-how-shor-s-algorithm-works.md) if that source note exists after the index rebuild; otherwise [week 2 raw](/mit-raw/week2.md)
- See also [[concepts/period-finding]], [[concepts/quantum-fourier-transform]]
