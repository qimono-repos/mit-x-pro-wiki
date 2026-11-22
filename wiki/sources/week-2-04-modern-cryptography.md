---
title: "Modern cryptography"
type: source
week: 2
raw: mit-raw/week2.md
---

# Modern cryptography

Source page from week 2. [Raw week 2](/mit-raw/week2.md)

## Learn

We generate and communicate tremendous amounts of digital data every
day. But, how do we protect this data from eavesdroppers? In this video,
you will learn about modern cryptography and how it is used to protect
data through the use of encryption.

### The Engima Machine and Modern Cryptography

The Enigma machine is a legendary cipher machine used by German forces
before and during World War II. Enigma is an electro-mechanical rotor
cipher machine. A message -- called \"plaintext\" -- written by an
operator is encoded by a machine -- similar to a typewriter in
appearance -- in the following manner: a single character is
pseudo-randomly replaced with a different letter according to the wiring
of the machine. The subsequent letter is replaced following the same
mechanism, but with the rotor shifted to a different position. The
shifted rotor position causes the letter to be substituted according to
a different electrical pathway and hence character substitution table.
Thus, each character of the message is replaced according to a different
encoding scheme. The resulting \"ciphertext\" can subsequently be
transmitted via regular public communication channels, and it can only
be decoded using a machine with the same configuration and capability to
reverse the encoding. Finally, a successful decipher trial reveals the
true content of the message in the form of a plaintext again.

In 1941, at Bletchley Park, a British team including Alan Turing
uncovered the working principles of Enigma for the Allies. The
deciphered information of the intercepted messages provided the Allies
with a significant advantage that ultimately became a key element in
their victory over the Axis powers.

The Enigma machine is an example of a *symmetric encryption* scheme,
where the same key is used to encode and decode a message. Symmetric
encryption schemes are still in use today. However, since World War II,
crypotgraphic key generation has evolved from electro-mechanical methods
to classically constructed digital bit strings serving as encrypting
keys. The keys are mathematically difficult to derive and require a
significant amount of computational power and time. The computational
power and time required to decode determines the security of an encoding
key.

In 1975, the Data Encryption Standard (DES) was introduced by IBM. The
DES algorithm generates a 56-bit symmetric encryption key using a
complex mathematical method. Despite this mathematical complexity, DES
was known from the beginning to be potentially susceptible to a
brute-force key-search attack due to its relatively limited key size. In
fact, by the beginning of the 21st century, computational power had
sufficiently advanced to the point that one could determine the key in
less than a day. For example, Distributed.Net -- an organization
specializing in the use of idle computer time -- utilized more than
100,000 computers ranging from slow PCs to powerful multiprocessor
machines to test 250 billion keys per second and thereby determine a
particular 56-bit key in about 23 hours. Given the increasing
vulnerability of DES, in 2001, DES was replaced by the Advanced
Encryption Standard (AES), a more secure symmetric key cryptography
scheme.

However, there remained a conundrum: how can two parties exchange a
symmetric key to initiate secure communication, before they have a
secure channel on which to send it? In 1976, a new method for
distributing cryptographic keys was introduced by Whitfield Diffie and
Martin Hellman -- referred to as the Diffie-Hellman key exchange
protocol -- which heralded the era of *public key cryptography* with
*asymmetric keys*. Asymmetric keys comprise a *public key* -- used to
encrypt messages -- and a mathematically related (but unique) *private
key* -- used to decrypt messages. The security of public key
cryptosystems is premised on the use of *one-way mathematical functions*
to create the public and private keys. One-way mathematical functions
are straightforward to calculate in the forward direction, but
prohibitively complex to calculate in the inverse direction. A widely
used public-key distribution algorithm was published in 1978 by Ronald
Rivest, Adi Shamir, and Len Adleman -- referred to as the RSA algorithm.
It was later declassified in the late 1990\'s that asymmetric encryption
schemes like RSA had already been developed by the British Government
Communications Headquarters (GCHQ) in the early 1970\'s. With public key
cryptosystems, one could exchange public keys and thereby establish a
secure link, without having symmetric keys in hand at the beginning.
Once a secure link was established, one then has the option of
continuing to communicate using asymmetric keys, or one can
alternatively use this newly established secure link to exchange
symmetric keys and use symmetric encryption/decryption protocols.

In practice, public-key encryption techniques are primarily used to
establish a secure channel and distribute symmetric keys, which are in
turn used to encrypt messages. This is because encryption using an
asymmetric-key protocol is generally less resource efficient than using
a symmetric-key protocol. For example, a -bit symmetric key has
different possible key combinations. In contrast, a -bit asymmetric key
can leverage only the fraction of the possible bit strings that comply
with the conditions required by the underlying one-way function.
Therefore, whereas a symmetric key of bits and a bit public key afford a
similar level of security, the symmetric-key approach is generally more
efficient to implement.

## Notes for the wiki

- Frames from this page's video were moved next to the matching SRT cue in the raw file when a player timestamp was read.
- Equations are display math (`$$...$$`). Diagrams may still be an image plus a text description.
- This page is immutable source commentary. Synthesis belongs in `wiki/concepts/`.

## Related concepts

- [[concepts/rsa-cryptosystem]]
