import requests
from pwn import *
from os import urandom
"""
    According to CBC decryption, we see:
    if ciphertext[:16] (block 1) = ciphertext_block2[16:32] (block 2)
    => iv  = ciphertext[:16] (+) plaintext[16:32]
    iv = KEY 
    => KEY = ciphertext[:16] (+) plaintext[:16] (+) plaintext[16:32]

    We create the same block ciphertext by: urandom(16) * 2
"""
def encrypt(plaintext):
    url = f"http://aes.cryptohack.org/lazy_cbc/encrypt/{plaintext}/"
    return requests.get(url).json().get("ciphertext", None)

def receive(ciphertext):
    url = f"http://aes.cryptohack.org/lazy_cbc/receive/{ciphertext}/"
    r = requests.get(url).json()
    try:
        temp = r["error"]
    except:
        return r.get("success", None)
    return r.get("error", None)

def get_flag(key):
    url = f"http://aes.cryptohack.org/lazy_cbc/get_flag/{key}/"
    r = requests.get(url).json()
    try:
        temp = r["error"]
    except:
        return r.get("plaintext", None)
    return r.get("error", None)

ciphertext = urandom(16).hex() * 2

plaintext = receive(ciphertext)[len("Invalid plaintext: "):]
KEY = xor(bytes.fromhex(ciphertext[:32]), bytes.fromhex(plaintext[:32]), bytes.fromhex(plaintext[32:])).hex()
print(bytes.fromhex(get_flag(KEY)).decode())




