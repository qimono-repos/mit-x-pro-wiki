---
title: Adiabatic quantum computing
type: concept
---

# Adiabatic quantum computing

An adiabatic algorithm encodes the answer as the ground state of a problem Hamiltonian $H_p$ and reaches that state by a slow interpolation from an easy driver Hamiltonian $B$.

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

with $0 \le t \le T$ and $T$ the total runtime. The initial ground state of $B$ is the uniform superposition (every spin in $|+\rangle$), which is easy to prepare. If $T$ is large compared with the inverse square of the minimum spectral gap along the path, the adiabatic theorem keeps the system in the instantaneous ground state, which at $t = T$ is a ground state of $H_p$.

The lecture's caveat: for a large enough problem the minimum gap is so small that the required $T$ is impractical, and once the gap drops below the thermal energy $k_B T$ the environment kicks the system out of the ground state. That limitation is why the course distinguishes this closed-system ideal from [[concepts/quantum-annealing]].

## Sources

- [Adiabatic quantum computing: concept](../sources/week-5-02-adiabatic-quantum-computing-concept.md)
- [Expert view](../sources/week-5-03-adiabatic-quantum-computing-expert-view.md)
- Raw: [week 5](/mit-raw/week5.md)
