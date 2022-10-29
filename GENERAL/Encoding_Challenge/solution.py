from pwn import * # pip install pwntools
from Crypto.Util.number import *
import json
import base64
import codecs
import random

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


for i in range(101):
    received = json_recv()

    type = received["type"]
    content = received["encoded"]
    

    if type == "hex":
        decode = bytes.fromhex(content).decode()
    elif type == "bigint":
        decode = bytes.fromhex(content.replace("0x", "")).decode()
    elif type == "rot13":
        decode = codecs.decode(content, "rot13")
    elif type == "base64":
        decode = base64.b64decode(content).decode()
    elif type == "utf-8":
        decode = "".join([chr(c) for c in content])
    to_send = {
        "decoded": decode
    }
    json_send(to_send) 