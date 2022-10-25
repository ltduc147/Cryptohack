from Crypto.PublicKey import RSA

f = open("privacy_enhanced_mail_1f696c053d76a78c2c531bb013a92d4a.pem", "r")

key = RSA.importKey(f.read())

print(key.d)

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