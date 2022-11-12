
from requests import get
from multiprocessing.dummy import Pool
from pwn import log # to log the progress

def encrypt(plaintext):
    res = get(f"http://aes.cryptohack.org/ctrime/encrypt/{plaintext.hex()}/")
    try:
        return bytes.fromhex(res.json()['ciphertext'])
    except:
        print(res.content)

initial_flag = b"crypto{"
printable_chars = [bytes([i]) for i in range(32, 127)]
logger = log.progress("🏴☠")

while True:
    with Pool(5) as p:
        ciphertexts = p.map(encrypt, ((initial_flag+i)*5 for i in printable_chars))
    cipherlens = list(map(len, ciphertexts))
    best_char = bytes([cipherlens.index(min(cipherlens)) + 32])

    initial_flag += best_char
    logger.status(initial_flag.decode())
    if best_char == b"}":
        logger.success(f"Found the flag: {initial_flag.decode()}")
        break