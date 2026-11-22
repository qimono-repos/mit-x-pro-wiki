---
title: "Quantum Annealing"
type: source
week: 5
raw: mit-raw/week5-quantum-annealing.md
---

# Quantum Annealing

Source page from week 5 (official Week 4), lecture video by Gabriel Samach. [Raw transcript](/mit-raw/week5-quantum-annealing.md)

This page was missing from the original capture of `week5.md`. Captured: the SRT transcript and a screenshot of the Learn text, "Introduction to Quantum Annealing (QA)" (both added 2026-11-22). Still missing: video frames and the page's practice question.

## Learn (summary in my words; [screenshot](/mit-raw/week5/media/annealing/learn-introduction-to-quantum-annealing.png))

- QA solves classical optimization problems. It is an adiabatic quantum computer allowed to leave its ground state, then tunneling and relaxation bring it back to the ground state or a lower one, which encodes an (approximate) answer.
- **The name** comes from annealing in metallurgy: heating lets the metal rearrange, and cooling locks in the new, better configuration.
- **Classical simulated annealing (SA):** from the current solution with energy $E$, pick a nearby one with energy $E'$. Always keep it if $E' < E$. Keep it *sometimes* even if $E' > E$, which lets the search climb out of local minima. That acceptance probability is high at the start ("high temperature") and drops as the temperature parameter $T$ is lowered to zero, until the system freezes into a local or global minimum.
- **QA swaps thermal fluctuations for quantum fluctuations.** A wavefunction is spread out (it has a mean and a spread, and repeated measurements give different results). When it spans several local minima, the system *tunnels through* barriers instead of being thermally kicked *over* them. The tunneling rate is set by a transverse field (along x or y on the Bloch sphere), not by temperature.
- **Schedule:** $H(t) = A(t)\,H_\text{initial} + B(t)\,H_\text{problem}$ with $A: 1 \to 0$ and $B: 0 \to 1$. $H_\text{initial}$ is a large transverse $X$ field on all qubits; the optimum is the ground state of $H_\text{problem}$.
- As in AQC there is a minimum gap, and real problems almost certainly leave the ground state through noise and Landau–Zener transitions. The hope is that tunneling plus dissipation bring the system back down.
- **D-Wave:** commercially available, more than 2000 superconducting qubits with fixed "chimera graph" connectivity. An engineering achievement, but there is no theoretical or experimental evidence of quantum enhancement for a general class of optimization problems. Scaling up forced relatively low-coherence qubits, fixed connectivity and only $ZZ$ couplings. Higher coherence, other couplings ($XX$, $YY$), multi-body terms ($XXX$) and richer connectivity might do better, and even a "just classical" annealer could be useful if it beats existing classical computers on some problems.

## What the video covers

- **Recap (0:20–1:07).** AQC is *analog* quantum computing: a continuous transition from one Hamiltonian's ground state to another's instead of discrete gates. It is provably universal, but it fails if the system ends in an excited state.
- **Thermal problem (1:13–3:01).** A shrinking ground/excited gap meets thermal photons from a finite-temperature environment. The smaller the gap relative to the photon energy, the likelier an excitation. That's why superconducting qubits run at about 10 mK in a dilution refrigerator: a 5 GHz bare-qubit gap corresponds to about 250 mK, an order of magnitude above. Avoided crossings during the evolution can be far smaller than the bare-qubit gap, which would need a fridge much colder than 10 mK, which isn't practical today.
- **Speed problem (3:01–3:25).** Sweeping a small gap too fast causes a Landau–Zener transition, even at zero temperature.
- **Annealing defined (3:34–4:23).** Quantum annealing is basically an adiabatic quantum computer that has left its ground state at some point. Quantum tunneling plus relaxation are used to get back to the ground state or a lower state. There is no proof or evidence that this gives quantum enhancement for a general class of problems; that's an open research question.
- **Scope (4:26–6:11).** Unlike universal AQC, annealing targets only classical optimization problems (cost function; many near-optimal answers are good enough).
- **Ising encoding (6:11–7:29).** The problem goes into an Ising Hamiltonian (local fields plus pairwise couplings). Its energy levels are candidate solutions, and each energy is that solution's cost. "The goal of quantum annealing is to engineer a system of qubits with an Ising Hamiltonian corresponding to the optimization problem of interest."
- **Protocol (7:33–8:37).** Start in the ground state of $\sum_j X_j$ (all qubits in $|+\rangle$), then ramp that down while ramping the problem Hamiltonian up.
- **Status (8:37–10:04).** Ending in an excited state still gives a candidate answer, but there's no guarantee it is better or found faster than classically. No provable universality or enhancement, and no demonstration of enhancement for a class of optimization problems to date.

## Concepts touched

[[concepts/quantum-annealing]] · [[concepts/adiabatic-quantum-computing]]
