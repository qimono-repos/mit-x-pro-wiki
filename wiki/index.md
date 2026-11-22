# Index

Content catalog for the MIT xPRO **QCFx2** LLM wiki (*Quantum Algorithms for Cybersecurity, Chemistry, and Optimization*). Raw file numbers are not the official week numbers. See the [course map](analyses/course-map.md). Read this first when answering a question, then open the linked pages.

## How this vault is organized

- `mit-raw/` — immutable course capture (Learn prose, SRT transcripts, slides as LaTeX or images).
- `wiki/sources/` — one note per course page, pointing at the raw week file.
- `wiki/concepts/` — synthesized topic pages. The LLM owns this layer.
- `wiki/log.md` — append-only ingest / query / lint log.

## Concepts

| Page | Summary |
|---|---|
| [RSA cryptosystem](concepts/rsa-cryptosystem.md) | Public-key crypto on a one-way function: $c=m^e \bmod N$, $d=e^{-1} \bmod (p-1)(q-1)$; breaks if $N$ can be factored. |
| [Shor's algorithm](concepts/shors-algorithm.md) | Factoring reduced to order finding, then solved by quantum period finding. |
| [Period finding](concepts/period-finding.md) | Quantum subroutine that estimates the period of $f(x) = a^x \bmod N$. |
| [Simon's algorithm](concepts/simons-algorithm.md) | Hidden-subgroup precursor that inspired Shor's circuit. |
| [Quantum Fourier transform](concepts/quantum-fourier-transform.md) | Change of basis that turns periodicity into peaks. |
| [Grover's algorithm](concepts/grovers-algorithm.md) | Amplitude amplification for unstructured search. |
| [Adiabatic quantum computing](concepts/adiabatic-quantum-computing.md) | Slow interpolation from a driver Hamiltonian to a problem Hamiltonian. |
| [Quantum annealing](concepts/quantum-annealing.md) | Open-system variant that allows leaving and returning toward the ground state. |
| [BB84](concepts/bb84.md) | Prepare-and-measure quantum key distribution. |
| [Ekert 91](concepts/ekert91.md) | Entanglement-based QKD, with BBM92. |
| [Bell inequality](concepts/bell-inequality.md) | Device-independent test used for certifiable randomness. |
| [Quantum teleportation](concepts/quantum-teleportation.md) | Move an unknown state using entanglement and two classical bits. |
| [Hamiltonian simulation](concepts/hamiltonian-simulation.md) | Approximate $e^{-iHt}$ on a quantum computer. |
| [Trotterization](concepts/trotterization.md) | Product-formula simulation of a sum of local Hamiltonians. |
| [Phase estimation](concepts/phase-estimation.md) | Read an eigenphase into a clock register with the QFT. |
| [VQE](concepts/vqe.md) | Hybrid variational loop for ground-state energy. |

## Analyses

| Page | Summary |
|---|---|
| [Course map](analyses/course-map.md) | Official QCFx2 weeks ↔ raw files ↔ source notes in reading order; Dec 14 deadline. |
| [Quiz inventory](analyses/quiz-inventory.md) | Every graded question in the outline vs. the capture: 52/57 present, 5 to re-capture. |

## Sources


### Week 1

- [Period finding algorithm](sources/week-1-01-period-finding-algorithm.md) — The quantum part of Shor\'s algorithm is called "period finding.\" In this section, you will learn about this quantum subroutine.
- [Shor's algorithm: reduction of factoring to order finding](sources/week-1-02-shor-s-algorithm-reduction-of-factoring-to-order-finding.md) — In the next several videos and text units, you will take a deep dive with Peter Shor into several details behind Shor\'s algorithm, including a discussion of the reduction of facto
- [Shor's Algorithm: introduction to the short quantum factorization algorithm](sources/week-1-03-shor-s-algorithm-introduction-to-the-short-quantum-factorization-algorithm.md) — The quantum part of Shor\'s algorithm is called "period finding.\" In this section, you will learn about this quantum subroutine.
- [Simon's Algorithm](sources/week-1-04-simon-s-algorithm.md) — In the last video, Professor Shor mentioned *Simon\'s Algorithm* as a motivation for his discovery of the factoring algorithm.
- [Shor's Algorithm: Detailed Steps of the Quantum Order Finding Algorithm](sources/week-1-05-shor-s-algorithm-detailed-steps-of-the-quantum-order-finding-algorithm.md) — {width="5.267716535433071in" height="3.0555555555555554in"} {width="5.267716535433071in" height="3.1944444444444446in"} {width="5.267716535433071in" height="3.1805555555555554in"}
- [Shor's Algorithm: Order Finding Algorithm Measurement Result as a Geometric Sum](sources/week-1-06-shor-s-algorithm-order-finding-algorithm-measurement-result-as-a-geometric-sum.md) — The quantum part of Shor\'s algorithm is called "period finding.\" In this section, you will learn about this quantum subroutine.
- [Demonstrations of Shor's Algorithm: Introduction](sources/week-1-07-demonstrations-of-shor-s-algorithm-introduction.md) — In the next several videos, you will explore two demonstrations of Shor\'s algorithm on small-scale quantum-computers realized using liquid-state NMR and trapped ions.
- [Demonstrations of Shor's Algorithm: Shor's Algorithm with NMR](sources/week-1-08-demonstrations-of-shor-s-algorithm-shor-s-algorithm-with-nmr.md) — Course page.
- [Demonstrations of Shor's Algorithm: Perspective on NMR](sources/week-1-09-demonstrations-of-shor-s-algorithm-perspective-on-nmr.md) — Course page.
- [Demonstrations of Shor's Algorithm: Quantum Factoring With Trapped Ions - Challenge Setup](sources/week-1-10-demonstrations-of-shor-s-algorithm-quantum-factoring-with-trapped-ions-challenge.md) — Course page.
- [Demonstrations of Shor's Algorithm: Quantum Factoring With Trapped Ions - Ion Trapping System](sources/week-1-11-demonstrations-of-shor-s-algorithm-quantum-factoring-with-trapped-ions-ion-trapp.md) — Course page.
- [Demonstrations of Shor's Algorithm: Quantum Factoring With Trapped Ions - Experimental Results](sources/week-1-12-demonstrations-of-shor-s-algorithm-quantum-factoring-with-trapped-ions-experimen.md) — Course page.
- [Demonstrations of Shor's Algorithm: Pretending to Factor](sources/week-1-13-demonstrations-of-shor-s-algorithm-pretending-to-factor.md) — Course page.
- [Case Study Concept Questions](sources/week-1-14-case-study-concept-questions.md) — Course page.
- [Modern Cryptography and Shor's Algorithm Quiz](sources/week-1-15-modern-cryptography-and-shor-s-algorithm-quiz.md) — Course page.

### Week 2

- [Qiz: 9 questions](sources/week-2-01-qiz-9-questions.md) — Course page.
- [Introduction to quantum algorithms and cryptography](sources/week-2-02-introduction-to-quantum-algorithms-and-cryptography.md) — Welcome to Course 2, *Quantum Algorithms for Cybersecurity, Chemistry, and Optimization*.
- [Classical and quantum gates from course number 1](sources/week-2-03-classical-and-quantum-gates-from-course-number-1.md) — The following tables present a list of classical gates and quantum gates that were used in Course 1, *Introduction to Quantum Computing*.
- [Modern cryptography](sources/week-2-04-modern-cryptography.md) — We generate and communicate tremendous amounts of digital data every day.
- [RSA cryptosystem](sources/week-2-05-rsa-cryptosystem.md) — We often communicate securely by encrypting data using cryptographic schemes.
- [Factoring with a quantum computer: shor's algorithm](sources/week-2-06-factoring-with-a-quantum-computer-shor-s-algorithm.md) — The security of the RSA cryptosystem is premised on a one-way function that is difficult to invert using a classical computer.
- [Factoring with a quantum computer: How Shor's algorithm works](sources/week-2-07-factoring-with-a-quantum-computer-how-shor-s-algorithm-works.md) — In the last video, you saw how Shor\'s Algorithm is implemented within the circuit model for quantum computing.
- [Quantum Fourier Transform](sources/week-2-08-quantum-fourier-transform.md) — **The following reading is optional for learners who want to learn a bit more about the Quantum Fourier Transform (QFT).** The Quantum Fourier Transform (QFT) is a critical operati

### Week 3

- [Quantum Cryptography - Making Codes](sources/week-3-01-quantum-cryptography-making-codes.md) — Course page.
- [Post-Quantum Cryptography](sources/week-3-01a-post-quantum-cryptography.md) — Shor breaks asymmetric crypto; symmetric-key schemes are not thought to be at catastrophic risk; NIST post-quantum standardization.
- [Single-photon sources and detectors](sources/week-3-01b-single-photon-sources-and-detectors.md) — Generating and detecting the photons that QKD runs on.
- [quantum key distribution bb84](sources/week-3-02-quantum-key-distribution-bb84.md) — Course page.
- [entangled proton sources and detectors](sources/week-3-03-entangled-proton-sources-and-detectors.md) — Course page.
- [Quantum Key Distribution - Ekert91 and BBM92](sources/week-3-04-quantum-key-distribution-ekert91-and-bbm92.md) — Course page.
- [random numbers: an introduction](sources/week-3-05-random-numbers-an-introduction.md) — Course page.
- [bell's inequality](sources/week-3-06-bell-s-inequality.md) — Course page.
- [Bell's Inequality and Certifiable Random Number Generation](sources/week-3-07-bell-s-inequality-and-certifiable-random-number-generation.md) — Course page.
- [Quantum Teleportation](sources/week-3-08-quantum-teleportation.md) — Course page.
- [Quantum Repeaters](sources/week-3-08a-quantum-repeaters.md) — Photon loss plus no-cloning rules out classical amplifiers; repeaters distribute entanglement instead.
- [Quantum Cryptography Quiz (4 questions)](sources/week-3-09-quantum-cryptography-quiz-4-questions.md) — Course page.

### Week 4

- [Introduction: quantum simulation](sources/week-4-00-introduction-quantum-simulation.md) — Manin (1980) and Feynman (1982): simulating quantum systems classically scales exponentially, so use a quantum system.
- [What s a Hamiltonian?](sources/week-4-01-what-s-a-hamiltonian.md) — Course page.
- [Simulation example: Particle in a box](sources/week-4-02-simulation-example-particle-in-a-box.md) — Course page.
- [Hamiltonian simulation : Trotterization](sources/week-4-03-hamiltonian-simulation-trotterization.md) — Course page.
- [Simulation of chemistry problems](sources/week-4-04-simulation-of-chemistry-problems.md) — Course page.
- [Phase estimation](sources/week-4-05-phase-estimation.md) — Course page.
- [Variational Quantum Eigensolver](sources/week-4-06-variational-quantum-eigensolver.md) — Course page.
- [VQE in practice](sources/week-4-07-vqe-in-practice.md) — Course page.

### Week 5

- [Introduction to Quantum optimization](sources/week-5-01-introduction-to-quantum-optimization.md) — Course page.
- [Adiabatic quantum computing: concept](sources/week-5-02-adiabatic-quantum-computing-concept.md) — Course page.
- [Adiabatic Quantum Computing: Expert View](sources/week-5-03-adiabatic-quantum-computing-expert-view.md) — Course page.
- [Grover's Algorithm: Quantum Search](sources/week-5-04-grover-s-algorithm-quantum-search.md) — Course page.
- [Introduction to Grover's Algorithm on the Quantum Experience](sources/week-5-05-introduction-to-grover-s-algorithm-on-the-quantum-experience.md) — Course page.
- [Lab practicum: Grover's algorythm](sources/week-5-06-lab-practicum-grover-s-algorythm.md) — Course page.
- [Grover's algorithm: Introduction](sources/week-5-07-grover-s-algorithm-introduction.md) — Course page.
- [Quantum optimization Qiz](sources/week-5-08-quantum-optimization-qiz.md) — Course page.
