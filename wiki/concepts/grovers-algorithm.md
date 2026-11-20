---
title: Grover's algorithm
type: concept
---

# Grover's algorithm

Grover's algorithm finds a marked item in an unstructured search space of size $N$ with $O(\sqrt{N})$ queries of a phase oracle. A classical algorithm needs $\Theta(N)$ queries in the worst case.

## Step

The oracle reflects the amplitude of every marked basis state $|w\rangle$:

$$
U_w |x\rangle = (-1)^{f(x)} |x\rangle, \qquad f(w) = 1.
$$

The diffusion operator reflects about the uniform superposition $|s\rangle$:

$$
D = 2|s\rangle\langle s| - I, \qquad |s\rangle = \frac{1}{\sqrt{N}}\sum_x |x\rangle.
$$

One Grover iterate is $G = D\, U_w$. Starting from $|s\rangle$, each iterate rotates the state by $2\theta$ toward $|w\rangle$ in the plane spanned by $|w\rangle$ and the unmarked uniform state, where

$$
\sin \theta = \frac{1}{\sqrt{N}}
$$

for a single marked item. After about $\lfloor \pi/4 \sqrt{N} \rfloor$ iterates the marked state is measured with high probability.

## In this course

Week 5 covers the algorithm, a walkthrough on the IBM Quantum Experience, and a lab in QASM (the OpenQASM syntax used by the composer: registers, `h`, `x`, `cx`, `ccx`, `measure`).

- [Quantum search](../sources/week-5-04-grover-s-algorithm-quantum-search.md)
- [Quantum Experience](../sources/week-5-05-introduction-to-grover-s-algorithm-on-the-quantum-experience.md)
- [Lab practicum](../sources/week-5-06-lab-practicum-grover-s-algorythm.md)
- Raw: [week 5](/mit-raw/week5.md)
