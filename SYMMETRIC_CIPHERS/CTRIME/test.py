import zlib
import string

str = b'crypto{ecrypto{ecrypto{ecrypto{ecrypto{ecrypto{secret}'
min = 1000
ch = ""
for c in string.printable:
    x = (b"crypto{" + c.encode()) * 5 + b"crypto{secret}"
    print (x)
print(ch)

print(len(zlib.compress(str)))