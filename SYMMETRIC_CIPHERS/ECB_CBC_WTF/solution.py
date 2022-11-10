import requests
from Crypto.Cipher import AES 
from pwn import xor

def encrypt_flag():
    url = "http://aes.cryptohack.org/ecbcbcwtf/encrypt_flag/"
    return requests.get(url).json().get("ciphertext", None)

def decrypt(ciphertext):
    url = f"http://aes.cryptohack.org/ecbcbcwtf/decrypt/{ciphertext}/"
    return requests.get(url).json().get("plaintext", None)

def solve():
    # len(flag) = len(ciphertext) - len(iv) = 48 - 16 = 32 (bytes)
    ciphertext = encrypt_flag()
    iv = bytes.fromhex(ciphertext[:32])
    flag = bytes.fromhex(ciphertext[32:96])
    # plain_flag[0:16] = decrypt(encrypt_flag[0:16]) xor iv (initial vector)
    flag_block1 = xor(bytes.fromhex(decrypt(flag[:16].hex())), iv)
    # plain_flag[0:16] = decrypt(encrypt_flag[16:32]) xor encrypt_flag[0:16]
    flag_block2 = xor(bytes.fromhex(decrypt(flag[16:32].hex())), flag[:16])
    return (flag_block1 + flag_block2).decode()

print(solve())
