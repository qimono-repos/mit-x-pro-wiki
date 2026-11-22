---
title: Photon sources, beam splitters and detectors
type: concept
aliases: [single photons, beam splitter, polarizing beam splitter, PBS, SPDC, spontaneous parametric down-conversion, BBO]
---

# Photon sources, beam splitters and detectors

Photonic QKD and teleportation need three kinds of hardware: sources that emit one photon (or one entangled pair) at a time, beam splitters that route photons, and detectors that click. Week 2's photonics pages define each and explain why "one photon" is harder than it sounds.

## Single-photon sources

A true single-photon source emits one, and only one, photon at a time; it is non-classical light. One route is **attenuated laser light**: classical, mostly empty pulses, with a small but nonzero chance of two photons. The other is **spontaneous emission from a two-level system** (quantum dots, quantum wells, atoms or molecules), with random emission times governed by the excited-state lifetime ([source note](../sources/week-3-01b-single-photon-sources-and-detectors.md)). ^single-photon-sources

**Detector efficiency.** A single-photon detector "clicks" on absorption. Its internal quantum efficiency is the probability that a photon entering the detector is actually detected, and noise must be distinguished from real photons (same source). ^detectors

## Beam splitters

An ideal, lossless **50:50 beam splitter** puts a single photon into a superposition of the transmitted and reflected arms. A detection then randomly finds it in one arm, 50/50, so either output detector can click. A **polarizing beam splitter (PBS)** instead routes by polarization: the $|H\rangle$ component is transmitted, the $|V\rangle$ component is reflected. For a photon that is purely $|H\rangle$, only the transmission-port detector can click (raw week 3, Beam Splitters CYU stem, ~line 1592). ^beam-splitters

## Entangled pairs: spontaneous parametric down-conversion (SPDC)

A strong pump beam through a **non-linear crystal** (BBO, beta barium borate) has a *small probability* that one pump photon converts into two, signal and idler. A linear system cannot convert frequencies; that is why the crystal must be non-linear. Energy conservation makes each half the pump frequency; momentum conservation makes their directions correlated ([raw week 3](/mit-raw/week3.md), entangled sources transcript, ~3:06–4:04). ^spdc-basics

**Type I vs. Type II.** In a **type-I** crystal the two down-converted photons have the *same* polarization. In a **type-II** crystal (BBO) they have *opposite* polarizations and leave on two cones. Keeping only the photons where the cones cross erases the which-polarization information, giving the entangled state $|HV\rangle + e^{i\phi}|VH\rangle$. The phase is tuned to 0 by phase-matching, crystal thickness or a phase shifter (same transcript, ~4:08–5:31). ^spdc-types

Correlation alone doesn't prove entanglement: a source that randomly emits classical $|HV\rangle$ or $|VH\rangle$ gives the same results in one basis. You need measurements in other bases too (same transcript, ~7:32). ^correlation-not-proof

## Sources

- [Single-photon sources and detectors](../sources/week-3-01b-single-photon-sources-and-detectors.md)
- [Entangled photon sources and detectors](../sources/week-3-03-entangled-proton-sources-and-detectors.md)
- See [[concepts/photon-polarization-qubits]], [[concepts/bb84]], [[concepts/ekert91]]
