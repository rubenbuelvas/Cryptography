import copy
import numpy as np
from egcd import egcd
import random


def get_alphabet_indexes(alphabet):
    dictionary = {}
    for i in range(len(alphabet)):
        dictionary[alphabet[i]] = i
    return dictionary


def caesar(message, key=7, mode="decode", alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    new_message = ""
    message = message.upper()
    for i in range(len(message)):
        found = False
        for j in range(len(alphabet)):
            if message[i] == alphabet[j]:
                found = True
                if mode == "decode":
                    new_message += alphabet[(j-key)%len(alphabet)]
                elif mode == "encode":
                    new_message += alphabet[(j+key)%len(alphabet)]
        if not found:
            new_message += message[i]
    return new_message


def playfair(message, key="UNAL", mode="decode", alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    new_message = ""
    message = message.upper()
    message = message.replace("J", "I")
    message = list(message)
    key = key.upper()
    matrix = [list(key)]
    my_row = []
    for i in range(len(alphabet)):
        if alphabet[i] not in matrix[0] and alphabet[i] != "J":
            my_row.append(alphabet[i])
            if len(my_row) == 5:
                matrix.append(my_row)
                my_row = []
    my_message = copy.deepcopy(message)
    for i in range(len(message)):
        if message[i] not in alphabet:
            my_message.remove(message[i])
    message = my_message
    message_pairs = []
    i = 0
    while i < len(message)-1:
        if message[i] == message[i+1]:
            message_pairs.append([message[i], 'X'])    
            i+=1
        else:
            message_pairs.append([message[i], message[i+1]])
            i+=2
    for i in range(len(message_pairs)):
        coords = [[0, 0], [0, 0]]
        for j in range(len(matrix)):
            for k in range(len(matrix[j])):
                if matrix[j][k] == message_pairs[i][0]:
                    coords[0] = [j, k]
                if matrix[j][k] == message_pairs[i][1]:
                    coords[1] = [j, k]
        if coords[0][1] == coords[1][1]:
            if mode == "encode":
                new_coords = [[(coords[0][0]+1)%5, coords[0][1]], [(coords[1][0]+1)%5, coords[1][1]]]
            elif mode == "decode":
                new_coords = [[(coords[0][0]-1)%5, coords[0][1]], [(coords[1][0]-1)%5, coords[1][1]]]
        elif coords[0][0] == coords[1][0]:
            if mode == "encode":
                new_coords = [[coords[0][0], (coords[0][1]+1)%5], [coords[1][0], (coords[1][1]+1)%5]]
            elif mode == "decode":
                new_coords = [[coords[0][0], (coords[0][1]-1)%5], [coords[1][0], (coords[1][1]-1)%5]]  
        else:
            new_coords = [[coords[0][0], coords[1][1]], [coords[1][0], coords[0][1]]]
        new_message += matrix[new_coords[0][0]][new_coords[0][1]]
        new_message += matrix[new_coords[1][0]][new_coords[1][1]]
    return new_message


def vigenere(message, key="UNAL", mode="decode", alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    new_message = ""
    message = message.upper()
    letter_ids = get_alphabet_indexes(alphabet)
    for i in range(len(message)):
        if message[i] in letter_ids:
            if mode == "encode":
                new_message += alphabet[(letter_ids[message[i]] + letter_ids[key[i%len(key)]])%len(alphabet)]
            elif mode == "decode":
                new_message += alphabet[(letter_ids[message[i]] - letter_ids[key[i%len(key)]])%len(alphabet)]    
        else:
            new_message += message[i]
    return new_message

matrix_key2 = np.array([[1, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 1], [0, 0, 1, 0]])
def grilla_giratoria(message, key=matrix_key2, mode="decode", alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
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
                key = np.rot90(key, k=1, axes=(0, 1))
        for i in range(size):
            for j in range(size):
                new_message += new_matrix[i][j]
    elif mode == "decode":
        encoded_matrix = np.zeros((size, size), dtype=str)
        for i in range(size):
            for j in range(size):
                encoded_matrix[i][j] = message.pop(0)
        while len(new_message) < size*size:
            for i in range(size):
                for j in range(size):
                    if key[i][j] == 1:
                        new_message += encoded_matrix[i][j]
            key = np.rot90(key, k=1, axes=(0, 1))
    return new_message

#P1
def hex_item_to_dec(a):
    b = ''
    if a == 'A':
        b = 10
    elif a == 'B':
        b = 11
    elif a == 'C':
        b = 12
    elif a == 'D':
        b = 13
    elif a == 'E':
        b = 14
    elif a == 'F':
        b = 15
    else:
        b = int(a)
    return b 

def custom_op(a, b, op="sum"):
    ans = ''
    sum_op = np.matrix([['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'],
                        ['1', '0', '0', '2', '5', '4', '7', '6', '9', '8', 'B', 'A', 'D', 'C', 'F', 'E'],
                        ['2', '3', '0', '1', '6', '7', '4', '5', 'A', 'B', '8', '9', 'E', 'F', 'C', 'D'],
                        ['3', '2', '1', '0', '7', '6', '5', '4', 'B', 'A', '9', '8', 'F', 'E', 'D', 'C'],
                        ['4', '5', '6', '7', '0', '1', '2', '3', 'C', 'D', 'E', 'F', '8', '9', 'A', 'B'],
                        ['5', '4', '7', '6', '1', '0', '3', '2', 'D', 'C', 'F', 'E', '9', '8', 'B', 'A'],
                        ['6', '7', '4', '5', '2', '3', '0', '1', 'E', 'F', 'C', 'D', 'A', 'B', '8', '9'],
                        ['7', '6', '5', '4', '3', '2', '1', '0', 'F', 'E', 'D', 'C', 'B', 'A', '9', '8'],
                        ['8', '9', 'A', 'B', 'C', 'D', 'E', 'F', '0', '1', '2', '3', '4', '5', '6', '7'],
                        ['9', '8', 'B', 'A', 'D', 'C', 'F', 'E', '1', '0', '3', '2', '5', '4', '7', '6'],
                        ['A', 'B', '8', '9', 'E', 'F', 'C', 'D', '2', '3', '0', '1', '6', '7', '4', '5'],
                        ['B', 'A', '9', '8', 'F', 'E', 'D', 'C', '3', '2', '1', '0', '7', '6', '5', '4'],
                        ['C', 'D', 'E', 'F', '8', '9', 'A', 'B', '4', '5', '6', '7', '0', '1', '2', '3'],
                        ['D', 'C', 'F', 'E', '9', '8', 'B', 'A', '5', '4', '7', '6', '1', '0', '3', '2'],
                        ['E', 'F', 'C', 'D', 'A', 'B', '8', '9', '6', '7', '4', '5', '2', '3', '0', '1'],
                        ['F', 'E', 'D', 'C', 'B', 'A', '9', '8', '7', '6', '5', '4', '3', '2', '1', '0']
    ])

    mul_op = np.matrix([['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                        ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'],
                        ['0', '2', '4', '6', '8', 'A', 'C', 'E', '3', '1', '7', '5', 'B', '9', 'F', 'D'],
                        ['0', '3', '6', '5', 'C', 'F', 'A', '9', 'B', '8', 'D', 'E', '7', '4', '1', '2'],
                        ['0', '4', '8', 'C', '3', '7', 'B', 'F', '6', '2', 'E', 'A', '5', '1', 'D', '9'],
                        ['0', '5', 'A', 'F', '7', '2', 'D', '8', 'E', 'B', '4', '1', '9', 'C', '3', '6'],
                        ['0', '6', 'C', 'A', 'B', 'D', '7', '1', '5', '3', '9', 'F', 'E', '8', '2', '4'],
                        ['0', '7', 'E', '9', 'F', '8', '1', '6', 'D', 'A', '3', '4', '2', '5', 'C', 'B'],
                        ['0', '8', '3', 'B', '6', 'E', '5', 'D', 'C', '4', 'F', '7', 'A', '2', '9', '1'],
                        ['0', '9', '1', '8', '2', 'B', '3', 'A', '4', 'D', '5', 'C', '6', 'F', '7', 'E'],
                        ['0', 'A', '7', 'D', 'E', '4', '9', '3', 'F', '5', '8', '2', '1', 'B', '6', 'C'],
                        ['0', 'B', '5', 'E', 'A', '1', 'F', '4', '7', 'C', '2', '9', 'D', '6', '8', '3'],
                        ['0', 'C', 'B', '7', '5', '9', 'E', '2', 'A', '6', '1', 'D', 'F', '3', '4', '8'],
                        ['0', 'D', '9', '4', '1', 'C', '8', '5', '2', 'F', 'B', '6', '3', 'E', 'A', '7'],
                        ['0', 'E', 'F', 'A', 'D', '3', '2', 'C', '9', '7', '6', '8', '4', 'A', 'B', '5'],
                        ['0', 'F', 'D', '2', '9', '6', '4', 'B', '1', 'E', 'C', '3', '8', '7', '5', 'A']
    ])

    if op == "sum":
        ans = sum_op[hex_item_to_dec(a), hex_item_to_dec(b)]
    elif op == "mul":
        ans = mul_op[hex_item_to_dec(a), hex_item_to_dec(b)]
    return ans

#Encontrar la inversa
matrix_key3 = np.array([['1', '3', '8', 'F', '8'],
                         ['3', '1', '7', '7', '3'],
                         ['6', '3', 'B', '5', '6'],
                         ['A', '7', '1', '2', '3'],
                         ['3', 'E', '7', 'C', '1']
])

def my_hill(message="", key=matrix_key3, mode="decode", alphabet="0123456789ABCDEF"):
    result = ""
    new_message = ""
    message = []
    for i in range(15):
        #Aleatorios, toca hacer convertidor de dec a hex (NO el de python)
        message.append(alphabet[random.randint(0, 15)])
    test_message = "".join(message)
    message = list(message)
    message = [message[0:5], message[5:10], message[10:15]]
    for submessage in message:
        new_submessage = np.zeros((5), dtype=str)
        for i in range(len(submessage)): #new one
            for j in range(len(submessage)): #old one
                if new_submessage[i] == "":
                    new_submessage[i] = custom_op(submessage[j], key.item((i, j)), "mul")
                else:
                    new_submessage[i] = custom_op(new_submessage[i], custom_op(submessage[j], key[i][j], "mul"), "sum")
        new_message += "".join(new_submessage)
    if new_message == "0C8F72E7F55EE1C":
        result = test_message
    return result



#Brute force grilla giratoria
#[Cries in failure]

#hill
#Muy complejo para hacer con fuerza bruta
for i in range(100000):
    ans = my_hill()
    if i%1000 == 0:
        print(i) 
    if not ans == "":
        print(ans)
