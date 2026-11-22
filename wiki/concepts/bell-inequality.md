---
title: Bell inequality
type: concept
---

# Bell inequality

A Bell inequality is a numerical bound that any local hidden-variable model must obey, and that entangled quantum measurements can violate. The course uses the CHSH form. Alice's observables are $A, A'$ and Bob's are $B, B'$, each with outcomes $\pm 1$. Local realism implies

$$
\bigl|\langle AB \rangle + \langle AB' \rangle + \langle A'B \rangle - \langle A'B' \rangle\bigr| \le 2.
$$

Quantum mechanics on the singlet (or $\Phi^+$) reaches $2\sqrt{2}$ for the right pair of bases. A measured value above 2 cannot be explained by shared classical randomness alone. ^chsh

Week 3 uses that violation twice: as the test inside [[concepts/ekert91]], and as the certificate in randomness expansion. If the devices violate a Bell inequality, their outputs contain private randomness even when you do not trust the internal description of the devices (device-independent randomness).

## Local realism and the loopholes

What a violation rules out is **local realism**. "The local part just says that you can't send out information faster than the speed of light. And realism means that things have definite properties that exist independently of whether or not we choose to measure them" ([raw week 3](/mit-raw/week3.md), Bell transcript, ~3:54). ^local-realism

**Loopholes** are "ways in which nature could trick us into thinking local realism is incorrect when in fact, it's not" (~4:52). The course names three (~5:00–5:53):
- **Locality:** neither side may learn the other's basis in time. Alice and Bob must be far enough apart that the information about Alice's basis can't reach Bob before he chooses his.
- **Free choice:** the basis selections must be uncorrelated with any classical variable; they have to be made "of their own free will."
- **Detection:** enough of the pairs must be measured that you aren't looking only at a subset that happens to violate the inequality.

^loopholes


## Sources

- [Bell's inequality](../sources/week-3-06-bell-s-inequality.md)
- [Certifiable random numbers](../sources/week-3-07-bell-s-inequality-and-certifiable-random-number-generation.md)
- Raw: [week 3](/mit-raw/week3.md)
