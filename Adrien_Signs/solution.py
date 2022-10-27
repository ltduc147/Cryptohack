"""
    n === a ^ e mod p
    log_a(n) === e mod p

    log_a(n) mod p called discrete_log

    caculated Discrete_log use 'sympy' module

    caculate log_a(n) mod p:
        if error <=> ( n is modified -> -n % p : binary += "1" )
        else ( binary += "0" )

    syntax:
        discrete_log(p, n, a) : log_a(n) mod p
"""

from sympy import discrete_log

a = 288260533169915
p = 1007621497415251

f =  open("output.txt", "r")
str = f.read()
ints = list(map(int, str[1:len(str) - 2].split(", ")))

binary = ""
for i in range(len(ints)):
    try:
        r = discrete_log(p, ints[i], a)
        binary += "1"
    except:
        binary += "0"
flag = ""
#print flag if have bin strings
for i in range(0, len(binary), 8):
    flag += chr(int(binary[i : i+8], 2))

print(flag)