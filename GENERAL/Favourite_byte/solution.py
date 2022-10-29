from pwn import *
from Crypto.Util.number import *

key = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

for i in range(255):
    print(xor(long_to_bytes(i), bytes.fromhex(key)))
