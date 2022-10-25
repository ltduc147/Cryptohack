from pwn import *
from Crypto.Util.number import *

key = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

for i in range(255):
    print(xor(long_to_bytes(i), bytes.fromhex(key)))
