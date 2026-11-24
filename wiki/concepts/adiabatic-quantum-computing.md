---
title: Adiabatic quantum computing
type: concept
---

# Adiabatic quantum computing

An adiabatic algorithm encodes the answer as the ground state of a problem Hamiltonian $H_p$ and reaches that state by a slow interpolation from an easy driver Hamiltonian $B$.

**Definition and status.** AQC "casts the problem of finding the solution of a computational problem into the problem of obtaining the lowest energy eigenstate of a specified Hamiltonian." It was proposed by Farhi, Goldstone, Gutmann and Sipser (2000) (*background:* that's Michael Sipser of MIT mathematics, the complexity theorist behind the textbook *Introduction to the Theory of Computation*), and Aharonov et al. (2004) showed it is **polynomially equivalent to universal circuit-model quantum computation**. The governing principle is the **adiabatic theorem**: a system stays in its lowest-energy eigenstate under sufficiently slow changes to its Hamiltonian. The Hamiltonian is *time-dependent* (one continuous interpolation, not a sequence of constant Hamiltonians), the output is the *ground* state, not an excited state, ([raw week 5](/mit-raw/week5.md), AQC concept Learn, ~line 60). The course calls AQC a form of **analog** quantum computing: instead of discrete gates it relies on the continuous transition of a system from one Hamiltonian's ground state to another's ([annealing transcript](/mit-raw/week5-quantum-annealing.md), ~0:20–0:38). Being polynomially equivalent to the gate model is not the same as being the gate model. ^definition

The course writes the interpolation, for a transverse-field driver, as

$$
H_p |z\rangle = E(z) |z\rangle
$$

$$
H(t) = \left(1 - \frac{t}{T}\right) B + \frac{t}{T} H_p
$$

$$
B = -\sum_j \sigma_x^j
$$

with $0 \le t \le T$ and $T$ the total runtime. The initial ground state of $B$ is the uniform superposition (every spin in $|+\rangle$), which is easy to prepare. If $T$ is large compared with the inverse square of the minimum spectral gap along the path, the adiabatic theorem keeps the system in the instantaneous ground state, which at $t = T$ is a ground state of $H_p$. ^interpolation

The lecture's caveat: for a large enough problem the minimum gap is so small that the required $T$ is impractical, and once the gap drops below the thermal energy $k_B T$ the environment kicks the system out of the ground state. That limitation is why the course distinguishes this closed-system ideal from [[concepts/quantum-annealing]].

## Why it's hard in practice: the minimum gap

Along the path the two lowest levels form an **avoided crossing**, and the gap shrinks as the problem grows. The Learn text gives two consequences ([raw week 5](/mit-raw/week5.md), AQC concept Learn):
1. **Speed:** you must go more slowly through the gap region. Go too fast and the system "jumps" to the excited state via a **Landau–Zener transition**. Running faster than the adiabatic theorem allows lowers the chance of a correct answer.
2. **Noise:** thermal noise and control noise drive transitions once the gap falls below $k_BT$. The annealing lecture makes this concrete: a finite-temperature environment emits thermal photons, and absorbing one can excite the system. Superconducting qubits run at about 10 mK because their bare 5 GHz gap ≈ 250 mK, but avoided crossings during the evolution can be far smaller (see [[concepts/quantum-annealing#^thermal-excitation]]). Landau–Zener is separate: it happens even at zero temperature if you go too fast. The device's limited coherence time bounds how slowly you can go. The requirement is a *finite* runtime long compared with the inverse gap squared, not infinite coherence. The course's AQC II question treats coherence ≈ gap timescale as hard but workable, and the literature finds AQC fairly robust to decoherence in the energy eigenbasis ([external source](/mit-raw/external/adiabatic-decoherence.md)).

^minimum-gap

**Slow down only where it matters.** In the expert-view Q&A the lecturer says that if you know where the avoided crossing is, you can evolve quickly most of the time and slow down only near it. That is how adiabatic Grover search gets its square-root speedup: a single avoided crossing with a gap of about $1/\sqrt N$. If you don't know where the gaps are, this is hard ([raw transcript](/mit-raw/week5-quantum-annealing-expert-view.md), ~3:54–5:07; see [[concepts/grovers-algorithm]]). ^local-schedule

**What you can do instead.** Beyond that course point, this is my own reasoning built on the Learn text above, not a course list: change the path or Hamiltonians to *enlarge* the minimum gap; accept a *probabilistic* success and estimate the probability of staying in the ground state; or, as quantum annealers do, use relaxation to fall back to low energy. Two options do *not* help: rushing (Landau–Zener), and starting in an arbitrary state of $H_p$ and waiting for it to decay, which is not adiabatic computation. Plain relaxation also tends to get stuck in a *local* minimum of the cost landscape rather than the global one, which is exactly the problem simulated and quantum annealing try to escape (see [[concepts/quantum-annealing#^simulated-annealing]]). ^gap-strategies

## Ising-type problem Hamiltonians

Problems are encoded as $H_p|z\rangle = E(z)|z\rangle$ on bitstrings $z$, often as a sum of clause penalties $E_\alpha(z)$ (0 if clause $\alpha$ is satisfied, 1 if not) ([raw week 5](/mit-raw/week5.md), ~line 1038). The quiz uses an Ising chain, driver $\sum_j X^j$ and problem $J\sum Z^iZ^{j+1}$. Its stem states the energy rule: aligned neighbours contribute $+J$, anti-aligned $-J$, so with $J > 0$ the ground state minimizes the number of aligned neighbours. That's all the information the question needs (raw week 5, quiz Q3, ~line 5121). ^ising

*Background, not in the course:* with $J > 0$ the lowest arrangement is two-fold degenerate, $\uparrow\downarrow\uparrow\cdots$ and $\downarrow\uparrow\downarrow\cdots$ (the two Néel states). Both the driver and $Z^jZ^{j+1}$ commute with the global spin flip $\prod_j X^j$, and the start state $|+\rangle^{\otimes N}$ is flip-symmetric. So an ideal sweep ends in the symmetric superposition of the two Néel states, and measuring in $z$ returns one of them at random. Either way the chain alternates.

## Research papers

- [[papers/zhang-2017-53-ion-dynamical-phase-transition|Zhang 2017 (53 ions)]]: a 53-ion Ising chain whose Fig. 2 discusses the same Z₂ (∏X) symmetry as `^ising` above.

## Sources

- [Adiabatic quantum computing: concept](../sources/week-5-02-adiabatic-quantum-computing-concept.md)
- [Expert view](../sources/week-5-03-adiabatic-quantum-computing-expert-view.md)
- Raw: [week 5](/mit-raw/week5.md)

See also [[concepts/qaoa]]: the gate-model cousin that uses the same $B = \sum X$ driver and cost operator, as discrete parameterized unitaries.
