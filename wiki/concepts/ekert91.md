---
title: Ekert 91 and BBM92
type: concept
---

# Ekert 91 and BBM92

Ekert's protocol (E91) distributes a key from entangled pairs rather than from states Alice prepared. A source sends one qubit of a Bell pair to Alice and the other to Bob. They measure in randomly chosen bases. The bits from matching bases become the raw key. The bits from mismatched bases are used to estimate a [[concepts/bell-inequality]] violation, which certifies that the correlations were not produced by an eavesdropper who holds a classical description of both qubits. ^e91-protocol

**Course specifics.** E91 needs an entangled source (BB84 does not). The source can be trusted and run by Alice or Bob themselves, so the protocol has two parties, not three. It needs no Bell-state *measurement*: each side does ordinary single-photon polarization measurements. The course's version uses the singlet $|\Psi^-\rangle$ and three analyzer settings per side. The mismatched-setting results are published to evaluate CHSH: $S = -2\sqrt2$ for an intact channel, against the classical bound $|S| \le 2$ ([raw week 3](/mit-raw/week3.md), Ekert91 Learn, ~lines 6420–7390). ^e91-course-specifics

BBM92 (Bennett, Brassard, Mermin) is the entanglement version of [[concepts/bb84]]: the same two bases, without the full CHSH estimation, relying on the monogamy of entanglement plus the sampled error rate.

The course also discusses practical entangled-photon sources and detectors in the same week.

## Sources

- [Ekert91 and BBM92](../sources/week-3-04-quantum-key-distribution-ekert91-and-bbm92.md)
- Raw: [week 3](/mit-raw/week3.md)
