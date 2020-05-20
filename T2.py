import numpy as np
from AES import *

# 1 GF(27)

# 2 W40, k = 00000000000000000000000000000000

k = "00000000000000000000000000000000"
w = key_generator(k)
print(w[40])

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
print(c)

# 4 AES inverse operations

y = np.matrix([
    ["01", "02", "03", "04"],
    ["05", "06", "07", "08"],
    ["09", "0a", "0b", "0c"],
    ["0d", "0e", "0f", "10"]
])

x = SR1(MC1(SB1(y)))
print(x)

# 5 ECB mode

