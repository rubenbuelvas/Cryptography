import numpy.polynomial.polynomial as poly
import numpy as np

def sum(a, b, prime, exp):
    ans = []
    a = list(map(int, a)) 
    b = list(map(int, b)) 
    for i in range(exp):
        tmp = (a[i]+b[i])%prime
        ans.append(tmp) 
    return ans


def mul(a, b, prime, exp, min0):
    a.reverse()
    b.reverse()
    min0.reverse()
    ans = []
    mul0 = poly.polymul(a, b)
    ans = poly.polydiv(mul0, min0)[1]
    ans = list(map(int, ans)) 
    ans.reverse()
    return ans


"""def generate_elements(prime, exp, gen, min0):
    elements = []
    n = prime**exp
    e0, e1 = [], []
    for i in range(exp):
        e0.append(0)
    elements.append(e0)
    for i in range(n-1):
        tmp = gen
        for j in range(i):
            tmp = mul(tmp, gen, prime, exp, min0)
        elements.append(tmp)
    return elements
"""