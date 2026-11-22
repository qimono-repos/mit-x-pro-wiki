---
title: OpenQASM (IBM Quantum composer code)
type: concept
aliases: [QASM, qelib1.inc, qreg, creg, IBM composer]
---

# OpenQASM

OpenQASM is the text form of circuits in IBM's composer. The Week 4 lab uses its 2.0 dialect to build Grover's algorithm. Its syntax is small; the course's first rule is that every statement ends in a semicolon.

## The course's minimal program

```
include "qelib1.inc";   // load the standard gate library (x, y, z, h, cx, ...)
qreg q[5];              // quantum register of 5 qubits
creg c[5];              // classical register of 5 bits
// This is a comment
measure q[0] -> c[0];   // measure qubit 0 into bit 0
```

Course notes for each line: line 1 includes all gates in the quantum gate library, and "**each line has to end in a semicolon ";"**". Line 2 defines a 5-qubit quantum register (you may use 1–5). The classical register holds measurement results ([raw week 5](/mit-raw/week5.md), lab practicum, ~line 4849). ^qasm-syntax

## Access note

IBM now requires each learner to have their own IBM Quantum account; the shared MIT xPRO access was removed. The lab points to IBM's composer and tutorials ([lab Learn](../sources/week-5-06-lab-practicum-grover-s-algorythm.md)). ^ibm-access

## Sources

- [Lab practicum: Grover's algorithm](../sources/week-5-06-lab-practicum-grover-s-algorythm.md)
- See [[concepts/grovers-algorithm]], [[concepts/exactly-1-3-sat]]
