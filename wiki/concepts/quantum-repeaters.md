---
title: Quantum repeaters
type: concept
aliases: [repeater, entanglement swapping, fiber loss, attenuation]
---

# Quantum repeaters

Fiber loses photons. Classical links fix that with amplifiers, but the no-cloning theorem forbids amplifying an unknown quantum state. A quantum repeater instead distributes **entanglement** over short segments and stitches the segments together, then uses the long-distance entangled pair as a resource, e.g. for teleportation.

## Why amplifiers don't work

Classical "repeater stations" boost the signal along the line. Amplifying a single photon's unknown quantum state would copy it into more photons carrying the same quantum information, which the no-cloning theorem forbids ([raw week 3](/mit-raw/week3.md), repeaters Learn, ~line 11062). ^no-amplification

## How bad fiber loss is

Silica fiber loses light to **Rayleigh scattering** (dominant at short wavelengths) and **material absorption** (dominant at long wavelengths). The combined minimum is ≈0.2 dB/km near 1550 nm. Loss per km is roughly constant, so **total attenuation in dB is proportional to distance**. The transmitted *power* therefore falls exponentially: about 95% remains after 1 km, about 1% after 100 km, and at 500 km (100 dB) only 1 in $10^{10}$ photons arrives (same Learn section). ^fiber-loss

## The repeater idea

Make two entangled pairs, each spanning $L/2$, and combine them at the middle node so the end nodes share one entangled state spanning $L$. Nest the step as often as needed. "The final entangled state distributed by quantum repeaters can be used as a resource for any quantum communication protocol," for example to teleport an unknown state over the full distance deterministically (same Learn section). ^repeater-idea

## Sources

- [Quantum repeaters](../sources/week-3-08a-quantum-repeaters.md)
- [Quantum teleportation](../sources/week-3-08-quantum-teleportation.md)
- See [[concepts/quantum-teleportation]], [[concepts/photon-polarization-qubits]]
