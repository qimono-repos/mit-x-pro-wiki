---
title: Quiz and graded-question inventory
type: analysis
---

# Quiz and graded-question inventory

This page checks every graded item in the official QCFx2 outline (platform screenshot, 2026-11-09) against what is captured in `mit-raw/`. Everything is **due Dec 14, 2026, 8:30 PM GMT-3**. For the concept behind each question, see the [quiz → concept map](quiz-concept-map.md). Raw locations are `file:line`. Use the [course map](course-map.md) to translate raw weeks into official weeks.

**Result: 52 of 57 outline questions are captured.** The five that are missing were never in the source Google Docs, so nothing was lost in the vault build. The Post-Assessment is not captured either; it opens at the end of the course.

## Pre-Assessment: 9/9 ✓

`week2.md:5–175`. Questions Q1–Q9 cover cryptography schemes, the factoring reduction, post-quantum crypto, entanglement, teleportation, Hamiltonians, chemistry simulation, VQE and adiabatic QC. The capture shows the submitted answers (1.0/1.0 each). → [source](../sources/week-2-01-qiz-9-questions.md)

## Week 1: Modern Cryptography and Shor's Algorithm (9/10)

| Outline item | Expected | Captured | Raw |
|---|---|---|---|
| Modern Cryptography (CYU) | 1 | Q1 Encryption/Decryption Process ✓ | `week2.md:714` |
| RSA, Factoring, Shor (CYU) | 1 | Q1 RSA Key Generation (4 points) ✓ | `week2.md:1981` |
| ✭ Case Study: Demonstrations | 3 | Q1 Reduction of the Factorization Problem ✓ · **Q2 missing** · Q3 Trapped Ions ✓ | `week1.md:10103` |
| ✭ Week 1 Quiz | 5 | RSA Encryption · RSA Decryption · QFT II · QFT III · Period Finding ✓ | `week1.md:10141` |

Case-study Q2 is missing because the source doc has two screenshots (Q1, Q3). Its title is unknown; re-capture it from the platform.

## Week 2: Quantum Cryptography (12/12 ✓)

| Outline item | Expected | Captured | Raw |
|---|---|---|---|
| Post-Quantum Cryptography | 1 | Post-Quantum Cryptography ✓ | `week3.md:449` |
| Single Photon Schemes | 2 | Beam Splitters · The BB84 Protocol I ✓ | `week3.md:1592`, `3541` |
| Entangled Photon Schemes | 2 | Spontaneous Parametric Down-Conversion · The Ekert91 Protocol ✓ | `week3.md:5134`, `6551` |
| Random Number Generators | 1 | Bell's Inequality ✓ | `week3.md:8484` |
| Quantum Repeaters | 2 | Quantum Entanglement I · Quantum Repeaters ✓ | `week3.md:10133`, `11121` |
| ✭ Week 2 Quiz | 4 | BB84 Protocol II · Quantum Entanglement II · Quantum Teleportation · Half-Wave Plate ✓ | `week3.md:11138` |

Each page's PRACTICE heading sits at the end of the page in the capture, after the transcript. The SPDC question stem was split across two frames (`week3.md:5149`, "stem not in this frame").

## Week 3: Hamiltonian Simulation (11/12)

| Outline item | Expected | Captured | Raw |
|---|---|---|---|
| Introduction | 1 | Ultra-Cold Atoms ✓ | `week4.md:74` |
| Hamiltonian Simulation | 3 | Role of Hamiltonians · Particle in a Box · Trotterization ✓ | `week4.md:1080`, `2603`, `3160` |
| Quantum Simulation: Chemistry | 3 | Simulation of Chemistry Problems · Phase Estimation Algorithm · VQE ✓ | `week4.md:4012`, `5062`, `5782` |
| ✭ Reflect and Review Activity (1.5 h) | 1 | **missing**: no page in the capture | — |
| ✭ Week 3 Quiz | 4 | Quantum-Inspired Approximations · Ideas and Issues · Non-Commuting Terms · Evolution of a State ✓ | `week4.md:7773` |

The Week 3 quiz has no page title in the capture. It sits at the end of the [VQE in practice](../sources/week-4-07-vqe-in-practice.md) source note.

## Week 4: Quantum Optimization (11/14 incl. Lab)

| Outline item | Expected | Captured | Raw |
|---|---|---|---|
| Adiabatic Quantum Computing | 3 | Adiabatic QC I · Adiabatic QC II · **1 missing** | `week5.md:148`, `953` |
| Quantum Annealing & Polynomial-Speedup | 2 | **2 missing** | — |
| Digital Simulation: Grover's | 2 | Grover's Algorithm · How Many Qubits? N=512 ✓ | `week5.md:1874`, `5049` |
| ✭ Lab Practicum: Grover (IBM-Q) | 2 | Exactly-1 3-SAT Problem I · Syntax Error ✓ | `week5.md:3398`, `4904` |
| ✭ Week 4 Quiz | 5 | Adiabatic Evolution · Quantum Annealing III · Ising Model · Grover Operator · Exactly-1 3-SAT II ✓ | `week5.md:5070` |

The Week 4 source doc has only 6 PRACTICE blocks, against the 9 CYU questions in the outline. There is no separate "Quantum Annealing & Polynomial-Speedup" page in the capture; annealing appears only in the [introduction](../sources/week-5-01-introduction-to-quantum-optimization.md). The quiz is titled "Quantum Annealing **III**", which suggests the two missing CYUs are Annealing I and II. That is an inference from naming, not confirmed.

The pairing of the Grover/Lab rows is inferred from page order. The Exactly-1 3-SAT I question sits on the "Grover on the Quantum Experience" page.

## To re-capture from the platform

1. Week 1 Case Study, Q2
2. Week 3 Reflect and Review Activity
3. Week 4 Adiabatic QC, third CYU
4. Week 4 Quantum Annealing & Polynomial-Speedup page (whole page + 2 CYUs)
5. Post-Assessment (at course end)
