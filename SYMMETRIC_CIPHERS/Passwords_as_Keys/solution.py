from Crypto.Cipher import AES
import hashlib
import random
import requests

def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = password_hash

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return decrypted

with open("words.txt") as f:
    words = [w.strip() for w in f.readlines()]
keyword = random.choice(words)

def encrypt_flag():
	url = "http://aes.cryptohack.org/passwords_as_keys/encrypt_flag/"
	r = requests.get(url)
	return r.json()["ciphertext"]

flag = encrypt_flag()

for word in words:
    KEY = hashlib.md5(word.encode()).digest()
    decrypted = decrypt(flag, KEY)
    
    if decrypted[0] == ord('c') and decrypted[1] == ord('r'):
        print(decrypted.decode())
        break