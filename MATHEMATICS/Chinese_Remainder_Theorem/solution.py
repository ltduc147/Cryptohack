a = [2, 3, 5]
n = [5, 11, 17]
y = [187, 85, 55]
r = 0
for i in range(3):
    z = pow(y[i], -1, n[i])
    r += a[i] * z *y[i]

print(r)