---
title: Quantum teleportation
type: concept
---

# Quantum teleportation

Teleportation moves an unknown qubit state from Alice to Bob using one shared Bell pair and two classical bits. It does not move the physical qubit, and it does not allow faster-than-light signaling: Bob's half of the pair is maximally mixed until the two classical bits arrive. ^summary

## Protocol

Shared resource $|\Phi^+\rangle = (|00\rangle + |11\rangle)/\sqrt{2}$. Alice holds $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$ and her half of the pair.

1. Alice applies CNOT from $|\psi\rangle$ onto her half of the pair, then a Hadamard on $|\psi\rangle$.
2. She measures both of her qubits, getting two bits $m_1 m_0$.
3. She sends those bits to Bob.
4. Bob applies $X^{m_0} Z^{m_1}$ (the Pauli named by the bits) to his qubit and holds $|\psi\rangle$.

The unknown state is destroyed on Alice's side by the measurement, which is why the protocol does not clone. ^no-clone-no-photon-sent

**The photonic version in the course.** An entangled source gives photon A to Alice and B to Bob (pre-shared Bell pair). Alice does a **Bell-state measurement** on A and her input photon C, projecting the pair onto one of the four Bell states (with a beam splitter and two detectors). She sends the outcome over a **classical channel**. Bob applies the matching **rotation/decoding** to photon B, which then carries $|\psi\rangle$. Alice never sends a photon to Bob ([raw week 3](/mit-raw/week3.md), teleportation page and quiz Q3 diagram, ~line 11206). Week 3 presents this next to QKD because both spend entanglement as a resource. ^photonic-teleportation

## Sources

- [Quantum teleportation](../sources/week-3-08-quantum-teleportation.md)
- Raw: [week 3](/mit-raw/week3.md)
