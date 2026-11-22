---
title: Photon polarization as a qubit
type: concept
aliases: [polarization qubit, H V basis, diagonal basis, polarizer, half-wave plate, waveplate, Bell state photons]
---

# Photon polarization as a qubit

Polarization is a two-level system, so a photon is a natural qubit: $|H\rangle \leftrightarrow |0\rangle$, $|V\rangle \leftrightarrow |1\rangle$. Polarizers act as measurements, and waveplates act as single-qubit gates. Every photonic protocol in Week 2 is built from these pieces.

## The mapping

The course gives the dictionary $|0\rangle \to |H\rangle$, $|1\rangle \to |V\rangle$, with diagonal states on the Bloch-sphere equator:

$$
|{\nearrow}\rangle = \tfrac{1}{\sqrt2}(|H\rangle + |V\rangle), \qquad |{\searrow}\rangle = \tfrac{1}{\sqrt2}(|H\rangle - |V\rangle)
$$

So $\{H, V\}$ is the rectilinear ($Z$) basis and $\{+45°, -45°\}$ is the diagonal ($X$) basis (raw week 3, quiz Q4 stem, ~line 11243). ^polarization-mapping

## Polarizers as measurements

A polarizer along direction $\theta$ transmits the component of the state along $\theta$, with probability $|\langle\theta|\psi\rangle|^2$. After transmission the photon *is* polarized along $\theta$. Measuring $|H\rangle$ with a $\pm 45°$ polarizer gives each outcome with probability $|\langle \pm45|H\rangle|^2 = 1/2$, because the bases are mutually unbiased. (Standard Born-rule background, used by the course's BB84 and entanglement questions.) ^polarizer-measurement

## Entangled pairs measured far apart

For $\tfrac{1}{\sqrt2}(|H\rangle_A|H\rangle_B + |V\rangle_A|V\rangle_B)$: when Alice's $H$-polarizer transmits, the joint state collapses to $|H\rangle_A|H\rangle_B$, and Bob's photon is now $|H\rangle$ wherever he is. What Bob then sees follows from the polarizer rule above applied to $|H\rangle$. If Alice's polarizer is $V$ instead, Bob's photon is $|V\rangle$, and the same reasoning applies. This works at any distance (Moon, Mars), but it gives no way to signal, because Bob's local statistics alone don't reveal Alice's choice. ^entangled-pair-measurement

> **Conflict (course model vs physics), recorded 2026-11-22.** The course's entanglement questions ask what Bob's detector "registers" after a ±45° polarizer. On the **collapse reading** the course appears to use (pre-assessment grading), Bob's photon is described by the polarization it collapsed to (H or V). On the **strict optics reading**, a photon that passes a +45° polarizer *is* +45°-polarized, and a later H/V measurement gives H or V 50/50. The two readings select different options on these questions. Check the platform's feedback before relying on either.

The course also stresses that entangled states "remain entangled even in different bases," and that a conditional two-qubit gate (CNOT) is needed to create them in the circuit model (raw week 3, entangled sources transcript, ~1:45). ^entangled-any-basis

## Waveplates as single-qubit gates

A waveplate (birefringent crystal, e.g. quartz) has a fast axis and a slow axis. The slow-axis component gains extra phase. A **half-wave plate** adds a phase of $\pi$ (half a wavelength), so it *rotates* linear polarization ([source note](../sources/week-3-03-entangled-proton-sources-and-detectors.md), "Generating Four Bell States"). With the plate's fast axis at angle $\theta$ to $H$:

$$
|H\rangle \mapsto \cos 2\theta\,|H\rangle + \sin 2\theta\,|V\rangle, \qquad |V\rangle \mapsto \sin 2\theta\,|H\rangle - \cos 2\theta\,|V\rangle
$$

(raw week 3, quiz Q4 stem). At $\theta = 0$ this is $Z$; at $\theta = 22.5°$ it is the Hadamard $H$; at $\theta = 45°$ it is $X$ (own check: plug the angle into the matrix $\begin{psmallmatrix}\cos2\theta & \sin2\theta\\ \sin2\theta & -\cos2\theta\end{psmallmatrix}$). Waveplates are also how one Bell state is converted into the other three. ^half-wave-plate

## Sources

- [Entangled photon sources and detectors](../sources/week-3-03-entangled-proton-sources-and-detectors.md)
- [Quantum key distribution: BB84](../sources/week-3-02-quantum-key-distribution-bb84.md)
- [Quantum cryptography quiz](../sources/week-3-09-quantum-cryptography-quiz-4-questions.md): Q2 and Q4 stems carry the definitions quoted above
- See [[concepts/photon-sources-and-detectors]], [[concepts/bb84]], [[concepts/quantum-teleportation]]
