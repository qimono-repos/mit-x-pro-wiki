---
title: Trotterization
type: concept
---

# Trotterization

Trotterization approximates the exponential of a sum by a product of exponentials. For $H = \sum_\ell H_\ell$,

$$
e^{-iHt} = \Bigl(\prod_\ell e^{-i H_\ell t/n}\Bigr)^n + O(t^2/n),
$$

the first-order Lie–Trotter formula. Each $e^{-i H_\ell \Delta t}$ is easy when $H_\ell$ is a Pauli string or another local term: it is a small circuit of basis changes and a diagonal phase. Raising $n$ (more slices) shrinks the error. Higher-order product formulas cancel more commutators and reduce the number of slices needed for a given $\varepsilon$. ^trotter-formula

This is the concrete algorithm the course uses for [[concepts/hamiltonian-simulation]] before it introduces [[concepts/phase-estimation]] and [[concepts/vqe]] as ways to read energies out.

## Why it's needed: non-commuting terms

If $H_1H_2 \ne H_2H_1$, then $e^{-i(H_1+H_2)t} \ne e^{-iH_1t}e^{-iH_2t}$. The **exact** evolution is $|\psi(t)\rangle = e^{-i(H_1+H_2)t/\hbar}|\psi(0)\rangle$, and either product order is only an approximation (raw week 4, Trotterization CYU stem, ~line 3160). The course's Trotter limit:

$$
e^{-i(H_1+H_2)t} = \lim_{n\to\infty}\left(e^{-iH_1 t/n}\,e^{-iH_2 t/n}\right)^n
$$

^exact-vs-product


**Geometric picture (the course's cow).** Rotations about the *same* axis commute: 90° then 45° about $x$ equals 45° then 90°. Rotations about *different* axes generally don't: 90° about $x$ then about $y$ lands the object differently from the reverse order (raw week 4, quiz Q3, ~line 7817). Operators behave the same way. ^non-commuting-rotations

## Sources

- [Hamiltonian simulation: Trotterization](../sources/week-4-03-hamiltonian-simulation-trotterization.md)
- Raw: [week 4](/mit-raw/week4.md)
