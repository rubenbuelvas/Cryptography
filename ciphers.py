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