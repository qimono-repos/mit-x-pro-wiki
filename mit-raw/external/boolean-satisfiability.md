---
title: "External: Boolean satisfiability (SAT, 3-SAT) — definitions"
type: external-source
added: 2026-11-22
added_by: Claude (Opus 5.5), on request
reason: The course uses "satisfies", "clause", "literal" and the ¬ ∨ ∧ legend (raw week 5, line 3790ff) but never states the formal definition of a satisfiable formula or of CNF. This file fills that gap from outside sources. It is NOT course material.
---

# External source: Boolean satisfiability

Paraphrased definitions with links. Not copied text. Outside the MIT course capture.

## Definitions

- **Literal:** a Boolean variable $x_i$ (positive literal) or its negation $\neg x_i$ (negative literal). [Wikipedia: Boolean satisfiability problem, "Conjunctive normal form"](https://en.wikipedia.org/wiki/Boolean_satisfiability_problem); [UIUC CS/ECE 374, Fall 2020, lecture 21.6, Definition 21.1](https://courses.grainger.illinois.edu/cs374/fa2020/lec_prerec/21/21_6_0_0.pdf)
- **Clause:** a disjunction (OR, $\vee$) of literals, e.g. $x_1 \vee x_2 \vee \neg x_4$. (same sources)
- **CNF (conjunctive normal form):** a conjunction (AND, $\wedge$) of clauses. (same sources)
- **3-CNF:** a CNF formula in which every clause has exactly 3 literals. **3-SAT** is the problem of deciding whether a given 3-CNF formula is satisfiable. (UIUC 21.6; [arXiv:2305.02659, Defs. 1–3](https://arxiv.org/pdf/2305.02659))
- **Satisfying assignment / satisfiable:** an assignment of 0/1 values to the variables *satisfies* a CNF formula when every clause has at least one literal made true. A formula is **satisfiable** when at least one such assignment exists, i.e. the formula evaluates to 1 (True). **SAT** is the decision problem "is this formula satisfiable?" (Wikipedia; [arXiv:math/0702261, §3.1](https://arxiv.org/pdf/math/0702261))
- **Connectives:** $\neg$ = NOT (flips the value of the variable it precedes: $\neg 0 = 1$, $\neg 1 = 0$), $\vee$ = OR, $\wedge$ = AND. Standard propositional-logic notation; the course legend agrees ([raw week 5](/mit-raw/week5.md), slide under line 3810).
- **Complexity:** SAT was the first problem proven NP-complete (Cook–Levin). Checking all assignments by truth table costs $O(2^n)$ for $n$ variables. ([Baeldung: Cook–Levin and 3-SAT](https://www.baeldung.com/cs/cook-levin-theorem-3sat))

## Relation to the course

The course's problem is **Exactly-1 3-SAT**, which is stricter than 3-SAT. Every clause must have *exactly one* true literal, not at least one. The course calls it "a variation of the well-known three-satisfiability problem" and says it is NP-hard (raw week 5, ~line 3836). A formula can be satisfiable as plain 3-SAT yet have no exactly-1 solution.
