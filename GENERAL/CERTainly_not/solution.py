
from Crypto.PublicKey import RSA

f = open("2048b-rsa-example-cert_3220bd92e30015fe4fbeb84a755e7ca5.der", "rb")

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