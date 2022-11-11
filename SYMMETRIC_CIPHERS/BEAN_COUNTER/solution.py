from pwn import *
import requests


class StepUpCounter(object):
    def __init__(self, value=os.urandom(16), step_up=False):
        self.value = value.hex()
        self.step = 1
        self.stup = step_up

    def increment(self):
        if self.stup:
            self.newIV = hex(int(self.value, 16) + self.step)
        else:
            self.newIV = hex(int(self.value, 16) - self.stup)
        self.value = self.newIV[2:len(self.newIV)]
        return bytes.fromhex(self.value.zfill(32))

    def __repr__(self):
        self.increment()
        return self.value

"""
    step_up = False -> the counter is constant 
    -> the keystream don't change during the encrypted process (1)
    we have to find the keystream and xor keystream with ciphertext

    we notice that: all png file have the similar header
    -> use the random png file to get header(16 bytes) and we have:
    KEY = header (+) ciphertext[:16]

    KEY is constant (1)
    => plaintext = xor(ciphertext, KEY)
"""

def encrypt():
    url = "http://aes.cryptohack.org/bean_counter/encrypt/"
    return requests.get(url).json().get("encrypted", None)

encrypted = bytes.fromhex(encrypt())

f = open("2.png", "rb")

KEY = xor(f.read(16), encrypted[:16])

with open("bean_flag.png", "wb") as f1:
    f1.write(xor(encrypted, KEY))