Title: Introduction to Encryption
Author: Rong
Date: 2024-12-03
Tags: SRC, encryption


## Objective
+ Understand basic cryptographic principles  
+ Understand the difference between symmetric and asymmetric encryption 
+ Learn basic concepts: plaintext, ciphertex and keys.

## Lesson Plan
+ Brief history of encryption.
    + Caesar cipher: 
    + Enigma: 
+ Symmetric encryption
    + Caesar cipher
    + AES
+ Asymmetric encryption (public-key cryptosystem,) 
    + RSA (Rivest–Shamir–Adleman)
    + EEC (Elliptic-curve cryptography (ECC) )

## Reading Materials
+ [Engima Machine](https://brilliant.org/wiki/enigma-machine/)

## Activities and exercises
1.Caesar cipher implementation in Python
    + Write a function caesar_encryption() that encrypts message by alphabet shift. 
```python
def caesar_cipher(msg: str, shift: int):
    
    for a in msg:
        if ...
    
    return cipher_text
``` 
2. Vigenère ciphers implementation
    + Write a function vigenere_cipher() that encrypts message by shifting a entire block after a "key-word"
```python
def vigenere_cipher(msg: str, keyword: str):

    return cipher_text



```


