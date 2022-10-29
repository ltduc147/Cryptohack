"""
    a1 = x ^ k mod p
    a2 = x ^ (k + 1) mod p
    => a1 * x = x ^ (k + 1) = a2 mod p
    => x = a2 * (a1 ^ -1) mod p
    ------------------------------------------------------
    For each p > max(list) and < 1000 (p three digit)
        check for each pair in list, if x unique: print result
"""


ints = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]

x = max(ints)

print(x)

for p in range(x + 1, 1000):
    temp = [pow(ints[i - 1], p - 2 , p) * ints[i] % p for i in range(1, len(ints))]
    if len(set(temp)) == 1:
        print(p, set(temp))
        break