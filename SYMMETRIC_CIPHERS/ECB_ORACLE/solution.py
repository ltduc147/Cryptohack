import requests
"""
assume flag = crypto{secret_flag}

if input = "A" * 16, block is

    AAAAAAAAAAAAAAAA
    crypto{secret_fl
    ag}

To guess the first of flag we can make the input is "A" * 15 + guess + "A" * 15

    AAAAAAAAAAAAAAA?   1
    AAAAAAAAAAAAAAAc   2
    rypto{secret_fla
    g}

Now, if we encrypt the output of 1 and 2 are the same if ? = "c":
With the second of flag: "A" * 14 + guess + "A" * 14
    
    AAAAAAAAAAAAAAc?   1
    AAAAAAAAAAAAAAcr   2
    ypto{secret_flag
    }
Similar, the output of 1 and 2 are the same if ? = "r:
We try all char for ? until match the flag

We need a padding function: 
    size_of_pad = 16 - len(guess) % 16
    return "A" * size_of_pad + guess + "A" * size_of_pad

"""
def encrypt(plaintext):
    plain_hex = plaintext.encode().hex()
    url = f"http://aes.cryptohack.org/ecb_oracle/encrypt/{plain_hex}/"
    return requests.get(url).json().get("ciphertext", None)

def pad_guess(guess):
    pad = "A" * (16 - len(guess) % 16)
    return pad + guess + pad

flag = ""
letter = "abcdefghijklmnopqrstuvwxyz0123456789_{}"

while flag[-1:] != "}":
    for l in letter:
        flag_guess = flag + l
        guess_pad = pad_guess(flag_guess)
        cipher = encrypt(guess_pad)

        guess_size = (16 - len(flag_guess) % 16 + len(flag_guess)) * 2
        # If flag_guess > 16 we need compare a combination of two block -> guess_size = 64 
        if (cipher[:guess_size] == cipher[guess_size : guess_size * 2]):
            # If the guess match the flag, record and break
            flag = flag_guess
            print(flag)
            break