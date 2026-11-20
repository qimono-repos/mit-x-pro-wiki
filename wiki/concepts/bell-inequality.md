---
title: Bell inequality
type: concept
---

# Bell inequality

A Bell inequality is a numerical bound that any local hidden-variable model must obey, and that entangled quantum measurements can violate. The course uses the CHSH form. Alice's observables are $A, A'$ and Bob's are $B, B'$, each with outcomes $\pm 1$. Local realism implies

$$
\bigl|\langle AB \rangle + \langle AB' \rangle + \langle A'B \rangle - \langle A'B' \rangle\bigr| \le 2.
$$

Quantum mechanics on the singlet (or $\Phi^+$) reaches $2\sqrt{2}$ for the right pair of bases. A measured value above 2 cannot be explained by shared classical randomness alone.

Week 3 uses that violation twice: as the test inside [[concepts/ekert91]], and as the certificate in randomness expansion. If the devices violate a Bell inequality, their outputs contain private randomness even when you do not trust the internal description of the devices (device-independent randomness).

## Sources

- [Bell's inequality](../sources/week-3-06-bell-s-inequality.md)
- [Certifiable random numbers](../sources/week-3-07-bell-s-inequality-and-certifiable-random-number-generation.md)
- Raw: [week 3](/mit-raw/week3.md)
