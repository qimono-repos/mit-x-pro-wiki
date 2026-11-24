---
title: "Zhang et al. 2017: many-body dynamical phase transition, 53-qubit ion simulator"
type: paper
aliases: [Zhang 2017, 53-qubit simulator, 53 ions, Monroe 2017]
citation: "J. Zhang, G. Pagano, P. W. Hess, A. Kyprianidis, P. Becker, H. Kaplan, A. V. Gorshkov, Z.-X. Gong, C. Monroe. Nature 551, 601–604 (2017)"
arxiv: "1708.01044"
local_pdf: "mit-raw/external/papers/zhang-2017-53-ion-dpt-arxiv-1708.01044.pdf"
assigned_by: "[[sources/week-4-08-reflect-and-review]]"
---

# Zhang et al. 2017: 53-ion dynamical phase transition

**Local PDF:** [[mit-raw/external/papers/zhang-2017-53-ion-dpt-arxiv-1708.01044.pdf|open the paper]] · arXiv [1708.01044](https://arxiv.org/abs/1708.01044) · *Chosen paper for the Week 3 Reflect & Review* → [[analyses/reflect-rev-draft-002]]

## In two sentences
Up to 53 trapped ¹⁷¹Yb⁺ ions simulate a **long-range transverse-field Ising model**. A sudden change of the Hamiltonian (a *quench*), followed by single-shot readout of every ion, reveals a **dynamical phase transition**: a non-equilibrium transition that equilibrium statistical mechanics doesn't describe.

## Where to look in the PDF
| What | Page |
|---|---|
| Abstract: 53 qubits, ~99% detection, "difficult to model classically" | [[mit-raw/external/papers/zhang-2017-53-ion-dpt-arxiv-1708.01044.pdf#page=1\|p.1]] |
| Fig. 1, the quench picture (spins on a Bloch sphere: they either follow the field or stay pinned) | [[mit-raw/external/papers/zhang-2017-53-ion-dpt-arxiv-1708.01044.pdf#page=2\|p.2]] |
| Fig. 2, 16-spin magnetization dynamics and the **Z₂ symmetry** (σˣ,ʸ → −σˣ,ʸ) of the Ising Hamiltonian | [[mit-raw/external/papers/zhang-2017-53-ion-dpt-arxiv-1708.01044.pdf#page=2\|p.2]]–[[mit-raw/external/papers/zhang-2017-53-ion-dpt-arxiv-1708.01044.pdf#page=3\|p.3]] |
| Fig. 3, two-body correlations C₂ up to N = 53; "∼99% for each qubit… all possible many-body correlators in a single shot" | [[mit-raw/external/papers/zhang-2017-53-ion-dpt-arxiv-1708.01044.pdf#page=3\|p.3]] |
| Fig. 4, **domains** of aligned spins = many-body (high-order) correlators, "difficult or impossible to model classically" | [[mit-raw/external/papers/zhang-2017-53-ion-dpt-arxiv-1708.01044.pdf#page=4\|p.4]] |
| Appendix G, analytic solution for all-to-all coupling (α = 0) | [[mit-raw/external/papers/zhang-2017-53-ion-dpt-arxiv-1708.01044.pdf#page=7\|p.7]] |

## How it connects to our wiki
- **Same Hamiltonian family as annealing and AQC.** The transverse field Bᶻ ΣZ plays the role of the driver, and J Σ σˣσˣ is the Ising problem term. Compare [[concepts/quantum-annealing#^encoding-and-gap|annealing's Ising encoding]] and [[concepts/adiabatic-quantum-computing#^ising|the AQC Ising chain]]. The difference is in *how* the Hamiltonian changes: AQC sweeps it **slowly** ([[concepts/adiabatic-quantum-computing#^interpolation|interpolation]]), while Zhang changes it **suddenly** (quench) and watches the dynamics. The axis labels are swapped too (field along z, coupling along x), which is just a basis choice.
- **Z₂ symmetry, the same one as our graded Ising question.** Zhang's Fig. 2 discusses the global spin-flip symmetry. That's the ∏X symmetry behind the two degenerate Néel states in [[concepts/adiabatic-quantum-computing#^ising]] and [[quizzes/week-4#Q3: Adiabatic Quantum Computing: Ising Model]].
- **Analog quantum simulation.** This is Chuang's "build a controllable quantum system that mimics the target" strategy: [[concepts/quantum-simulation#^approaches]], [[concepts/quantum-simulation#^analog-deformation]], and the ultracold-atoms CYU [[quizzes/week-3#Q1: Ultra-Cold Atoms]]. Its readout matches Chuang's "issue #3: what to measure?" in [[concepts/quantum-simulation#^ideas-and-issues]]: single-shot readout of every ion is exactly that answer.
- **Why classical methods struggle.** Long-range, all-to-all interactions are hard for DMRG-type tensor networks ([[concepts/quantum-simulation#^quantum-inspired]]), which do best in 1D with short-range entanglement.
- **Hardware lineage.** Monroe → IonQ (NYSE: IONQ), and trapped ions at scale today (Quantinuum Helios, 98 qubits, all-to-all, Nature 2026). Context and sources in [[analyses/reflect-rev-draft-002]] §Q1–Q2.

## Rival paper in the same Nature issue
Bernien et al. (Lukin group, Harvard/MIT): a 51-atom Rydberg simulator, Nature 551 (30 Nov 2017). *[to verify: page 579]*. Not stored locally.
