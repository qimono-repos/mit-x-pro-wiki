---
title: Quiz → concept map
type: analysis
---

# Quiz → concept map

Every graded question in the course capture, linked to the **exact paragraph** of the concept page that teaches what it tests. Links use Obsidian block references (`[[concepts/x#^block]]`), so they land on the paragraph, not the top of the page. **No answers are stored here:** the repo is public. Work the question, then open the linked paragraph to check your reasoning.

Coverage: **52 captured questions, all mapped**; 4 rows are missing from the capture (see [quiz inventory](quiz-inventory.md)). Official week numbers are used; raw files follow the [course map](course-map.md). Due **Dec 14, 2026, 8:30 PM GMT-3**.


## Pre-Assessment

| Question | Raw | Concepts (targeted) | Note |
|---|---|---|---|
| Q1 Modern Cryptography Schemes | [week2.md:19](/mit-raw/week2.md) | [[concepts/modern-cryptography#^cipher-terms\|cipher, plaintext, ciphertext]] · [[concepts/modern-cryptography#^hybrid-in-practice\|symmetric + public key in practice]] · [[concepts/modern-cryptography#^qkd-role\|what QKD is for]] |  |
| Q2 Reduction of the Factorization Problem | [week2.md:33](/mit-raw/week2.md) | [[concepts/shors-algorithm#^reduction-summary\|factoring → order finding]] · [[concepts/period-finding\|period finding]] |  |
| Q3 Post-Quantum Cryptography | [week2.md:47](/mit-raw/week2.md) | [[concepts/post-quantum-cryptography#^why-now\|why care now]] · [[concepts/post-quantum-cryptography#^mosca-inequality\|x + y ≥ z]] |  |
| Q4 Quantum Entanglement | [week2.md:63](/mit-raw/week2.md) | [[concepts/photon-polarization-qubits#^entangled-pair-measurement\|measuring one photon of a Bell pair]] · [[concepts/photon-polarization-qubits#^polarizer-measurement\|polarizer as measurement]] |  |
| Q5 Quantum Teleportation | [week2.md:83](/mit-raw/week2.md) | [[concepts/quantum-teleportation#^photonic-teleportation\|photonic protocol]] · [[concepts/quantum-teleportation#^no-clone-no-photon-sent\|no cloning, no photon sent]] |  |
| Q6 The Role of Hamiltonians in Quantum Mechanics | [week2.md:109](/mit-raw/week2.md) | [[concepts/hamiltonian-simulation#^what-is-a-hamiltonian\|what a Hamiltonian is]] |  |
| Q7 Simulation of Chemistry Problems | [week2.md:128](/mit-raw/week2.md) | [[concepts/quantum-chemistry#^molecular-hamiltonian\|molecular Hamiltonian]] · [[concepts/quantum-chemistry#^known-but-unsolved\|known but unsolved]] · [[concepts/quantum-chemistry#^haber-bosch-nitrogenase\|Haber–Bosch vs nitrogenase]] |  |
| Q8 Variational Quantum Eigensolver | [week2.md:148](/mit-raw/week2.md) | [[concepts/vqe#^hybrid-loop\|quantum vs classical steps]] |  |
| Q9 Adiabatic Quantum Computing | [week2.md:164](/mit-raw/week2.md) | [[concepts/adiabatic-quantum-computing#^definition\|definition, adiabatic theorem]] |  |

## Week 1 · Modern Cryptography and Shor's Algorithm

| Question | Raw | Concepts (targeted) | Note |
|---|---|---|---|
| CYU · Q1 Encryption/Decryption Process | [week2.md:714](/mit-raw/week2.md) | [[concepts/modern-cryptography#^cipher-terms\|cipher terms]] · [[concepts/modern-cryptography#^hybrid-in-practice\|what e-commerce uses]] · [[concepts/modern-cryptography#^qkd-role\|what QKD is for]] | Modern Cryptography page |
| CYU · Q1 RSA Key Generation (4 pts) | [week2.md:1981](/mit-raw/week2.md) | [[concepts/rsa-cryptosystem#^key-generation\|five key-generation steps]] · [[concepts/rsa-cryptosystem#^modular-inverse\|e⁻¹ mod r]] · [[concepts/rsa-cryptosystem\|worked example (own numbers)]] | RSA page |
| Case Study · Q1 Reduction of the Factorization Problem | [week1.md:10109](/mit-raw/week1.md) | [[concepts/shors-algorithm#^reduction-summary\|factoring → order finding]] |  |
| Case Study · Q2 (not captured) | — | — | Re-capture from the platform. |
| Case Study · Q3 Trapped Ions | [week1.md:10124](/mit-raw/week1.md) | [[concepts/shor-demonstrations#^trapped-ions-2016\|Kitaev QFT, recycling, ion count]] |  |
| Quiz · Q1 RSA Encryption | [week1.md:10153](/mit-raw/week1.md) | [[concepts/rsa-cryptosystem#^encrypt-decrypt\|c = mᵉ mod N]] |  |
| Quiz · Q2 RSA Decryption | [week1.md:10170](/mit-raw/week1.md) | [[concepts/rsa-cryptosystem#^key-generation\|compute r, then d]] · [[concepts/rsa-cryptosystem#^modular-inverse\|e⁻¹ mod r]] · [[concepts/rsa-cryptosystem#^encrypt-decrypt\|m = cᵈ mod N]] |  |
| Quiz · Q3 Quantum Fourier Transform II | [week1.md:10187](/mit-raw/week1.md) | [[concepts/quantum-fourier-transform#^binary-fraction-phases\|binary-fraction phases φₘ]] |  |
| Quiz · Q4 Quantum Fourier Transform III | [week1.md:10212](/mit-raw/week1.md) | [[concepts/quantum-fourier-transform#^two-qubit-circuit\|2-qubit QFT circuit]] |  |
| Quiz · Q5 Period Finding Algorithm | [week1.md:10228](/mit-raw/week1.md) | [[concepts/period-finding#^circuit-roles\|role of each stage]] · [[concepts/period-finding#^first-qft-is-hadamard\|first QFT = Hadamards]] |  |

## Week 2 · Quantum Cryptography

| Question | Raw | Concepts (targeted) | Note |
|---|---|---|---|
| CYU · Q1 Post-Quantum Cryptography | [week3.md:447](/mit-raw/week3.md) | [[concepts/post-quantum-cryptography#^why-now\|why care now]] · [[concepts/post-quantum-cryptography#^mosca-inequality\|x + y ≥ z]] |  |
| CYU · Q1 Beam Splitters | [week3.md:1590](/mit-raw/week3.md) | [[concepts/photon-sources-and-detectors#^beam-splitters\|50:50 vs polarizing BS]] | Single-photon schemes |
| CYU · Q1 The BB84 Protocol I | [week3.md:3539](/mit-raw/week3.md) | [[concepts/bb84#^polarization-sifting\|sifting + bit convention]] · [[concepts/bb84#^sifting\|sifting in general]] | Single-photon schemes |
| CYU · Q1 Spontaneous Parametric Down-Conversion | [week3.md:5132](/mit-raw/week3.md) | [[concepts/photon-sources-and-detectors#^spdc-basics\|SPDC basics]] · [[concepts/photon-sources-and-detectors#^spdc-types\|type I vs type II]] · [[concepts/photon-polarization-qubits#^entangled-pair-measurement\|what detecting one photon does]] | Entangled-photon schemes |
| CYU · Q1 The Ekert91 Protocol | [week3.md:6549](/mit-raw/week3.md) | [[concepts/ekert91#^e91-course-specifics\|parties, source, no Bell measurement, CHSH]] · [[concepts/ekert91#^e91-protocol\|protocol]] | Entangled-photon schemes |
| CYU · Q1 Bell's Inequality | [week3.md:8482](/mit-raw/week3.md) | [[concepts/bell-inequality#^local-realism\|local realism]] · [[concepts/bell-inequality#^loopholes\|locality / free-choice / detection loopholes]] | Random number generators |
| CYU · Q1 Quantum Entanglement I | [week3.md:10131](/mit-raw/week3.md) | [[concepts/photon-polarization-qubits#^entangled-pair-measurement\|Alice's H polarizer → Bob's state]] · [[concepts/photon-polarization-qubits#^polarizer-measurement\|±45° polarizer on H]] | Quantum repeaters unit |
| CYU · Q1 Quantum Repeaters | [week3.md:11119](/mit-raw/week3.md) | [[concepts/quantum-repeaters#^repeater-idea\|entanglement as resource]] · [[concepts/quantum-repeaters#^fiber-loss\|loss ∝ distance (dB)]] · [[concepts/quantum-repeaters#^no-amplification\|why no amplifiers]] | Quantum repeaters unit |
| Quiz · Q1 BB84 Protocol II | [week3.md:11146](/mit-raw/week3.md) | [[concepts/bb84#^polarization-sifting\|sifting + bit convention]] |  |
| Quiz · Q2 Quantum Entanglement II | [week3.md:11179](/mit-raw/week3.md) | [[concepts/photon-polarization-qubits#^entangled-pair-measurement\|Alice's V polarizer → Bob's state]] · [[concepts/photon-polarization-qubits#^polarizer-measurement\|±45° polarizer on V]] |  |
| Quiz · Q3 Quantum Teleportation | [week3.md:11206](/mit-raw/week3.md) | [[concepts/quantum-teleportation#^photonic-teleportation\|photonic protocol]] · [[concepts/quantum-teleportation#^no-clone-no-photon-sent\|nothing physical sent]] |  |
| Quiz · Q4 Half-Wave Plate | [week3.md:11241](/mit-raw/week3.md) | [[concepts/photon-polarization-qubits#^polarization-mapping\|H/V ↔ 0/1, diagonals]] · [[concepts/photon-polarization-qubits#^half-wave-plate\|HWP matrix vs Z, H, X]] |  |

## Week 3 · Hamiltonian Simulation

| Question | Raw | Concepts (targeted) | Note |
|---|---|---|---|
| CYU · Q1 Ultra-Cold Atoms | [week4.md:74](/mit-raw/week4.md) | [[concepts/quantum-simulation#^analog-deformation\|BEC, time-averaged Hamiltonians]] · [[concepts/quantum-simulation#^quantum-inspired\|MERA/PEPS are classical methods]] | Introduction |
| CYU · Q1 The Role of Hamiltonians | [week4.md:1080](/mit-raw/week4.md) | [[concepts/hamiltonian-simulation#^what-is-a-hamiltonian\|what a Hamiltonian is]] | Hamiltonian simulation |
| CYU · Q1 Particle in a Box | [week4.md:2603](/mit-raw/week4.md) | [[concepts/hamiltonian-simulation#^particle-in-a-box\|wavefunction, kinetic + potential, discretize]] | Hamiltonian simulation |
| CYU · Q1 Trotterization | [week4.md:3160](/mit-raw/week4.md) | [[concepts/trotterization#^exact-vs-product\|exact vs product]] · [[concepts/trotterization#^trotter-formula\|Trotter formula]] | Hamiltonian simulation |
| CYU · Q1 Simulation of Chemistry Problems | [week4.md:4012](/mit-raw/week4.md) | [[concepts/quantum-chemistry#^molecular-hamiltonian\|all five terms]] · [[concepts/quantum-chemistry#^known-but-unsolved\|known but unsolved]] · [[concepts/quantum-chemistry#^haber-bosch-nitrogenase\|room-temperature enzymes]] | Chemistry |
| CYU · Q1 Phase Estimation Algorithm | [week4.md:5062](/mit-raw/week4.md) | [[concepts/phase-estimation#^precision\|estimate, not exact]] · [[concepts/phase-estimation#^uses\|QFT, subroutine of Shor]] | Chemistry |
| CYU · Q1 Variational Quantum Eigensolver | [week4.md:5782](/mit-raw/week4.md) | [[concepts/vqe#^hybrid-loop\|quantum vs classical steps]] | Chemistry |
| Reflect and Review Activity (not captured) | — | — | Re-capture from the platform. |
| Quiz · Q1 Quantum-Inspired Approximations | [week4.md:7777](/mit-raw/week4.md) | [[concepts/quantum-simulation#^quantum-inspired\|DMRG first, then PEPS/MERA]] |  |
| Quiz · Q2 Ideas and Issues of Quantum Simulation | [week4.md:7798](/mit-raw/week4.md) | [[concepts/quantum-simulation#^ideas-and-issues\|Chuang's list]] · [[concepts/quantum-simulation#^analog-deformation\|analog deformation]] · [[concepts/quantum-simulation#^quantum-inspired\|DMRG]] |  |
| Quiz · Q3 Non-Commuting Terms | [week4.md:7817](/mit-raw/week4.md) | [[concepts/trotterization#^non-commuting-rotations\|cow rotations]] |  |
| Quiz · Q4 Evolution of a State | [week4.md:7878](/mit-raw/week4.md) | [[concepts/trotterization#^exact-vs-product\|exact evolution]] |  |

## Week 4 · Quantum Optimization

| Question | Raw | Concepts (targeted) | Note |
|---|---|---|---|
| CYU · Q1 Adiabatic Quantum Computation I | [week5.md:148](/mit-raw/week5.md) | [[concepts/adiabatic-quantum-computing#^definition\|definition, universality]] · [[concepts/adiabatic-quantum-computing#^interpolation\|time-dependent H(t)]] | Adiabatic QC |
| CYU · Q1 Adiabatic Quantum Computation II | [week5.md:953](/mit-raw/week5.md) | [[concepts/adiabatic-quantum-computing#^minimum-gap\|minimum gap, Landau–Zener]] · [[concepts/adiabatic-quantum-computing#^gap-strategies\|what helps, what doesn't]] | Adiabatic QC |
| Adiabatic QC · 3rd CYU (not captured) | — | — | Re-capture. |
| Quantum Annealing · CYU I and II (not captured) | — | — | Page and questions missing. |
| CYU · Q1 Quantum Annealing II | [expert-view transcript](/mit-raw/week5-quantum-annealing-expert-view.md) (question from eDX screenshot) | [[concepts/quantum-annealing#^thermal-excitation\|thermal excitation vs gap]] · [[concepts/adiabatic-quantum-computing#^minimum-gap\|Landau–Zener is a speed effect]] |  |
| CYU · Q1 Grover's Algorithm | [week5.md:1874](/mit-raw/week5.md) | [[concepts/grovers-algorithm#^register-size\|n = log₂N qubits]] · [[concepts/grovers-algorithm#^two-reflections\|two reflections]] · [[concepts/grovers-algorithm#^iteration-bound\|π/4·√(N/M)]] | Digital simulation: Grover |
| CYU · Q1 How Many Qubits? N=512 | [week5.md:5049](/mit-raw/week5.md) | [[concepts/grovers-algorithm#^register-size\|n = log₂N qubits]] | Digital simulation: Grover |
| CYU · Q1 Exactly-1 3-SAT Problem I | [week5.md:3396](/mit-raw/week5.md) | [[concepts/exactly-1-3-sat#^definitions\|clause, literal]] · [[concepts/exactly-1-3-sat#^truth-table\|truth table]] · [[concepts/exactly-1-3-sat#^clause-subcircuit\|per-clause subcircuit]] | Lab |
| CYU · Q1 Syntax Error | [week5.md:4904](/mit-raw/week5.md) | [[concepts/openqasm#^qasm-syntax\|QASM line rules]] | Lab |
| Quiz · Q1 Adiabatic Evolution | [week5.md:5076](/mit-raw/week5.md) | [[concepts/adiabatic-quantum-computing#^minimum-gap\|Landau–Zener, thermal noise, coherence]] · [[concepts/quantum-annealing#^thermal-excitation\|thermal photons]] |  |
| Quiz · Q2 Quantum Annealing III | [week5.md:5095](/mit-raw/week5.md) | [[concepts/quantum-annealing#^tunneling-relaxation\|tunneling + relaxation]] · [[concepts/quantum-annealing#^no-enhancement-evidence\|no enhancement shown]] · [[concepts/quantum-annealing#^encoding-and-gap\|Ising encoding, gap vs speed]] |  |
| Quiz · Q3 AQC: Ising Model | [week5.md:5119](/mit-raw/week5.md) | [[concepts/adiabatic-quantum-computing#^ising\|Ising energies]] |  |
| Quiz · Q4 Grover Operator | [week5.md:5159](/mit-raw/week5.md) | [[concepts/grovers-algorithm#^two-reflections\|two reflections, |ψ⟩]] · [[concepts/grovers-algorithm#^iteration-bound\|bound]] |  |
| Quiz · Q5 Exactly-1 3-SAT Problem II | [week5.md:5180](/mit-raw/week5.md) | [[concepts/exactly-1-3-sat#^definitions\|3-SAT definitions]] | Course gap: 'satisfiable' → [external source](/mit-raw/external/boolean-satisfiability.md) |

## Reverse index: which questions test each concept

- [[concepts/adiabatic-quantum-computing]] (5): Pre Q9 Adiabatic Quantum Computing; Week 4 CYU · Q1 Adiabatic Quantum Computation I; Week 4 CYU · Q1 Adiabatic Quantum Computation II; Week 4 Quiz · Q1 Adiabatic Evolution; Week 4 Quiz · Q3 AQC: Ising Model
- [[concepts/bb84]] (2): Week 2 CYU · Q1 The BB84 Protocol I; Week 2 Quiz · Q1 BB84 Protocol II
- [[concepts/bell-inequality]] (1): Week 2 CYU · Q1 Bell's Inequality
- [[concepts/ekert91]] (1): Week 2 CYU · Q1 The Ekert91 Protocol
- [[concepts/exactly-1-3-sat]] (2): Week 4 CYU · Q1 Exactly-1 3-SAT Problem I; Week 4 Quiz · Q5 Exactly-1 3-SAT Problem II
- [[concepts/grovers-algorithm]] (3): Week 4 CYU · Q1 Grover's Algorithm; Week 4 CYU · Q1 How Many Qubits? N=512; Week 4 Quiz · Q4 Grover Operator
- [[concepts/hamiltonian-simulation]] (3): Pre Q6 The Role of Hamiltonians in Quantum Mechanics; Week 3 CYU · Q1 The Role of Hamiltonians; Week 3 CYU · Q1 Particle in a Box
- [[concepts/modern-cryptography]] (2): Pre Q1 Modern Cryptography Schemes; Week 1 CYU · Q1 Encryption/Decryption Process
- [[concepts/openqasm]] (1): Week 4 CYU · Q1 Syntax Error
- [[concepts/period-finding]] (2): Pre Q2 Reduction of the Factorization Problem; Week 1 Quiz · Q5 Period Finding Algorithm
- [[concepts/phase-estimation]] (1): Week 3 CYU · Q1 Phase Estimation Algorithm
- [[concepts/photon-polarization-qubits]] (5): Pre Q4 Quantum Entanglement; Week 2 CYU · Q1 Spontaneous Parametric Down-Conversion; Week 2 CYU · Q1 Quantum Entanglement I; Week 2 Quiz · Q2 Quantum Entanglement II; Week 2 Quiz · Q4 Half-Wave Plate
- [[concepts/photon-sources-and-detectors]] (2): Week 2 CYU · Q1 Beam Splitters; Week 2 CYU · Q1 Spontaneous Parametric Down-Conversion
- [[concepts/post-quantum-cryptography]] (2): Pre Q3 Post-Quantum Cryptography; Week 2 CYU · Q1 Post-Quantum Cryptography
- [[concepts/quantum-annealing]] (3): Week 4 CYU · Q1 Quantum Annealing II; Week 4 Quiz · Q1 Adiabatic Evolution; Week 4 Quiz · Q2 Quantum Annealing III
- [[concepts/quantum-chemistry]] (2): Pre Q7 Simulation of Chemistry Problems; Week 3 CYU · Q1 Simulation of Chemistry Problems
- [[concepts/quantum-fourier-transform]] (2): Week 1 Quiz · Q3 Quantum Fourier Transform II; Week 1 Quiz · Q4 Quantum Fourier Transform III
- [[concepts/quantum-repeaters]] (1): Week 2 CYU · Q1 Quantum Repeaters
- [[concepts/quantum-simulation]] (3): Week 3 CYU · Q1 Ultra-Cold Atoms; Week 3 Quiz · Q1 Quantum-Inspired Approximations; Week 3 Quiz · Q2 Ideas and Issues of Quantum Simulation
- [[concepts/quantum-teleportation]] (2): Pre Q5 Quantum Teleportation; Week 2 Quiz · Q3 Quantum Teleportation
- [[concepts/rsa-cryptosystem]] (3): Week 1 CYU · Q1 RSA Key Generation (4 pts); Week 1 Quiz · Q1 RSA Encryption; Week 1 Quiz · Q2 RSA Decryption
- [[concepts/shor-demonstrations]] (1): Week 1 Case Study · Q3 Trapped Ions
- [[concepts/shors-algorithm]] (2): Pre Q2 Reduction of the Factorization Problem; Week 1 Case Study · Q1 Reduction of the Factorization Problem
- [[concepts/trotterization]] (3): Week 3 CYU · Q1 Trotterization; Week 3 Quiz · Q3 Non-Commuting Terms; Week 3 Quiz · Q4 Evolution of a State
- [[concepts/vqe]] (2): Pre Q8 Variational Quantum Eigensolver; Week 3 CYU · Q1 Variational Quantum Eigensolver

## Notes

- Raw links point to the line in `mit-raw/` where the question starts. Raw files are immutable, so the links run quiz → concept. To see the questions for a concept, use the reverse index above or Obsidian's backlinks pane.
- Several concept pages were created or extended on 2026-11-22 specifically so every question had a precise target. Lines marked *Background* or *own reasoning* on those pages are not course content.
- Table pipes in Obsidian links are escaped as `\|` so the aliases render inside tables.
