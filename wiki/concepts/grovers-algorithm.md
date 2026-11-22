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

One Grover iterate is $G = D\, U_w$. In the course's notation, the oracle first reflects about the non-solution axis $|\alpha\rangle$ (it flips the sign of the solution component $|\beta\rangle$). The diffusion step, conditional phase shifts between Hadamards, then reflects about the starting superposition $|\psi\rangle$. Two reflections make a rotation toward $|\beta\rangle$ ([raw week 5](/mit-raw/week5.md), quantum search transcript ~7:27–7:47). Starting from $|s\rangle$, each iterate rotates the state by $2\theta$ toward $|w\rangle$ in the plane spanned by $|w\rangle$ and the unmarked uniform state, where ^two-reflections

$$
\sin \theta = \frac{1}{\sqrt{N}}
$$

for a single marked item. After about $\lfloor \pi/4 \sqrt{N} \rfloor$ iterates the marked state is measured with high probability. With $M$ marked items the course bounds the number of repetitions by $R \le \frac{\pi}{4}\sqrt{N/M}$; overshooting lowers the success probability again. ^iteration-bound

**Register size.** The index register holds $x = 0, \dots, N-1$ with $N = 2^n$, so it needs $n = \log_2 N$ qubits (plus the oracle's ancilla), not $N$, $n^2$ or $2^N$ ([raw week 5](/mit-raw/week5.md), quantum search, ~2:23). ^register-size

## In this course

Week 5 covers the algorithm, a walkthrough on the IBM Quantum Experience, and a lab in QASM (the OpenQASM syntax used by the composer: registers, `h`, `x`, `cx`, `ccx`, `measure`).

- [Quantum search](../sources/week-5-04-grover-s-algorithm-quantum-search.md)
- [Quantum Experience](../sources/week-5-05-introduction-to-grover-s-algorithm-on-the-quantum-experience.md)
- [Lab practicum](../sources/week-5-06-lab-practicum-grover-s-algorythm.md)
- Raw: [week 5](/mit-raw/week5.md)

## Related

- [[concepts/exactly-1-3-sat]]: the course's worked oracle example (3 variables, solution $|101\rangle$, 2 iterations ≈ 95%).
