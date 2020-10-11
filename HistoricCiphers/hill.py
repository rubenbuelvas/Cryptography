import os
import platform


def eea(a, b):
    q = a/b
    if b == 0:
        return a, 1, 0
    dp, xp, yp = eea(b, a % b)
    d, x, y = dp, yp, xp - (q*yp)
    return d, x, y


def hill(message, key, mode='decode', alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    new_message = ''
    letter2index = {}
    for i in range(len(alphabet)):
        letter2index[alphabet[i]] = i
    key_matrix = []
    for i in range(2):
        row = []
        for j in range(2):
            row.append(letter2index.get(key[i * 2 + j]))
        key_matrix.append(row)
    return new_message


if __name__ == '__main__':
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    print('HILL CIPHER')
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
    print('Result:')
    print(hill(message, key, mode))
    print('-----------------------------------')
    pause = input('Press the <ENTER> key to continue...')
