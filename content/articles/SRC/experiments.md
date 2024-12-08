Title: Experiments 
Author: Rong
Category: projects/SRC
Date: 2024-12-08
Tags: SRC, RSA, experiments

## Session 1 
**Warm-up and RSA key Generation**

### Objective: Understand the steps in RSA key generation and create simple keys.

### Activities

+ Warm-up
    + Brief explanation of RSA (Alice, Bob, Eve and the secret message in the locked box)

+ Key Generation
    + Generate two prime numbers ($q$ and $p$)
    + Calculate 
	$$n= qp$$ and
	$$\phi(n) = (p-1)(q-1)$$
    + Pick a public exponent $(e)$ and ensure it is coprime with $\phi(n)$
    + Find the private key $(d)$, which is
        $$ ed = 1(mod \phi(n))$$
### Deliverable: Generate a small RSA key pair and save them into keyfiles individually.
-----------------------------------------------------------------------------------------

## Session2
**Encrypting and Decrypting Messages**
### Objective: Learn to encrypt and decrypt messages using the generated RSA keys.
+ Write a simple function to take the mode and message. (hint: you should start from a single character)
+ Encrypt the message using public key
+ Decrypt the encrypted text using private key

### Deliverable: Complete the publicKeyCipher.py
-----------------------------------------------------------------------------------------


## Session 3 
**Observation and Analysis**
### Objective: Observe and analyze patterns in RSA behavior and understand its strengths

+ Test the algorithm with different key sizes. (4, 8, 16, 32, 128 bits)
+ Observe how encryption time change
+ Encrypt a larger message ("helloworld")
+ (Bonus): How would you attempt to brute-force and crack the code.

### Deliverable: submit your observations and conclusion 
