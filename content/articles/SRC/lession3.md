Title: RSA   
Author: Rong
Date: 2024-11-30
Tags: SRC, encryption


## Objective
+ Learn about prime numbers, factorizations, modulus and Euclid's algorithm.
+ Understand modular exponentiation and modular inversion.
+ Learn the steps to generate RSA keys
+ Implement a simple RSA encryption and decryption algorithm. 

## Math behind RSA
+ The math behind RSA is 
    + $C = M^e \; mod \; n$
    + $M = C^d \; mod \; n$
        


## Activities:

+ Key Generating 
    + Complete function *isPrime()*, which checks if a number is prime number. (primeNum.py)
    + Implment a function *generateLargePrime()* for generating large prime numbers (primeNum.py).
    + Implment a function for Eucild's algorithm (cryptomath.py). 
    + Implment a function for modular inversion (cryptomath.py).   
    + Use the above function to generate public key and private key pairs (makePublicPrivatekeys.py). 
Implement a function for modular exponentiation.
+ Calculate e, d and n for a simple RSA setup.
+ implmentation of RSA encryption and decryption
+ Test

  
