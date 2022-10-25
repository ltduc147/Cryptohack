
from Crypto.PublicKey import RSA

f = open("key.pem", "r")

key = RSA.importKey(f.read())

print(key.n)

""" 
ype(key) : RsaKey
RsaKey:
    n: RSA modulus 
    d : private exponent 
    e : public exponent 
    p: First factor of the RSA modulus
    q: Second factor of the RSA modulus
    u : Chinese remainder component (p ^ −1 mod q) 
"""