---
title: "RSA cryptosystem"
type: source
week: 2
raw: mit-raw/week2.md
---

# RSA cryptosystem

Source page from week 2. [Raw week 2](/mit-raw/week2.md)

## Learn

We often communicate securely by encrypting data using cryptographic
schemes. However, how do we initiate and establish a secure channel, if
we have not yet securely exchanged cryptographic keys? In this video,
you will learn about the RSA cryptosystem, a quintessential example of a
public-key cryptosystem that leverages asymmetric keys based on one-way
mathematical functions to communicate sensitive information.

### RSA Algorithm

Modern cryptography is a foundation for today\'s information and
economic security, enabling secure communication between individuals,
businesses, and governments. There are two basic classes of
cryptosystems: symmetric-key and asymmetric-key cryptography.
Asymmetric-key cryptography -- also referred to as public-key
cryptography -- uses a public key and a private key to encode and decode
messages. The two distinct keys are mathematically related via a one-way
function, which is computationally efficient to calculate in one
direction, but not in the inverse direction.

The workhorse of public-key encryption schemes is the RSA cryptosystem,
which can be broken into four steps:

1.  key generation (a public key and a private key ),

2.  public key distribution,

3.  message encryption (a message a ciphertext ) and transmission,

4.  message decryption.

**Key Generation and Distribution:**

The encryption and decryption keys are generated using a one-way
function related to *modular exponentiation*. To begin, two distinct
prime numbers and are chosen at random. Key generation then centers on
the function

  ------------------------------------------------------- ---------------

  ------------------------------------------------------- ---------------

where is an integer number, the modulus is the product of and , and
\"mod \" means \"modulo \". The term \"modular exponentiation\" refers
to there being an exponential that is calculated modulo .

From the number theory of modular exponentiation, it is known that the
function is periodic with period , and finding the value of is called
*order finding*. Order finding is a manageable task if one knows and ,
but not if one only knows their product . This is the one-way function
that underlies the security of RSA.

To see this, consider the following. When in the above function, . If is
periodic in , then it follows that the function , , , \... must also
equal 1. The period can be derived using [Fermat's little theorem](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem),
which uses [Euler's totient function](https://en.wikipedia.org/wiki/Euler%27s_totient_function)

  ------------------------------------------------------- ---------------

  ------------------------------------------------------- ---------------

to find the period .

In essence, Euler\'s totient function gives the number of positive
integers smaller than the product which have no prime factors in common
with -- that is, *coprime* with , , and -- and Fermat\'s little theorem
shows that this is the period . Note that may be the fundamental period,
or it may be an integer multiple of the fundamental period. The
fundamental period is the least common multiple of and . Both the
fundamental period or a multiple of the fundamental period will work.

With and known, the totient can be easily calculated with a classical
computer. However, if one is only given (without knowledge of or ), then
one must *factor* to find and and thereby find the period . Factoring is
a hard problem for a classical computer.

With the period in hand, one can generate the public key and private key
. One first *chooses* a *public encryption exponent* that satisfies the
following conditions:

1.  ,

2.  is coprime with .

The second condition means that there is no integer (other than 1) that
divides both and , and so their [greatest common divisor (gcd)](http://mathworld.wolfram.com/GreatestCommonDivisor.html)
is 1. This is written as .

Once a value of is chosen, then one *calculates* a *private decryption
exponent* as the modular multiplicative inverse of , modulo :

  ------------------------------------------------------- ---------------

  ------------------------------------------------------- ---------------

[**Note**]{.underline} that the notation for the modular multiplicative
inverse above, while often found, can be misleading. is another way of
writing such that . It does not mean to take the reciprocal of . When
using a [modular calculator](https://www.wolframalpha.com/input/?i=7%5E(-1)+mod+288),
you will have to use the syntax\"[A\^(-1) mod C](https://www.wolframalpha.com/input/?i=7%5E(-1)+mod+288)\"
and **[not]{.underline}** \"1/A mod C\" as the modular multiplicative
inverse is only defined for integers.

Intuitively, as we explain in more detail below, the inversion follows
from the fact that is used to decrypt a message that is encrypted using
. And, again, one can trivially calculate the private decryption
exponent given the public encryption exponent , *provided* one knows the
period .

The steps are summarized in the following table for the specific example
of and .

  -------------------------------------------------------------------------------------------------------
  1\) ,  choose two random prime numbers                                                   ,
  :                                                                                        
  ------ --------------------------------------------------------------------------------- --------------
  2\) :  calculate                                                                         

  3\) :  find the period                                                                   

  4\) :  choose a public exponent with [greatest common divisor](http://mathworld.wolfram.com/GreatestCommonDivisor.html):   
         gcd                                                                               

  5\) :  calculate the private exponent                                                    
  -------------------------------------------------------------------------------------------------------

Having created the keys, Alice sends the public key to Bob. Importantly,
she retains the private key and does not reveal the values , , or .

**Message Encryption and Decryption:**

Bob has a message he wants to send to Alice. Having received the public
encryption key , he encrypts to create cyphertext using the public key
and modular exponentiation:

  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

After the message is sent to Alice, she decrypts it with her private key
using the properties of modular exponentiation,

  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

provided the original message is smaller than the modulus . Eve has
access to the public key , but this is no use to her in trying to
decrypt the cyphertext, since

In summary, the number theory and properties of modular exponentiation
underlie the security of the RSA cryptosystem. As you have seen, the
challenge of order finding can be related to the problem of factoring.
While it is straightforward to multiple two numbers and to give the
modulus , the inverse problem is hard on a classical computer. And, if
is chosen sufficiently large, then a brute-force search to find and is
also inefficient. Thus, the RSA cryptosystem is believed to be secure
provided the prime numbers and , and the private exponent are not made
public. However, the encryption exponent and modulus *can* be made
public. This type of cryptosystem, where the encryption key is public
and anyone can encrypt a message, while the decryption key is private
and only the receiver can decrypt the cyphertext, is the backbone of our
modern day communication systems.

## Notes for the wiki

- Frames from this page's video were moved next to the matching SRT cue in the raw file when a player timestamp was read.
- Equations are display math (`$$...$$`). Diagrams may still be an image plus a text description.
- This page is immutable source commentary. Synthesis belongs in `wiki/concepts/`.
