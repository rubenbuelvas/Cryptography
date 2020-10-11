import os
import platform


def get_alphabet_indexes(alphabet):
    dictionary = {}
    for i in range(len(alphabet)):
        dictionary[alphabet[i]] = i
    return dictionary


def vigenere(message, key, mode='decode', alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    new_message = ''
    message = message.upper()
    message = message.replace(' ', '')
    key = key.upper()
    letter_ids = get_alphabet_indexes(alphabet)
    for i in range(len(message)):
        if message[i] in letter_ids:
            if mode == 'encode':
                new_message += alphabet[(letter_ids[message[i]] + letter_ids[key[i%len(key)]])%len(alphabet)]
            elif mode == 'decode':
                new_message += alphabet[(letter_ids[message[i]] - letter_ids[key[i%len(key)]])%len(alphabet)]
        else:
            new_message += message[i]
    return new_message


if __name__ == '__main__':
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    print('VIGENÈRE CIPHER')
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
    print(vigenere(message, key, mode))
    print('-----------------------------------')
    pause = input('Press the <ENTER> key to continue...')