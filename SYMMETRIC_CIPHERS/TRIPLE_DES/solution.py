import requests
from Crypto.Util.Padding import pad, unpad

"""
    In DES, we have 4 weak key: encrypt = decrypt
    (1) 0x0000000000000000
    (2) 0xffffffffffffffff
    (3) 0xE1E1E1E1F0F0F0F0
    (4) 0x1E1E1E1E0F0F0F0F

    Encrypt two time, we'll get plaintext
"""

def encrypt(key, plaintext):
    url = f"http://aes.cryptohack.org/triple_des/encrypt/{key}/{plaintext}/"
    return requests.get(url).json().get("ciphertext", None)

def encrypt_flag(key):
    url = f"http://aes.cryptohack.org/triple_des/encrypt_flag/{key}/"
    return requests.get(url).json().get("ciphertext", None)

weak_key = "00" * 8 + "ff" * 8
flag_encrypt = encrypt_flag(weak_key)
flag = unpad(bytes.fromhex(encrypt(weak_key, flag_encrypt)), 8)
print(flag.decode())