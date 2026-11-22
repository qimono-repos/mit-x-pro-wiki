---
title: "External: adiabatic computation and finite coherence time"
type: external-source
added: 2026-11-22
added_by: Claude (Opus 5.5), on request
reason: The course never states whether adiabatic evolution needs infinite coherence. Its Learn text says "sufficiently slow" changes and a runtime long compared with the inverse gap squared; the expert view says it "will work, for sure, if you go infinitely slowly"; and the AQC II question treats coherence time ≈ gap timescale as a workable, if hard, situation. This file adds primary literature. It is NOT course material.
---

# External source: adiabatic computation does not require infinite coherence

Paraphrased, with links.

- **Inherent robustness.** Childs, Farhi (one of AQC's inventors, MIT) and Preskill describe an inherent robustness of adiabatic computation against unitary control errors and decoherence, studied numerically. Environment interactions matter mainly when they induce transitions between energy eigenstates. ([Phys. Rev. A 65, 012322 (2001), arXiv:quant-ph/0108048](https://arxiv.org/abs/quant-ph/0108048))
- **T2 is not the right yardstick.** Albash & Lidar: when the computation stays near the ground state and decoherence acts in the instantaneous energy eigenbasis, a short single-qubit $T_2$ need not hurt the adiabatic algorithm. ([Phys. Rev. A 91, 062320 (2015), arXiv:1503.08767](https://arxiv.org/abs/1503.08767))
- **The requirement is finite.** For open systems relaxing toward thermal equilibrium, the runtime must be long compared with the minimum inverse gap squared: finite, not infinite. ([Campos Venuti, Albash, Lidar, Zanardi, Phys. Rev. A 93, 032118 (2016)](https://link.aps.org/accepted/10.1103/PhysRevA.93.032118))

## Relation to the course

It agrees with the Learn text ("sufficiently slow", gap-limited runtime, thermal transitions once the gap < $k_BT$). The expert's "infinitely slowly" describes the ideal limit that guarantees success; it is not a hardware requirement.
