import requests
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from pwn import *


"""
    According to CBC decryption, we have:
    block_out  (+)  iv = plaintext

    function get_cookie(): 
    iv (+) ciphertext[:16] = b"admin=False;expi"     (1)

    we want to have plaintext = b"admin=True;?????"
    -> find new_iv sastified:
    new_iv (+) ciphertext[:16] = b"admin=True;?????" (2)

    (1) (+) (2) -> iv (+) new_iv = b"admin=False;expi" (+)  b"admin=True;?????"
    xor two side with iv -> new_iv = b"admin=False;expi" (+)  b"admin=True;?????" (+) iv
    Finally:
    We call check_admin(cookie, new_iv)
"""

def get_cookie():
    url = "http://aes.cryptohack.org/flipping_cookie/get_cookie/"
    return requests.get(url).json().get("cookie", None)


def check_admin(cookie, iv):
    url = f"http://aes.cryptohack.org/flipping_cookie/check_admin/{cookie}/{iv}/"
    return requests.get(url).json().get("flag", None)


ciphertext = get_cookie()  

iv = bytes.fromhex(ciphertext[:32])

cookie = ciphertext[32:96]
output_plaintext = b"admin=False;expi"
expect_plaintext = pad(b"admin=True;", 16)

new_iv = xor(iv, output_plaintext, expect_plaintext)
print(check_admin(cookie, new_iv.hex()))
