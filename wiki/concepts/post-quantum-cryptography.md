---
title: Post-quantum cryptography
type: concept
aliases: [PQC, quantum-safe cryptography, Mosca's theorem, x + y > z]
---

# Post-quantum cryptography

Post-quantum (quantum-safe) cryptography means classical public-key schemes built on problems that quantum computers are not known to solve efficiently. The urgency comes from timing, not from today's hardware: data encrypted now can be recorded now and decrypted later.

## Why care before the quantum computer exists

Shor's algorithm breaks the one-way functions behind asymmetric cryptography. Once a large enough quantum computer exists, it could reveal information *previously* encrypted with today's most common public-key schemes. Symmetric-key schemes are "not thought to be at catastrophic risk" ([source note](../sources/week-3-01a-post-quantum-cryptography.md); raw week 3, ~line 380). ^why-now

**Mosca's inequality.** Let $x$ = how long the data must stay secret (security shelf-life), $y$ = how long it takes to migrate to new crypto, $z$ = time until a quantum computer can break the current scheme (collapse time). If $x + y \ge z$, then worry: some data will become readable while it still matters (raw week 3, Michele Mosca video, ~line 400). ^mosca-inequality

## What's being done

NIST and the NSA advocated acting now. In 2016 NIST began requesting nominations for post-quantum public-key algorithms, aiming to standardize one or more. The two schemes the course highlights as most promising are **lattice-based** and **code-based** cryptography. QKD ([[concepts/bb84]], [[concepts/ekert91]]) is the *other* route: security from physics rather than from computational hardness. ^pqc-response

> **Data gap:** Mosca's quoted odds for breaking RSA-2048 lost their numbers in the Doc export ("constructed by and at and respectively"). Re-check them on the platform; don't fill them in from memory.

## Sources

- [Post-quantum cryptography](../sources/week-3-01a-post-quantum-cryptography.md)
- See [[concepts/rsa-cryptosystem]], [[concepts/shors-algorithm]], [[concepts/modern-cryptography]]
