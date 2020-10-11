import os
import numpy as np
import platform


def key_generator(input_key, size):
    matrix_key = np.zeros((size, size), dtype=str)
    for row in range(len(input_key)):
        row_list = input_key[row].split()
        for column in row_list:
            matrix_key[row, int(column)] = 1
    return matrix_key


def turning_grille(message, key, mode='decode', clock_wise=False):
    new_message = ''
    message = list(message)
    size = len(key)
    if mode == 'encode':
        new_matrix = np.zeros((size, size), dtype=str)
        while len(message) > 0:
            for j in range(size):
                for k in range(size):
                    if key.item(j, k):
                        new_matrix[j, k] = message.pop(0)
            if clock_wise:
                key = np.rot90(key, k=3, axes=(0, 1))
            else:
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
            if clock_wise:
                key = np.rot90(key, k=3, axes=(0, 1))
            else:
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
    while choice != '0' and choice != '1':
        choice = input('Write 0 to decode or 1 to encode: ')
        if choice == '0':
            mode = 'decode'
        elif choice == '1':
            mode = 'encode'
    message = input('Write your message: ')
    grille_size = int(input('Write grille size: '))
    choice = '-1'
    while choice != '0' and choice != '1':
        choice = input('Write 0 to turn clock wise or 1 otherwise: ')
        if choice == '0':
            clock_wise = True
        elif choice == '1':
            clock_wise = False
    print('Write your key')
    print(f'Numbers from 0 to {grille_size - 1} separated by spaces')
    key = []
    for i in range(grille_size):
        row = input(f'Row {i} : ')
        key.append(row)
    key = key_generator(key, grille_size)
    print('-----------------------------------')
    print('Result:')
    print(turning_grille(message, key, mode, clock_wise))
    print('-----------------------------------')
    pause = input('Press the <ENTER> key to continue...')
