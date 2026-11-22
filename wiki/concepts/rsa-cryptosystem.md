---
title: RSA cryptosystem
type: concept
aliases: [RSA, public-key cryptography, asymmetric encryption]
---

# RSA cryptosystem

RSA is the standard public-key cryptosystem. Anyone can encrypt with the public pair $(e, N)$, but decrypting needs $d$, and computing $d$ from $(e, N)$ requires factoring $N = pq$. Its security therefore rests on one assumption: multiplying $p \times q$ is easy, while recovering $p$ and $q$ from $N$ is hard for a classical computer. That assumption is exactly what [[concepts/shors-algorithm]] breaks.

## Why public keys exist at all

The course reaches RSA through the history of *symmetric* encryption, where one key both encrypts and decrypts: Enigma, then DES (1975, a 56-bit key brute-forced in about 23 hours by Distributed.Net), then AES (2001). Symmetric schemes leave a chicken-and-egg problem: how do two parties share a key before they have a secure channel to send it over? Diffie–Hellman (1976) started *asymmetric* cryptography: a public key to encrypt and a related but different private key to decrypt, linked by a **one-way function**. RSA (Rivest, Shamir, Adleman, 1978) became the workhorse. In practice, public-key crypto mostly sets up a channel and hands over a symmetric key, and the bulk data then goes through the symmetric cipher, because asymmetric encryption costs more ([raw week 2](/mit-raw/week2.md), line 816). → [Modern cryptography](../sources/week-2-04-modern-cryptography.md)

The one-way function, as drawn in the lecture:

$$
p \times q \;\xrightarrow{\text{easy}}\; N
\qquad\qquad
N \;\xrightarrow{\text{hard}}\; ?\times ?
$$

## The four steps

The course splits RSA into: (1) key generation, (2) public-key distribution, (3) encryption and transmission, (4) decryption. → [RSA cryptosystem](../sources/week-2-05-rsa-cryptosystem.md)

**Key generation (Alice).** These are the slide formulas from [raw week 2](/mit-raw/week2.md), "Determining e and d":

$$
\begin{aligned}
&1.\ \text{choose distinct primes } p, q \\
&2.\ N = pq \\
&3.\ r = (p-1)(q-1) \\
&4.\ \text{choose } e \text{ with } \gcd(e, r) = 1 \\
&5.\ d = e^{-1} \bmod r \quad\Longleftrightarrow\quad e\,d \equiv 1 \pmod r
\end{aligned}
$$

**Alice keeps private:** $p, q, r, d$. **Alice publishes:** $e, N$. A common choice is $e = 2^{16}+1 = 65\,537$, binary `10000000000000001`. Only two bits are set, so encryption by repeated squaring is cheap.

**Encryption (Bob) and decryption (Alice):**

$$
c = m^{e} \bmod N
\qquad\qquad
c^{d} = \left(m^{e}\right)^{d} = m^{ed} \equiv m \pmod N \quad (m < N)
$$

**Eve** sees $c$, $e$ and $N$. Without $d$ she has no shortcut, and getting $d$ means getting $r$, which means factoring $N$.

### Notation trap: $e^{-1}$ is not $1/e$

$d = e^{-1} \bmod r$ is the **modular multiplicative inverse**: the integer $d$ with $e\,d \bmod r = 1$. It is not a reciprocal. The course warns about this explicitly. In a calculator, type `A^(-1) mod C`, never `1/A mod C`.

## Why decryption works: the period

The engine of RSA is that **modular exponentiation is periodic**. The course's slide example uses $N = 10 = 2 \times 5$, $x = 3$:

$$
3^{i} \bmod 10:\quad 3,\ 9,\ 7,\ 1,\ 3,\ 9,\ 7,\ 1,\ \dots \qquad\Rightarrow\qquad r = 4
$$

and $(p-1)(q-1) = 1 \times 4 = 4$. In general, the sequence $x^{i} \bmod N$ has a period that **evenly divides $(p-1)(q-1)$**. This is Euler's totient $\varphi(N)$, via Fermat's little theorem. So $x^{(p-1)(q-1)} \equiv 1$. The course adds that $(p-1)(q-1)$ may be a multiple of the fundamental period, which is $\operatorname{lcm}(p-1, q-1)$, and that either works.

Decryption then follows in one line. Since $e\,d = 1 + k\,(p-1)(q-1)$ for some integer $k$:

$$
m^{ed} = m \cdot \left(m^{(p-1)(q-1)}\right)^{k} \equiv m \cdot 1^{k} = m \pmod N .
$$

## Worked example (own numbers, not from the course)

These are tiny primes for hand-checking. They are deliberately **not** the graded numbers ($p=101$, $q=113$, $e=3533$) from the course's check-your-understanding question and Week 1 quiz. Work those yourself.

| Step | Value |
|---|---|
| $p, q$ | $3, 11$ |
| $N = pq$ | $33$ |
| $r = (p-1)(q-1)$ | $2 \times 10 = 20$ (fundamental period $\operatorname{lcm}(2,10) = 10$) |
| $e$ | $3$, and $\gcd(3, 20) = 1$ ✓ |
| $d = 3^{-1} \bmod 20$ | $7$, since $3 \times 7 = 21 \equiv 1$ |
| encrypt $m = 4$ | $c = 4^{3} \bmod 33 = 64 \bmod 33 = 31$ |
| decrypt | $31^{7} \bmod 33 = 4$ ✓ |

Checked in Python with `pow(4,3,33)`, `pow(3,-1,20)` and `pow(31,7,33)`.

## Where quantum enters: the same period, seen from the attacker's side

Eve's problem is "find $r$ without knowing $p, q$". [[concepts/shors-algorithm]] reduces factoring to **order finding**: pick a random $g$, find the period $r_g$ of $g^{x} \bmod N$ with [[concepts/period-finding]] (the quantum part, using the [[concepts/quantum-fourier-transform]]), then classically compute $\gcd(g^{r_g/2} \pm 1,\ N)$. With $p$ and $q$ in hand, Eve computes $(p-1)(q-1)$ and then $d$ exactly as Alice did.

Run that on the toy $N = 33$ (own numbers):

- $g = 5$: order $r_g = 10$; $5^{5} \bmod 33 = 23$; $\gcd(22, 33) = 11$ and $\gcd(24, 33) = 3$. **Factored.**
- $g = 2$: order $r_g = 10$, but $2^{5} \bmod 33 = 32 \equiv -1$, so the gcds give only $1$ and $33$. **Trivial: discard $g$ and draw again.** This is the failure branch on [[concepts/shors-algorithm]].

> **Same letter, two meanings.** The course uses $r$ for both things. On the RSA slides, $r = (p-1)(q-1)$, the totient that Alice computes from $p$ and $q$. In Shor, $r$ is the order of one particular $g$, which divides the totient and is often smaller ($10$ vs. $20$ above). Keep them apart: Alice *knows* the totient, Eve *measures* an order.

The course sums it up as: "the challenge of order finding can be related to the problem of factoring." Classically that is hard. On a fault-tolerant quantum computer it is polynomial, which is why [Post-Quantum Cryptography](../sources/week-3-01a-post-quantum-cryptography.md) exists.

## Course conflicts (recorded, not resolved)

- **Range of $e$.** The "Determining e and d" slide says $3 \le e \le r$. The key-generation summary slide says $3 \le e \le N-1$. Both require $\gcd(e, r) = 1$, which is the condition that matters. Logged in `wiki/log.md`, 2026-11-22.
- **Dropped inline math.** The Learn prose on the RSA page lost every inline symbol in the Doc export ("two distinct prime numbers and are chosen at random"). This page takes its formulas from the slides, which are intact.

## Graded items that use this concept

- CYU *RSA Key Generation* (4 points): [raw week 2](/mit-raw/week2.md), line 1981
- Week 1 Quiz Q1 *RSA Encryption*, Q2 *RSA Decryption*: [Week 1 quiz](../sources/week-1-15-modern-cryptography-and-shor-s-algorithm-quiz.md)
- See [quiz inventory](../analyses/quiz-inventory.md)

## Sources

- [Modern cryptography](../sources/week-2-04-modern-cryptography.md): Enigma → DES → AES, the key-distribution problem, Diffie–Hellman, one-way functions
- [RSA cryptosystem](../sources/week-2-05-rsa-cryptosystem.md): the four steps, modular exponentiation, $3^i \bmod 10$, $e$ and $d$
- [Factoring with a quantum computer: Shor's algorithm](../sources/week-2-06-factoring-with-a-quantum-computer-shor-s-algorithm.md): why RSA falls
- [Classical and quantum gates from course 1](../sources/week-2-03-classical-and-quantum-gates-from-course-number-1.md): the one-way-function and Alice/Bob/Eve slides sit in this page's raw range (week 2, lines 686–712), together with the Modern Cryptography check-your-understanding question (line 714)
- Raw: [week 2](/mit-raw/week2.md), headings "One-way functions", "RSA Algorithm", "Modular Exponentiation and RSA Cryptosystem", "Exponentiation and modular arithmetic", "Determining e and d"
