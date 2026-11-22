---
title: QAOA
type: concept
aliases: [Quantum Approximate Optimization Algorithm]
---

# QAOA

The Quantum Approximate Optimization Algorithm is a *gate-model* approximate optimizer. It alternates two parameterized unitaries, one built from the problem's cost function and one from a transverse $X$ field, then measures a bit string that should satisfy a large fraction of the clauses. It was introduced by Farhi, Goldstone and Gutmann in 2014 and is pitched as a natural fit for shallow near-term hardware ([source note](../sources/week-5-02a-qaoa-farhi.md)).

## The problem it targets

Combinatorial optimization: bit strings $z$ and clauses on subsets of bits. The cost $C(z)$ is the number of clauses $z$ satisfies. Maximizing it exactly is NP-hard, so QAOA looks for a *good* string, not necessarily the best ([raw transcript](/mit-raw/week5-qaoa.md), ~0:00–2:07). ^problem

## The circuit

Start with every spin along $x$:

$$
|s\rangle = |+\rangle^{\otimes n} = \frac{1}{\sqrt{2^n}} \sum_z |z\rangle .
$$

Promote the cost function to an operator that is diagonal in the computational basis (so it's Hermitian and easy to build):

$$
C\,|z\rangle = C(z)\,|z\rangle, \qquad B = \sum_{j} \sigma_x^{j} .
$$

$B$ is the same operator AQC uses as its starting Hamiltonian. The two building blocks are

$$
U(C,\gamma) = e^{-i\gamma C}, \qquad U(B,\beta) = e^{-i\beta B}.
$$

$U(B,\beta)$ rotates every spin about the $x$ axis. *Convention note (background):* on the Bloch sphere $e^{-i\beta X}$ is a rotation by $2\beta$; the lecture says "by an angle beta" loosely. ^circuit

**Depth 1:** prepare $|s\rangle$, apply $e^{-i\gamma C}$, then $e^{-i\beta B}$, measure in the computational basis. **Depth $p$:** alternate the pair $p$ times with fresh parameters,

$$
|\gamma, \beta\rangle = e^{-i\beta_p B} e^{-i\gamma_p C} \cdots e^{-i\beta_1 B} e^{-i\gamma_1 C}\, |s\rangle .
$$

More layers "can only improve" performance, since a deeper circuit can reproduce a shallower one, but it has proved too hard to analyze beyond the shallowest depth ([raw transcript](/mit-raw/week5-qaoa.md), ~5:51–6:41 and ~9:14–10:07). ^depth

## How it compares

| | AQC | QAOA |
|---|---|---|
| Model | continuous Hamiltonian evolution | discrete gates, gate model |
| Same ingredients | driver $B = \sum X$, problem Hamiltonian | $e^{-i\beta B}$, $e^{-i\gamma C}$ |
| Goal | stay in the ground state, exact answer | a good approximate string |

*Background, not stated in the video:* a deep QAOA with small angles resembles a Trotterized adiabatic sweep ([[concepts/trotterization]]), and in practice $\gamma, \beta$ are usually tuned by a classical optimizer, as in [[concepts/vqe]].

## Track record (as told in the course)

- **2014, restricted MAX-CUT:** a guaranteed approximation ratio better than random guessing on every instance, of any size, but not better than the best classical algorithm.
- **E3LIN2:** the shallow circuit beat the best known classical algorithm, until ten classical computer scientists, prompted by Scott Aaronson's blog post, found a classical algorithm that beat it.
- **Now:** on provable worst-case guarantees, the classical algorithm is ahead. Farhi is optimistic that running QAOA on near-term devices may reveal parameters that do as well as classical methods, or better ([raw transcript](/mit-raw/week5-qaoa.md), ~6:41–10:58). ^track-record

## Sources

- [QAOA (Farhi video)](../sources/week-5-02a-qaoa-farhi.md)
- Raw: [QAOA transcript](/mit-raw/week5-qaoa.md) · [week 5](/mit-raw/week5.md) (intro, line 32)
