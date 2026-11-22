---
title: Experimental demonstrations of Shor's algorithm
type: concept
aliases: [Shor demonstrations, factoring 15, NMR Shor, trapped-ion Shor, pretending to factor]
---

# Experimental demonstrations of Shor's algorithm

Every hardware demonstration of Shor's algorithm so far factors tiny numbers, mostly 15. What makes one demonstration meaningful rather than theatre is how much of the order-finding circuit it actually runs. The Week 1 case study walks through NMR (2001), trapped ions (2016) and the "pretending to factor" critique (2013).

## NMR, IBM, 2001: seven qubits for N = 15

Factoring 15 started as a PhD challenge from Ike Chuang in 1998, after the first two-qubit NMR algorithms on chloroform. The final experiment used **seven qubits**: nuclear spins in a custom molecule, controlled with a four-channel NMR spectrometer, run in fall/winter 2000–2001 at IBM. The analysis of the circuit showed that "only seven qubits are needed to realize Shor's algorithm for factoring 15," for both the easy and the hard case of the base ([raw week 1](/mit-raw/week1.md), NMR pages, ~lines 3410–4590). ^nmr-2001

## Trapped ions, 2016: Kitaev QFT plus qubit recycling

Monz, Chuang, Blatt et al. replaced the multi-qubit QFT with **Kitaev's serial, single-qubit version**, which uses feed-forward from mid-circuit measurements. One control ion is measured and re-prepared ("recycled") several times, while other ions act as quantum memory. The general count in the lecture is $\log N + 1$ qubits ("for 15, this works out to five bits as the minimum"). The results slide lists the hard case as **"Feed-forward · 5 ions · Fredkins, CNOTs"** ([raw week 1](/mit-raw/week1.md), trapped-ion pages, ~lines 6876–9500). ^trapped-ions-2016

## "Pretending to factor": the compilation trap

If you already know the answer, you can choose the base $a$ so that $r = 2$ (the "easy case") and compile the circuit down to almost nothing. The lecture's slide lists photonic $N = 21$ (2011), superconducting $N = 15$ with 3 qubits and 2 CNOTs (2012), and "compiled factoring with one qubit". Smolin, Smith and Vargo (*Nature* 499, 2013) made the point explicitly: over-compiled demonstrations prove very little ([raw week 1](/mit-raw/week1.md), "pretending to factor", ~line 9440). ^pretending-to-factor

## Sources

- [Demonstrations: introduction](../sources/week-1-07-demonstrations-of-shor-s-algorithm-introduction.md)
- [NMR](../sources/week-1-08-demonstrations-of-shor-s-algorithm-shor-s-algorithm-with-nmr.md), [Perspective on NMR](../sources/week-1-09-demonstrations-of-shor-s-algorithm-perspective-on-nmr.md)
- [Trapped ions: challenge](../sources/week-1-10-demonstrations-of-shor-s-algorithm-quantum-factoring-with-trapped-ions-challenge.md), [ion trap](../sources/week-1-11-demonstrations-of-shor-s-algorithm-quantum-factoring-with-trapped-ions-ion-trapp.md), [results](../sources/week-1-12-demonstrations-of-shor-s-algorithm-quantum-factoring-with-trapped-ions-experimen.md)
- [Pretending to factor](../sources/week-1-13-demonstrations-of-shor-s-algorithm-pretending-to-factor.md)
- See [[concepts/shors-algorithm]], [[concepts/quantum-fourier-transform]]
