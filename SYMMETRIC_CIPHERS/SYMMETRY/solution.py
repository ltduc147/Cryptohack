import requests
from pwn import *


def encrypt_flag():
    url = "http://aes.cryptohack.org/symmetry/encrypt_flag/"
    return requests.get(url).json().get("ciphertext", None)


def encrypt(ciphertext, iv):
    url = f"http://aes.cryptohack.org/symmetry/encrypt/{ciphertext}/{iv}/"
    return requests.get(url).json().get("ciphertext", None)

ciphertext = encrypt_flag()
iv = bytes.fromhex(ciphertext[:32])

flag_encrypt = bytes.fromhex(ciphertext[32:])

print(bytes.fromhex(encrypt(flag_encrypt.hex(), iv.hex())).decode())
