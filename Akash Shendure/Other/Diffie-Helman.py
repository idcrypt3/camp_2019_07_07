# From iD Game Plan

def apply_shift(plaintext, key):
    cipher = ""
    for c in range(len(plaintext)):
        number = ord(plaintext[c])
        number += key
        cipher += chr(number)
    return cipher

def remove_shift(ciphertext, key):
    message = ""
    for c in range(len(ciphertext)):
        number = ord(ciphertext[c])
        number -= key
        message += chr(number)
    return message

def find_shared_key(private_key, public_key):
    shared_key = public_key ** private_key % public_modulus
    return shared_key

public_base = 8
public_modulus = 29