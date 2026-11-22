---
title: Modern cryptography
type: concept
aliases: [encryption, symmetric key, asymmetric key, cipher, public-key cryptography]
---

# Modern cryptography

Encryption turns readable **plaintext** into unreadable **ciphertext** using a key, and decryption reverses it. Modern schemes come in two families: **symmetric** (one shared key) and **asymmetric / public-key** (a public encryption key plus a private decryption key, linked by a one-way function).

## Vocabulary

A **cipher** is the algorithm that maps plaintext to ciphertext under a cryptographic key. Enigma was an electro-mechanical rotor cipher machine: each character of the plaintext was substituted according to the rotor wiring, and the rotor shifted after every character ([raw week 2](/mit-raw/week2.md), "Modern cryptography", ~line 741). **Encryption** produces ciphertext from plaintext; **decryption** recovers the plaintext from the ciphertext. ^cipher-terms

## Symmetric vs. asymmetric

**Symmetric:** the same key encrypts and decrypts. Course examples are Enigma, DES (1975, 56-bit key, brute-forced in about 23 h by Distributed.Net), AES (2001), and the one-time pad from Course 1's QKD discussion. ^symmetric-keys

**Asymmetric (public-key):** "a public key is used for encryption and a separate independent, private key is used for decryption," and the two are related mathematically through a one-way function (transcript, ~line 760ff). Diffie–Hellman (1976) introduced public-key key exchange; RSA (1978) is the workhorse. See [[concepts/rsa-cryptosystem]]. ^asymmetric-keys

**How they're combined in practice:** public-key encryption is "primarily used to establish a secure channel and distribute symmetric keys, which are in turn used to encrypt messages," because asymmetric encryption is more resource-intensive ([raw week 2](/mit-raw/week2.md), line 816). So everyday secure traffic, including the "financial transactions" and "online sales" the lecture lists, relies on *both* families, not on one alone. ^hybrid-in-practice

## Where quantum fits

- **Threat:** Shor's algorithm inverts the one-way functions behind public-key crypto. See [[concepts/shors-algorithm]] and [[concepts/post-quantum-cryptography]]. ^quantum-threat
- **Remedy (one of two):** quantum key distribution is a way to *exchange keys* whose security rests on physics. It is not a way to send messages by teleportation; those are different protocols. See [[concepts/bb84]], [[concepts/ekert91]] and, for comparison, [[concepts/quantum-teleportation]]. ^qkd-role

## Sources

- [Modern cryptography](../sources/week-2-04-modern-cryptography.md)
- [Classical and quantum gates from course 1](../sources/week-2-03-classical-and-quantum-gates-from-course-number-1.md): one-way-function slide and this page's CYU (raw week 2, line 714)
- [Quantum cryptography: making codes](../sources/week-3-01-quantum-cryptography-making-codes.md)
