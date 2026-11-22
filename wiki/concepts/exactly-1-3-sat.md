---
title: Exactly-1 3-SAT
type: concept
aliases: [3-SAT, 3SAT, satisfiability, SAT, Boolean satisfiability]
---

# Exactly-1 3-SAT

Exactly-1 3-SAT asks for an assignment of Boolean variables that makes a 3-CNF formula true, with **exactly one true literal in every clause**. The course uses it as the search problem for [[concepts/grovers-algorithm]]: the formula becomes a quantum oracle $U_f$, and Grover finds the single satisfying assignment among $2^3 = 8$ inputs in two oracle calls.

## Vocabulary

Course legend ([raw week 5](/mit-raw/week5.md), slide at ~line 3810): $\vee$ = OR, $\wedge$ = AND, $\neg$ = NOT. A bracket marks one parenthesized factor as a **clause** and its three terms as **literals**.

Formal definitions that the course leaves implicit. These come from [external source: Boolean satisfiability](/mit-raw/external/boolean-satisfiability.md), not the course:

| Term | Meaning |
|---|---|
| literal | $x_i$ or $\neg x_i$ |
| clause | OR of literals; in 3-SAT, exactly three |
| 3-CNF formula | AND of clauses |
| satisfiable | some assignment makes the formula $= 1$ |
| 3-SAT | "is this 3-CNF formula satisfiable?" (NP-complete) |

In the course's words (transcript, ~line 3787): a 3-SAT formula "is the logical AND of a series of clauses ... where each clause is the logical OR of three Boolean variables or their negation." The transcript's "end" is a speech-to-text error for AND.

## Plain 3-SAT vs. Exactly-1 3-SAT

| | clause condition | per-clause truth |
|---|---|---|
| 3-SAT | at least one literal true | $l_1 \vee l_2 \vee l_3$ |
| Exactly-1 3-SAT | exactly one literal true | $l_1 \oplus l_2 \oplus l_3 \oplus (l_1 l_2 l_3)$ |

The course calls Exactly-1 3-SAT "a variation of the well-known three-satisfiability problem, and it is NP-hard" (raw week 5, ~line 3836).

## The course instance

$$
f(x_1,x_2,x_3)=(x_1\vee x_2\vee\neg x_3)\wedge(\neg x_1\vee\neg x_2\vee\neg x_3)\wedge(\neg x_1\vee x_2\vee x_3)
$$

Truth table from the lecture slide (1 = true):

| $x_1x_2x_3$ | $f$ | why not |
|---|---|---|
| 000 | 0 | 2nd clause has three true literals |
| 001 | 0 | 2nd clause has two true literals |
| 010 | 0 | 2nd clause has two true literals |
| 011 | 0 | 3rd clause has three true literals |
| 100 | 0 | 2nd clause has two true literals |
| **101** | **1** | **"Bingo!"** |
| 110 | 0 | 1st clause has three true literals |
| 111 | 0 | 2nd clause is not satisfied (zero true literals) |

Compare row 110. As plain 3-SAT, $(1,1,0)$ satisfies all three clauses (each has at least one true literal), so $f_{\text{3-SAT}}(110) = 1$. It fails Exactly-1 only because clause 1 has *three* true literals. This is the cleanest illustration of how the two problems differ. (Own check against the table above.)

## Oracle construction (course circuit)

One ancilla $y_\alpha$ per clause, then the output qubit is set iff all $y_\alpha = 1$ ([raw week 5](/mit-raw/week5.md), ~lines 4010–4160):

1. $X$ on every variable that appears negated in the clause, so the wire now carries the literal value.
2. Three CNOTs into $y_\alpha$: $y_\alpha = l_1 \oplus l_2 \oplus l_3$, which is 1 iff an **odd** number of literals is true (1 or 3).
3. A triply-controlled NOT on $l_1, l_2, l_3$ flips $y_\alpha$ back when **all three** are true, leaving 1 iff **exactly one** is true.
4. Undo the $X$ gates from step 1.

Step 3's gate isn't native, so the course builds it from **3 Toffolis plus 1 ancilla**, resetting the ancilla afterwards ("if you plan to re-use the auxiliary qubits, you should leave them in the same state"). The full $U_f$ uses four auxiliary qubits.

That is the general pattern: **the oracle only *recognizes* a solution; finding it is Grover's job.** In the course's words, determining and returning the satisfying assignment is "the goal of Grover's algorithm, not of the function f."

## Grover on this instance

$N = 8$, one marked state. Two iterations give $|101\rangle$ with probability ≈ 0.95 (simulator histogram: 0.948777). Three iterations drop it to ≈ 32%, overshooting, so "the number of iterations must be chosen optimally" (raw week 5, ~lines 4400–4740). The ideal value is $\sin^2\!\big((2k+1)\theta\big)$ with $\sin\theta = 1/\sqrt 8$: 0.945 at $k=2$ and 0.33 at $k=3$, matching the course (own calculation).

## Sources

- [Introduction to Grover's algorithm on the Quantum Experience](../sources/week-5-05-introduction-to-grover-s-algorithm-on-the-quantum-experience.md): formula, truth table, oracle construction, iteration histograms
- [Lab practicum: Grover's algorithm](../sources/week-5-06-lab-practicum-grover-s-algorythm.md)
- [Quantum optimization quiz](../sources/week-5-08-quantum-optimization-qiz.md): Q5 tests the definitions on this page
- External: [Boolean satisfiability](/mit-raw/external/boolean-satisfiability.md): formal definitions of literal, clause, CNF, satisfiable
