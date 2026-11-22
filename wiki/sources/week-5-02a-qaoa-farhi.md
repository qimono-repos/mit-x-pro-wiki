---
title: "Quantum Approximate Optimization Algorithm"
type: source
week: 5
raw: mit-raw/week5-qaoa.md
---

# Quantum Approximate Optimization Algorithm

Week 5 (official Week 4) video 3: Eddie Farhi introduces the **Quantum Approximate Optimization Algorithm**. [Raw transcript](/mit-raw/week5-qaoa.md)

Missing from the original `week5.md` capture; transcript added 2026-11-22. Learn prose is not captured. The page's practice question is **Q1: Quantum Approximate Optimization Algorithm** ([[quizzes/week-4|Week 4 quizzes]]).

## What the video covers

- **Combinatorial optimization (0:00–2:07).** Bit strings and clauses, each clause looking at a subset of bits. Satisfying the most clauses is NP-hard, so the target is an *approximate optimizer*: a good string, not necessarily the best.
- **Gate model, not continuous (2:07–2:38).** Unlike AQC's continuous evolution, QAOA applies a sequence of discrete unitaries to an initial state, then measures.
- **Ingredients (2:38–5:47).** Start with every spin along $x$: the uniform superposition of all bit strings. Cost operator $C|z\rangle = C(z)|z\rangle$, where $C(z)$ is the number of satisfied clauses; it is diagonal in the computational basis and Hermitian. Unitaries $e^{-i\gamma C}$ and $e^{-i\beta B}$ with $B = \sum_j \sigma_x^j$, the same operator as AQC's starting Hamiltonian; $e^{-i\beta B}$ rotates every spin about $x$.
- **Algorithm (5:51–6:41).** Prepare the start state, pick $\gamma$, apply $e^{-i\gamma C}$, pick $\beta$, apply $e^{-i\beta B}$, measure in the computational basis. For some problems there are $\gamma, \beta$ whose output string satisfies a high fraction of clauses.
- **Results (6:41–9:14).** 2014, restricted MAX-CUT: a guaranteed approximation ratio better than random on *every* instance, but not better than the best classical algorithm. E3LIN2: the shallow circuit briefly beat the best known classical algorithm. After Scott Aaronson blogged about it, ten classical computer scientists produced a classical algorithm that beat it. On provable worst-case guarantees, classical is currently ahead.
- **Going deeper (9:14–10:58).** Alternate the two unitaries again with new parameters. More layers can only improve performance, but it's been too hard to analyze beyond the shallowest depth. Farhi's view: it's a natural algorithm to try on near-term hardware because it's shallow and built from simple operators.

## Concepts touched

[[concepts/qaoa]] · [[concepts/adiabatic-quantum-computing]] · [[concepts/vqe]]
