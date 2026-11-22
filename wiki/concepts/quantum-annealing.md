---
title: Quantum annealing
type: concept
---

# Quantum annealing

A quantum annealer is basically an adiabatic quantum computer that has left its ground state at some point during the evolution, and uses quantum tunneling plus relaxation to get back down to the ground state or at least a lower-energy one. It targets only classical optimization problems, and the course is explicit that there is no proof or demonstration of quantum enhancement to date ([source note](../sources/week-5-03a-quantum-annealing.md)).

## Simulated annealing, then the quantum version

The name comes from metallurgy: heat lets a metal rearrange, and cooling freezes in the better configuration. **Classical simulated annealing** is the algorithmic version. From a solution with energy $E$, try a neighbour with energy $E'$. Always accept it if $E' < E$, and sometimes accept it even if $E' > E$, with a probability that is high at "high temperature" and shrinks as the temperature parameter $T$ is lowered to zero. Accepting worse moves lets the search climb *over* barriers out of local minima, and at $T = 0$ it freezes into a local or global minimum ([source note](../sources/week-5-03a-quantum-annealing.md), Learn). ^simulated-annealing

**Quantum annealing replaces thermal fluctuations with quantum fluctuations.** A wavefunction is spread out rather than sitting at one point, so when it spans several local minima the system can **tunnel through** a barrier instead of being kicked over it. The tunneling strength is set by the **transverse field** (along x or y on the Bloch sphere), not by temperature ([source note](../sources/week-5-03a-quantum-annealing.md), Learn). ^quantum-fluctuations

| | Simulated annealing | Quantum annealing |
|---|---|---|
| Escape mechanism | thermal activation *over* barriers | quantum tunneling *through* barriers |
| Control knob | temperature $T 	o 0$ | transverse field $A(t) 	o 0$ |
| Runs on | a classical computer | a quantum device |

## Why annealing exists: AQC's two failure modes

[[concepts/adiabatic-quantum-computing]] must stay in the ground state, and the gap to the first excited state can become very small. Two things then knock it out ([raw transcript](/mit-raw/week5-quantum-annealing.md), ~1:13–3:25):

1. **Heat.** A finite-temperature environment emits thermal photons with energy $\sim k_BT$. When one is absorbed the system may be excited, and the smaller the gap relative to the photon energy, the higher that probability. Temperature does not change the gap; it changes how often the bath can bridge it. Superconducting qubits run at about 10 mK because a 5 GHz bare-qubit gap corresponds to $hf/k_B \approx 250$ mK. Avoided crossings during the evolution can be much smaller than that, so staying cold enough would need a fridge "much colder than 10 millikelvin", which isn't practical. ^thermal-excitation
2. **Speed.** Sweeping a small gap too fast causes a **Landau–Zener transition**, even at zero temperature, so the runtime must grow as gaps shrink.

## What annealing does instead

It accepts that the system will leave the ground state, and relies on quantum tunneling and relaxation (dissipation into the environment) to return to the ground state or a lower one. Kadowaki and Nishimori (1998) proposed the idea; the course states the mechanism in the transcript (~3:53–4:10). ^tunneling-relaxation

The course is explicit about status: "to date, there is no proof or evidence" that these quantum and dissipative dynamics give quantum enhancement for a general class of problems. It is an open research question. Unlike AQC, annealing makes no provable claim to universality or enhancement, and there is no demonstration of enhancement for a class of optimization problems ([raw transcript](/mit-raw/week5-quantum-annealing.md), ~4:10–4:23 and ~9:17–9:30; also [raw week 5](/mit-raw/week5.md), AQC concept Learn). An annealer could still be useful if it beat existing classical hardware even with classical scaling, but that has not been demonstrated either. ^no-enhancement-evidence

## Encoding and protocol

The optimization problem goes into an **Ising Hamiltonian**: spin-1/2s with local fields plus pairwise interactions,

$$
H_p = \sum_i h_i Z_i + \sum_{i<j} J_{ij} Z_i Z_j .
$$

Choose the couplings so the energy levels are the candidate solutions and each level's energy is that solution's cost: higher energy, higher penalty. In the course's words, "the goal of quantum annealing is to engineer a system of qubits with an Ising Hamiltonian corresponding to the optimization problem of interest" ([raw transcript](/mit-raw/week5-quantum-annealing.md), ~6:11–7:22; the qubit-level hardware detail is in this [external source](/mit-raw/external/quantum-annealing-ising.md)). Gap logic carries over from AQC: a *smaller* minimum gap, not a larger one, forces slower evolution through the gap region (see [[concepts/adiabatic-quantum-computing#^minimum-gap]]). ^encoding-and-gap

Protocol: the Learn page writes the schedule as

$$
H(t) = A(t)\,H_\text{initial} + B(t)\,H_\text{problem}, \qquad A(0)=1,\ B(0)=0,\ A(t_\text{final})=0,\ B(t_\text{final})=1 .
$$

Start in the ground state of the transverse-field driver $H_\text{initial} = -\sum_j X_j$ (all qubits in $|+\rangle$, easy to prepare), gradually turn it down and $H_\text{problem}$ up, and read out a low-energy eigenstate of $H_p$. The lower its energy, the better the solution. An excited final state is still a candidate answer, which is the point: for optimization, "several nearly optimal solutions" are often good enough ([raw transcript](/mit-raw/week5-quantum-annealing.md), ~7:33–9:04). ^protocol

## D-Wave and the name "annealing"

The expert-view lecture gives the history ([raw transcript](/mit-raw/week5-quantum-annealing-expert-view.md)). D-Wave was founded in 1999, before AQC was proposed (Farhi et al., 2000; Aharonov et al. later proved it universal). In 2007 D-Wave announced a 16-qubit "adiabatic quantum computer", which drew heavy skepticism. Its chips run extremely cold, but their structure still allows thermal excitations, so the temperature probably exceeds the smallest gap. Since that isn't adiabatic computation, it was renamed quantum annealing. The lecturer's verdict: it certainly uses quantum processes, but there are no theoretical results that it is more powerful, and its experimental wins might be only a constant factor from a fast physical process. "We don't really know whether D-wave is more powerful." ^dwave

The Learn page adds the hardware picture: more than 2000 superconducting qubits with fixed "chimera graph" connectivity, an engineering achievement with no theoretical or experimental evidence of enhancement for a general class of problems. Scaling forced design limits: relatively low-coherence qubits, fixed connectivity, and only $ZZ$ couplings, a small corner of the possible annealing "phase space". Higher coherence, $XX$/$YY$ couplings, multi-body terms such as $XXX$, and better connectivity might help ([source note](../sources/week-5-03a-quantum-annealing.md), Learn). ^dwave-hardware

## AQC vs annealing

| | AQC | Quantum annealing |
|---|---|---|
| Must stay in ground state | yes | no |
| Scope | universal | classical optimization only |
| Provable enhancement | universal, polynomially equivalent to the gate model | none proved or demonstrated |
| Role of the environment | noise to avoid | relaxation is part of the mechanism |

## Sources

- [Quantum Annealing](../sources/week-5-03a-quantum-annealing.md) (transcript)
- [Quantum Annealing: Expert View](../sources/week-5-03b-quantum-annealing-expert-view.md) (transcript, D-Wave)
- [Introduction to quantum optimization](../sources/week-5-01-introduction-to-quantum-optimization.md)
- Raw: [week 5](/mit-raw/week5.md) · [quantum annealing transcript](/mit-raw/week5-quantum-annealing.md) · [expert view transcript](/mit-raw/week5-quantum-annealing-expert-view.md)
