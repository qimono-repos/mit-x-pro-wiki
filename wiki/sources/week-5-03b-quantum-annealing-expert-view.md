---
title: "Quantum Annealing: Expert View"
type: source
week: 5
raw: mit-raw/week5-quantum-annealing-expert-view.md
---

# Quantum Annealing: Expert View

Source page from week 5 (official Week 4): a classroom recording about D-Wave. Albert identifies the lecturer as Peter Shor. [Raw transcript](/mit-raw/week5-quantum-annealing-expert-view.md)

Missing from the original `week5.md` capture; transcript added 2026-11-22. The page's practice question is **Q1: Quantum Annealing II** ([[quizzes/week-4|Week 4 quizzes]]).

## What the video covers

- **Timeline (0:12–1:44).** D-Wave was founded in 1999. In 2000 Farhi, Goldstone, Gutmann and Sipser proposed adiabatic quantum computation, and a couple of years later Aharonov et al. showed it is universal. In 2007 D-Wave announced a 16-qubit prototype "adiabatic quantum computer", which drew a lot of skepticism (Scott Aaronson's blog). Some time later D-Wave started calling what it does *quantum annealing*.
- **Avoided crossing (2:32–3:54).** Hand-waving picture: near the crossing the two levels are superpositions of two state "structures"; the more the structures differ, the smaller the gap.
- **Student Q&A: go fast, slow down at the gap (3:54–5:07).** If you know where the avoided crossing is, you can evolve quickly most of the time and slow down only there. That's how adiabatic Grover search gets its square-root speedup: one avoided crossing with a gap of about $1/\sqrt{N}$. If you don't know where the gaps are, this is hard.
- **Why "annealing" (5:07–6:49).** D-Wave runs extremely cold, but its chips' structure still allows thermal excitations at that temperature; the temperature is probably bigger than the smallest gap. People argued it couldn't be called adiabatic quantum computation, so it was renamed quantum annealing.
- **What that costs (6:49–8:48).** Real AQC comes with a universality proof (up to a polynomial blow-up converting between models), and so a reason to claim beyond-classical power. An annealer certainly uses quantum processes, but there are no theoretical results showing it is more powerful. Whether a mathematical model of it beats classical computers: "Nobody knows."
- **Experiments (8:52–9:44).** D-Wave's claimed wins over classical computers might be a real speedup, or just a constant-factor advantage from a fast physical process. "We don't really know whether D-wave is more powerful."

## Concepts touched

[[concepts/quantum-annealing]] · [[concepts/adiabatic-quantum-computing]] · [[concepts/grovers-algorithm]]
