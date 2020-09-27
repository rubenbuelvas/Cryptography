import os
import platform


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


if __name__ == '__main__':
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    print('CAESAR CIPHER')
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
    key = int(input('Write your key: '))
    print('-----------------------------------')
    print('Resultado:')
    print(caesar(message, key, mode))
    print('-----------------------------------')
    pause = input('Press the <ENTER> key to continue...')