def str_to_ascii_binary(message):
    ans = ""
    for i in range(len(message)):
        ans += "0" + str(bin(ord(message[i]))[2:])    
    return ans


def ascii_binary_to_str(message):
    ans = ""
    for i in range(int(len(message)/8)):
        my_bin = message[i*8:i*8+8]
        my_bin = "0b" + my_bin[1:]
        ascii_code = int(my_bin, 2)
        ans += str(chr(ascii_code))
    return ans


def str_to_ascii_hex(message):
    ans = ""
    for i in range(len(message)):
        my_hex = str(hex(ord(message[i]))[2:])
        if len(my_hex) == 1:
            my_hex = "0" + my_hex
        ans += my_hex    
    return ans


def ascii_hex_to_str(message):
    ans = ""
    for i in range(int(len(message)/2)):
        my_hex = message[i*2:i*2+2]
        ascii_code = int(my_hex, 16)
        ans += str(chr(ascii_code))
    return ans


def xor(a, b):
    c = ""
    for i in range(len(a)):
        if a[i] == "0" and b[i] == "0":
            c += "0"
        elif a[i] == "0" and b[i] == "1":
            c += "1"
        elif a[i] == "1" and b[i] == "0":
            c += "1"
        elif a[i] == "1" and b[i] == "1":
            c += "0"
    return c


def bin_to_hex(a):
    b = hex(int(a, 2))[2:]
    b = ("0"*(int(len(a)/4)-len(b))) + b
    return b


def hex_to_bin(a):
    b = bin(int(a, 16))[2:]
    b = ("0"*((len(a)*4)-len(b))) + b
    return b


def dec_to_bin(a):
    b = ""
    a = int(a)
    b = bin(a)[2:]
    b = ("0"*(8-len(b))) + b
    return b


def bin_to_dec(a):
    b = 0
    a = "0b" + a
    b = int(a, 2)
    return b


def dec_to_hex(a):
    b = ""
    a = int(a)
    b = hex(a)[2:]
    if len(b) == 1:
        b = "0" + b
    return b


def hex_to_dec(a):
    b = 0
    a = str(a)
    a = "0x" + a
    b = int(a, 16)
    return b


def powermod(a, b, n):
    curr = a%n
    res = 1
    while b > 0:
        if b%2 == 1:
            res = (res*curr)%n
        curr = (curr*curr)%n
        b = int(b/2)
    return res


def discrete_log(a, b, n):
    ans = -1
    for i in range(0, n-1):
        if powermod(a, i, n) == b:
            ans = i
            break
    return ans