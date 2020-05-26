import numpy as np
import galois
from AES import *

# 1 GF(27)

e = [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 1, 2], [0, 2, 0], [0, 2, 1], [0, 2, 2], 
     [1, 0, 0], [1, 0, 1], [1, 0, 2], [1, 1, 0], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2],
     [2, 0, 0], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]
]

sm = []
for i in range(len(e)):
    sm.append([])
    for j in range(len(e)):
        item = galois.sum(e[i], e[j], 3, 3)
        item = list(map(str, item)) 
        item = int("".join(item))
        sm[i].append(item)
sm = np.matrix(sm)

mm = []
for i in range(len(e)):
    mm.append([])
    for j in range(len(e)):
        item = galois.mul(e[i], e[j], 3, 3, [1, 0, 2, 1])
        for k in range(len(item)):
            item[k] = item[k]%3
        item = list(map(abs, item)) 
        item = list(map(int, item)) 
        item = list(map(str, item)) 
        item = int("".join(item))
        mm[i].append(item)
mm = np.matrix(mm)

p1 = mm

# 2 W40, k = 00000000000000000000000000000000

k = "00000000000000000000000000000000"
w = key_generator(k)
p2 = w[40]

# 3 Matrix multiplication

a = np.matrix([
    ["10", "07", "b3"],
    ["2d", "81", "43"],
    ["7c", "a5", "66"]
])

b = np.matrix([
    ["b0", "78", "f2"],
    ["32", "12", "3f"],
    ["7a", "59", "86"]
])

c = matrix_mul(a, b)
p3 = c

# 4 AES inverse operations

y = np.matrix([
    ["01", "02", "03", "04"],
    ["05", "06", "07", "08"],
    ["09", "0a", "0b", "0c"],
    ["0d", "0e", "0f", "10"]
])

x = SR1(MC1(SB1(y)))
p4 = x

# 5 ECB mode

ecb_m = ECB("AES es un algoritmo muy importante en la seguridad de la informacion actual", "0123456789ABCDEF0123456789ABCDEF", mode="encode", mes_is_hex=False, key_is_hex=True)
p5 = ecb_m

# 6 Pseudo-random number

# 8 Quick exponentiation

n = util.powermod(2, 10, 100001)
n = util.powermod(n, 15, 100001)
p6 = n

# 9 Discrete logarithm 

log = util.discrete_log(2, 7, 13)
p9 = util.powermod(2, 11, 13)

# Print stuff

print(p1)