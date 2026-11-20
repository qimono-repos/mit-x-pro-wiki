---
title: Quantum teleportation
type: concept
---

# Quantum teleportation

Teleportation moves an unknown qubit state from Alice to Bob using one shared Bell pair and two classical bits. It does not move the physical qubit, and it does not allow faster-than-light signaling: Bob's half of the pair is maximally mixed until the two classical bits arrive.

## Protocol

Shared resource $|\Phi^+\rangle = (|00\rangle + |11\rangle)/\sqrt{2}$. Alice holds $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$ and her half of the pair.

1. Alice applies CNOT from $|\psi\rangle$ onto her half of the pair, then a Hadamard on $|\psi\rangle$.
2. She measures both of her qubits, getting two bits $m_1 m_0$.
3. She sends those bits to Bob.
4. Bob applies $X^{m_0} Z^{m_1}$ (the Pauli named by the bits) to his qubit and holds $|\psi\rangle$.

The unknown state is destroyed on Alice's side by the measurement, which is why the protocol does not clone. Week 3 presents this next to QKD because both spend entanglement as a resource.

## Sources

- [Quantum teleportation](../sources/week-3-08-quantum-teleportation.md)
- Raw: [week 3](/mit-raw/week3.md)
