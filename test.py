
u =[846835985, 9834798552]
v =[87502093, 123094980]


def tvh(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]

def solve(u, v):
    while True:
        if tvh(v, v) < tvh(u, u):
            temp = list(u)
            u = list(v)
            v = list(temp)
        m = tvh(u, v) // tvh(u, u)
        if m == 0: return tvh(u, v)
        v[0] = v[0] - m*u[0]
        v[1] = v[1] - m*u[1]
        
print(solve(u, v))