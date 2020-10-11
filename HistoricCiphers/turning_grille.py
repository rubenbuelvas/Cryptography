import os
import random
import numpy as np
import platform


def key_generator():
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


def turning_grille(message, key, mode='decode'):
    new_message = ''
    key = key_generator(key)
    message = list(message)
    size = len(key)
    if mode == 'encode':
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
    elif mode == 'decode':
        encoded_matrix = np.zeros((size, size), dtype=str)
        for i in range(size):
            for j in range(size):
                encoded_matrix[i][j] = message.pop(0)
        while len(new_message) < size*size:
            for i in range(size):
                for j in range(size):
                    if key.item((i, j)):
                        new_message += encoded_matrix[i][j]
            key = np.rot90(key, k=1, axes=(0, 1))
    return new_message


if __name__ == '__main__':
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    print('TURNING GRILLE CIPHER')
    print('By Rubén Buelvas')
    print('-----------------------------------')
    choice = '-1'
    while choice != '1' and choice != '2':
        choice = input('Write 0 to decode or 1 to encode: ')
        if choice == '1':
            mode = 'decode'
        elif choice == '2':
            mode = 'encode'
    message = input('Write your message: ')
    grille_size = int(input('Write grille size: '))
    print('Write your key')
    print(f'Numbers from 0 to {grille_size} separated by spaces')
    key = []
    for i in range(grille_size):
        row = input(f'Row {i} : ')
        key.append(row)
    print('-----------------------------------')
    print('Result:')
    print(turning_grille(message, key, mode))
    print('-----------------------------------')
    pause = input('Press the <ENTER> key to continue...')
    print(key_generator())
