---
title: Simon's algorithm
type: concept
---

# Simon's algorithm

Simon's algorithm finds a hidden XOR mask and is the direct predecessor of [[concepts/shors-algorithm]]. Shor has said he found the factoring algorithm after seeing Simon's circuit, before it was published.

## Promise

$f$ maps $n$-bit strings to $n$-bit strings and is either one-to-one, or two-to-one with a secret $s \neq 0$ such that

$$
f(x) = f(y) \iff y = x \oplus s.
$$

The task is to find $s$.

## Circuit

1. $n$ qubits in $|+\rangle^{\otimes n}$, and an $n$-qubit output register at $|0\rangle$.
2. A black box writes $f(x)$ into the output register.
3. Hadamard transform on the input register. That Hadamard is the [[concepts/quantum-fourier-transform]] over the group $(\mathbb{Z}/2\mathbb{Z})^n$, i.e. bitwise addition without carries.
4. Measure the input register. Each outcome $z$ satisfies $z \cdot s = 0 \pmod 2$.
5. Repeat until the linear equations determine $s$.

Shor's circuit is the same picture with the group changed from bitstrings to integers and the Hadamard replaced by the QFT over $\mathbb{Z}/2^q\mathbb{Z}$.

## Course sources

- [Simon's algorithm](../sources/week-1-04-simon-s-algorithm.md)
- Raw: [week 1](/mit-raw/week1.md)
