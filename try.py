# your code goes hereimport copy
import numpy as np
import random

def random_key():
  key = np.zeros((6, 6), dtype=str)
  rotations = np.zeros((6,6), dtype=str)
  random_row = random.randint(0,5)
  random_col = random.randint(0,5)
  for i in range(9):
    while(rotations.item(random_row,random_col)):
      random_row = random.randint(0,5)
      random_col = random.randint(0,5)
    key[random_row,random_col] = 1
    rotations[random_row,random_col] = 1
    for j in range(4):
      rotations = np.rot90(rotations,k=1,axes=(0,1))
      rotations[random_row,random_col] = 1
  return key


def grilla_giratoria(message, key, mode="decode", alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    new_message = ""
    message = list(message)
    size = len(key)
    if mode == "encode":
        new_matrix = np.zeros((size, size), dtype=str)
        while len(message) > 0:
            for j in range(size):
                for k in range(size):
                    if key.item(j, k) == 1:
                            new_matrix[j, k] = message.pop(0)
                key = np.rot90(key, k=3, axes=(0, 1))
        for i in range(size):
            for j in range(size):
                new_message += new_matrix[i][j]
    elif mode == "decode":
        encoded_matrix = np.zeros((size, size), dtype=str)
        for i in range(size):
            for j in range(size):
                encoded_matrix[i][j] = message.pop(0)
        print(encoded_matrix)
        while len(new_message) < size*size:
            for i in range(size):
                for j in range(size):
                    if key.item((i, j)):
                        new_message += encoded_matrix[i][j]
            key = np.rot90(key, k=3, axes=(0, 1))
    return new_message

def multiplicacion_polinomios(polinomio_a, polinomio_b):
    polinomio_a.reverse()
    polinomio_b.reverse()
    result = []
    size_a = len(polinomio_a)
    size_b = len(polinomio_b)
    for i in range(size_a+size_b-1):
        result.append(0)
    for i in range(size_a):
        result[i] = polinomio_a[i] * polinomio_b[0]
    for i in range(1, size_b):
        result[i] = result[i] + polinomio_b[i] * polinomio_b[0]
    for i in range(1, size_a):
        for j in range(1, size_b):
            pos = i+j
            result[pos] = result[pos] + (polinomio_a[i] * polinomio_b[j])
    return result

ans = multiplicacion_polinomios([3,2,1], [4,3,2,1])
print(ans)
# key = np.array([[0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1], [0, 1, 1, 0, 0, 1], [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1]])
# ans = grilla_giratoria(message="FDOLRAEDLTEEASCXDIOFCUSRALAVNETAOCIR", key= key)
# print(ans)
# for i in range(10000000):
#     ans = grilla_giratoria(message="FDOLRAEDLTEEASCCDIOFXUSRALAVNETAOCIR", key= random_key())
#     ans = list(ans)
#     ans.insert(9, " ")
#     ans.insert(9+3, " ")
#     ans.insert(9+3+6, " ")
#     ans.insert(9+3+6+8, " ")
#     ans.insert(9+3+6+8+7, " ")
#     ans.insert(9+3+6+8+7+3, " ")
#     ans = "".join(ans)
#     #DESCIFRAR
#     #CIFRADO
#     #CLAVE
#     #TEXTO
#     if "TEXTO" in ans:
#         print(ans)

#! /usr/bin/env python
def normalize(poly):
    while poly and poly[-1] == 0:
        poly.pop()
    if poly == []:
        poly.append(0)


def poly_divmod(num, den):
    #Create normalized copies of the args
    num = num[:]
    normalize(num)
    den = den[:]
    normalize(den)

    if len(num) >= len(den):
        #Shift den towards right so it's the same degree as num
        shiftlen = len(num) - len(den)
        den = [0] * shiftlen + den
    else:
        return [0], num

    quot = []
    divisor = float(den[-1])
    for i in range(shiftlen + 1):
        #Get the next coefficient of the quotient.
        mult = num[-1] / divisor
        quot = [mult] + quot

        #Subtract mult * den from num, but don't bother if mult == 0
        #Note that when i==0, mult!=0; so quot is automatically normalized.
        if mult != 0:
            d = [mult * u for u in den]
            num = [u - v for u, v in zip(num, d)]

        num.pop()
        den.pop(0)

    normalize(num)
    return quot, num


def test(num, den):
    q, r = poly_divmod(num, den)
    return q, r


def main():
    num = [1, 5, 10, 10, 5, 1]
    den = [1, 2, 1]
    print(test(num, den))

    num = [5, 16, 10, 22, 7, 11, 1, 3]
    den = [1, 2, 1, 3]

    quot = [5, 1, 3, 0, 1]
    rem = [0, 5]

    q, r = test(num, den)
    assert quot == q
    assert rem == r


if __name__ == '__main__':
    main()