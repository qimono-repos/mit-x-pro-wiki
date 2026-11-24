---
title: FeMoco classical benchmark (2026)
type: analysis
---

# Zhai et al. 2026: classical FeMoco benchmark
[Full preprint and verbatim abstract](https://arxiv.org/abs/2601.04621) · [full HTML](https://arxiv.org/html/2601.04621) · [journal record, Oct 21 2026](https://pubmed.ncbi.nlm.nih.gov/42905822/) · [code](https://github.com/hczhai/femoco-scripts-2026) · [data](https://zenodo.org/records/22116121).

Short exact excerpt: “Our result relies on the insight that the ground-state problem can be characterized as one of ranking many competing, but largely simple, states.”

Summary: high-order coupled cluster and density matrix renormalization group with extrapolation give closely agreeing resting-state energies; several spin configurations cannot be distinguished at chemical accuracy. The LLDUC model has 113 electrons in 76 spatial orbitals (152 spin orbitals). Consensus uncertainty ±0.31 kcal/mol; conservative ±1.25 kcal/mol, near rather than strictly within 1 kcal/mol. UDMRG cost 2,768,994 CPU core-hours; largest coupled cluster calculation 40,000 core-hours. Frontier estimates are hypothetical idealized throughput, not measured wall time. Ground-state model is not entire catalytic cycle.

Classical advantage: structured states, proven HPC workflow; drawbacks expensive extrapolation, model uncertainty and scaling. Quantum opportunity: correlated states, future fault-tolerant phase estimation; limitations state preparation, logical error correction, measurement and circuit cost. NISQ VQE on reduced fragments only, not full 152-orbital calculation. Compare same Hamiltonian, accuracy, time, all-in cost, repeatability; include classical DMRG/CC baselines and disclose truncation. See [[analyses/qimono-venture-pilot]] and [[concepts/quantum-chemistry]].
