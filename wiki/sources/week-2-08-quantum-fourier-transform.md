---
title: "Quantum Fourier Transform"
type: source
week: 2
raw: mit-raw/week2.md
---

# Quantum Fourier Transform

Source page from week 2. [Raw week 2](/mit-raw/week2.md)

## Learn

**The following reading is optional for learners who want to learn a bit
more about the Quantum Fourier Transform (QFT).**

The Quantum Fourier Transform (QFT) is a critical operation used in
quantum computing protocols including period finding and phase
estimation. For example, in the period finding protocol, the input state
encodes a sequence with an underlying periodic structure, and, following
the application of the QFT, the output encodes the period of the
sequence.

The QFT is a unitary linear transformation implemented with a series of
quantum gates. It maps an -qubit quantum state as

{width="3.1458333333333335in"
height="0.7708333333333334in"}

where is a constant defined by the number of qubits , and and go from 0
to .

Note that the input quantum state can be written as where is a decimal
number spanning to (as above), or, equivalently, it can be written as a
binary number , where each take the value 0 or 1. As short-hand
notation, this is sometimes written as the decimal value, e.g. or .

In addition to knowing the mapping of the Quantum Fourier Transform, you
also need to know how to implement it. For a single-qubit, the mapping
of the QFT is:

{width="6.5in"
height="4.319444444444445in"}

{width="6.5in"
height="6.361111111111111in"}

The figure below shows a graphical representation of the Quantum Fourier
Transform for an n-qubit system.

{width="3.8541666666666665in"
height="3.3333333333333335in"}

To understand how this new representation works, let\'s go back to the
example. The table below shows the output state corresponding to each of
the values of and . Note, that these states are all written in the
single-qubit basis {\|00\>\|01\>\|10\>\|11\>}

{width="6.5in"
height="7.625in"}

{width="6.5in"
height="3.3194444444444446in"}

{width="5.364583333333333in"
height="2.3333333333333335in"}

{width="6.5in"
height="7.527777777777778in"}

{width="6.5in"
height="1.9305555555555556in"}

However, the output states in equations (2) and (3) are not equal. The
output state of the first qubit in (2) is equivalent to the output state
of the last qubit in (3). The output state of the second qubit in (2) is
equivalent to the output state of the penultimate qubit in (3). The
state of qubit in (3) should be the state of the first qubit in (2), the
state of qubit in (3) should be the state of the second qubit (2), and
so on. To return the qubit states to their original ordering, we need to
apply swap-gates, which are generally used to exchange qubit states.
Thus, the difference between the output states in equations (2) and (3)
can be straightforwardly undone by applying a swap gate between qubits
\"1\" and \"n\", a swap gate between qubits \"2\" and \"n-1\", a swap
gate between qubits \"3\" and \"n-2\", and so on.

## Notes for the wiki

- Frames from this page's video were moved next to the matching SRT cue in the raw file when a player timestamp was read.
- Equations are display math (`$$...$$`). Diagrams may still be an image plus a text description.
- This page is immutable source commentary. Synthesis belongs in `wiki/concepts/`.
