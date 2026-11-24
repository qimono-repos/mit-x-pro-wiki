---
title: "External: the three Reflect & Review papers (abstract-level summaries)"
type: external-source
added: 2026-11-22
added_by: Claude (Opus 5.5), on request
reason: The official Week 3 Reflect & Review activity assigns these three articles (course-assigned reading, but not course text). Summaries are in our own words, from the arXiv versions Albert supplied.
---

# The three Reflect & Review papers

| Paper | Platform / institution | What it shows (own words) |
|---|---|---|
| [[papers/zhang-2017-53-ion-dynamical-phase-transition\|**Zhang et al.**]], *Observation of a many-body dynamical phase transition with a 53-qubit quantum simulator*, Nature 551, 601–604 (2017). [arXiv:1708.01044](https://arxiv.org/abs/1708.01044) | Up to 53 trapped ¹⁷¹Yb⁺ ions. Joint Quantum Institute (University of Maryland and NIST); C. Monroe also listed at IonQ. | Analog simulation of a long-range transverse-field Ising model. A global Ising interaction with tunable strength and range, plus individual readout of every ion at ~99% efficiency, gives single-shot many-body correlations. They observe a *dynamical* (non-equilibrium) phase transition, in a regime where equilibrium statistical mechanics doesn't apply and the long-range, highly connected features are hard to compute classically. Links: [[concepts/quantum-simulation]], [[concepts/quantum-annealing]] (same Ising model family). |
| [[papers/omalley-2016-h2-molecular-energies\|**O'Malley et al.**]], *Scalable quantum simulation of molecular energies*, Phys. Rev. X 6, 031007 (2016). [arXiv:1512.06860](https://arxiv.org/abs/1512.06860) | Superconducting qubits. UCSB and Google, with Harvard, LBNL, Tufts and UCL. | The H₂ energy surface on a programmable superconducting array, the first electronic-structure calculation without exponentially costly precompilation. Two algorithms: VQE with unitary coupled cluster (dissociation energy within chemical accuracy) and Trotterized phase estimation. VQE proved more robust to certain errors. Links: [[concepts/vqe]], [[concepts/phase-estimation]], [[concepts/trotterization]]. |
| [[papers/kandala-2017-hardware-efficient-vqe\|**Kandala et al.**]], *Hardware-efficient variational quantum eigensolver for small molecules and quantum magnets*, Nature 549, 242–246 (2017). [arXiv:1704.05018](https://arxiv.org/abs/1704.05018) | Superconducting qubits. IBM T.J. Watson. | VQE with trial states built from the chip's native interactions ("hardware-efficient"), up to 6-qubit Hamiltonians with 100+ Pauli terms, molecules up to BeH₂, plus a quantum-magnetism problem. Results agree with a noisy model of the device, so the paper also maps what noise does to a chemistry calculation. Links: [[concepts/vqe]], [[concepts/quantum-chemistry]]. |
