---
title: "Factoring with a quantum computer: shor's algorithm"
type: source
week: 2
raw: mit-raw/week2.md
---

# Factoring with a quantum computer: shor's algorithm

Source page from week 2. [Raw week 2](/mit-raw/week2.md)

## Learn

The security of the RSA cryptosystem is premised on a one-way function
that is difficult to invert using a classical computer. However, using
Shor\'s algorithm, a quantum computer can perform this task much more
efficiently. In this video, you will learn how Shor\'s algorithm works.

### Classical and Quantum Fourier Transforms

The Quantum Fourier Transform (QFT) is an important operation that is
used to do period finding in Shor\'s Algorithm, as well as in the phase
estimation algorithm. In this text unit we will learn how the QFT works.
We will start off learning about the classical Fourier Transform and the
Discrete Time Fourier Transform to build some intuition about how
operations like this work.

#### The (continuous) Classical Fourier Transform 

Imagine we have a periodic function of time with period . A field of
study called Fourier Analysis says that a function can be written as

for given by

So we can re-write in terms of a series of sines and cosines with
coefficients . (If you\'re familiar with a Taylor series, this is quite
similar. In a Taylor series we rewrite a function as a sum of
polynomials. Here we are rewriting a function as a sum of sines and
cosines.) This equation for comes from the Fourier Transform.

The Fourier Transform allows us to translate a function back and forth
between the time domain (where it is written as a function of time) and
the frequency domain (where it is written as a function of frequency).
The Fourier Transform of a function of time is a function of frequency
given by

Compare this to the equation for above and you\'ll see that if you
restrict the integral to the period

If you have a sine function with a frequency , like , then using the
Fourier Transform to move to the frequency domain will give you a
function that is simply a spike (a [delta function](https://en.wikipedia.org/wiki/Dirac_delta_function))
at .

Similarly, a Fourier Transform of a weighted sum of sine functions will
give you a set of spikes in frequency space. The Fourier Transform of
will give spikes at , and .

The Classical Fourier Transform is a fascinating mathematical operation
that is at the core of quantum mechanics as well as signal processing.
We did not even get close to doing it justice here, but the main
takeaway is that the Fourier Transform can take a function and break it
up into its different frequency components.

#### The Classical Discrete Time Fourier Transform

The classical Discrete Time Fourier Transform (DTFT) is like the
continuous [Fourier Transform](https://en.wikipedia.org/wiki/Fourier_transform)
except it acts on vectors instead of continuous functions. The DTFT
takes a vector of numbers as an input -- typically a digital sampling of
a time-domain signal being analyzed -- and outputs a vector of numbers
that is its frequency-domain representation:

where is the total number of points in the vector . This transform is
used ubiquitously in the analysis of signals, because periodic behavior
in the time domain is more easily identified in the transformed
frequency domain. For example, a sinusoidal signal in time with a
frequency will transform to spikes at in the frequency domain; find the
spikes, and you know the frequency of the input signal (or,
equivalently, the inverse of its period).

Naively, implementing the DTFT takes time (where is the length of the
input vector), which can be impractical for large vectors. So in most
applications the DTFT is implemented using the Fast Fourier Transform
(FFT) which can calculate the DTFT in time.

#### The Quantum Fourier Transform

The Quantum Fourier Transform (QFT) -- is essentially the same
transformation as the Discrete Time Fourier Transform. It takes a single
quantum state and transforms it to a superposition of states, each with
specific phase factors:

where is the total number of states ; for qubits, . If we start with a
superposition of states with coefficients , then the QFT yields an
output superposition of states with coefficients ,

where the output amplitudes are the DTFT of the input coefficients .
And, due to quantum parallelism and quantum interference, the QFT can be
implemented using only gates. This is exponentially faster than the Fast
Fourier Transform (FFT) algorithm used to calculate the classical DTFT,
which requires gates.

This sounds terrific -- and it is -- but there is an important caveat.
In general, the QFT cannot be used as a straightforward replacement for
the DTFT for real-world data processing applications, and the reason is
related to quantum measurement. In the case of the classical DTFT, even
for a real input vector , the transformed output vector is in general
complex. And, furthermore, we can classically access all of the complex
elements of .

In contrast, in the case of the QFT, a measurement of the output
superposition state will project the system into only one of those
states with a probability that is the magnitude squared of the
corresponding coefficient. We generally have no access to the complex
probability amplitudes . Even if we identically prepare the system and
measure it many times, we can only reconstruct the magnitude squared of
those coefficients (the magnitude squared of the Fourier spectrum); we
have no access to the phase information, and it will take an
exponentially large number of measurements to reconstruct the
probability for all states.

Nonetheless, the QFT is a critical element in quantum computing
protocols, including phase estimation and period finding. For these
types of applications, the desired output from the QFT is highly
localized into a few states with high probability, and these states
encode the desired information, for example, the period of modular
exponentiation used in Shor\'s algorithm.

One feature of the QFT to be aware of: If you apply the QFT to a state
were all qubits are 0. , you get an equal superposition state. So . In
some papers when preparing an initial equal superposition state, authors
will write rather than as we have been doing in this course.

## Notes for the wiki

- Frames from this page's video were moved next to the matching SRT cue in the raw file when a player timestamp was read.
- Equations are display math (`$$...$$`). Diagrams may still be an image plus a text description.
- This page is immutable source commentary. Synthesis belongs in `wiki/concepts/`.
