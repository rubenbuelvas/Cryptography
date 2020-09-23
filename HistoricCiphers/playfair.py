import copy
import os
import platform


def playfair(message, key, mode='decode', alphabet='ABCDEFGHIKLMNOPQRSTUVWXYZ'):
    new_message = ''
    message = message.upper()
    message = message.replace('J', 'I')
    message = message.replace(' ', '')
    message = list(message)
    key = key.upper()
    key = key.replace('J', 'I')
    key = list(key)
    matrix = []
    my_row = []
    for i in range(len(key)):
        my_row.append(key[i])
        if len(my_row) == 5:
            matrix.append(my_row)
            my_row = []
    for i in range(len(alphabet)):
        if alphabet[i] not in key:
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
    while i < len(message) - 1:
        if message[i] == message[i + 1]:
            message_pairs.append([message[i], 'X'])
            i += 1
        else:
            message_pairs.append([message[i], message[i + 1]])
            i += 2
    for i in range(len(message_pairs)):
        coords = [[0, 0], [0, 0]]
        for j in range(len(matrix)):
            for k in range(len(matrix[j])):
                if matrix[j][k] == message_pairs[i][0]:
                    coords[0] = [j, k]
                if matrix[j][k] == message_pairs[i][1]:
                    coords[1] = [j, k]
        if coords[0][1] == coords[1][1]:
            if mode == 'encode':
                new_coords = [[(coords[0][0] + 1) % 5, coords[0][1]], [(coords[1][0] + 1) % 5, coords[1][1]]]
            elif mode == 'decode':
                new_coords = [[(coords[0][0] - 1) % 5, coords[0][1]], [(coords[1][0] - 1) % 5, coords[1][1]]]
        elif coords[0][0] == coords[1][0]:
            if mode == 'encode':
                new_coords = [[coords[0][0], (coords[0][1] + 1) % 5], [coords[1][0], (coords[1][1] + 1) % 5]]
            elif mode == 'decode':
                new_coords = [[coords[0][0], (coords[0][1] - 1) % 5], [coords[1][0], (coords[1][1] - 1) % 5]]
        else:
            new_coords = [[coords[0][0], coords[1][1]], [coords[1][0], coords[0][1]]]
        new_message += matrix[new_coords[0][0]][new_coords[0][1]]
        new_message += matrix[new_coords[1][0]][new_coords[1][1]]
    return new_message


if __name__ == '__main__':
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    print('PLAYFAIR CIPHER')
    print('By Rubén Buelvas')
    print('-----------------------------------')
    choice = '-1'
    while choice != '1' and choice != '2':
        choice = input('Write 1 to decode or 2 to encode: ')
        if choice == '1':
            mode = 'decode'
        elif choice == '2':
            mode = 'encode'
    message = input('Write your message: ')
    key = input('Write your key: ')
    print('-----------------------------------')
    print('Resultado:')
    print(playfair(message, key, mode))
    print('-----------------------------------')
    pause = input("Press the <ENTER> key to continue...")
