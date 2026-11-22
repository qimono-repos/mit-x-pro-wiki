---
title: "Post-Quantum Cryptography"
type: source
week: 3
raw: mit-raw/week3.md
raw_line: 372
---

# Post-Quantum Cryptography

Source page from raw week 3, line 372. Official Week 2 · "Post-Quantum Cryptography (15 min) (1 Question)". [Raw week 3](/mit-raw/week3.md)

This page had a blank or level-2 `Page Title` in the capture, so the first build skipped it. Added by the 2026-11-21 lint pass.

## Learn

Post-Quantum Cryptography

The long-term security of modern cryptographic systems has been brought
into question by developments in quantum computing. The existence of
Shor\'s factoring algorithm shows that the inversion of the one-way
functions needed for asymmetric cryptography is an instance where
quantum computers have quantum advantage over classical algorithms. It
is worth noting that the development of quantum computers is not thought
to be catastrophic for symmetric-key cryptography schemes.

Based on the pace of quantum computing research, and the effort required
to update cryptographic standards, it has been argued by researchers
that the process of finding and implementing algorithms which are
suitably robust to quantum computers should begin immediately. Professor
Michele Mosca, a leading expert in quantum computing research, has
estimated the odds of a quantum computer capable of breaking RSA-2048 --
an RSA cryptosystem using 2048-bit private and public keys -- being
constructed by and at and respectively. These probabilities are informed
estimates based on of several parameters such as when a fault-tolerant
and scalable qubit will be designed, how many qubits are needed to break
RSA-2048, and how long it will take to scale quantum computers to this
size.

_(excerpt — continue in the raw file)_

## Related concepts

- [[concepts/shors-algorithm]]

## Notes for the wiki

- Equations are display math (`$$...$$`). Diagrams may still be an image plus a text description.
- This page is source commentary. Synthesis belongs in `wiki/concepts/`.
