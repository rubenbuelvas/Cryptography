import numpy as np
import util

# Galois field 2^8 operations
def L(a):
    b = ""
    return b


def E(a):
    b = ""
    return b


def add(a, b):
    c = ""
    a = util.hex_to_bin(a)
    b = util.hex_to_bin(b)
    c = util.xor(a, b)
    c = util.bin_to_hex(c)
    return c


def mul(a, b):
    c = E(add(L(a), L(b)))
    return c


# Subtitute bytes
def SB(message):

    pass


# Shift rows
def SR(message):
    new_message = []
    for i in range(4):
        tmp = message[i][i:]
        for j in range(i):
            tmp.append(message[i][j])  
        new_message.append(tmp)
    new_message = np.matrix(new_message)
    return new_message


# Mix columns
def MC(message):
    new_message = ""
    mc_matrix = np.matrix([["02", "03", "01", "01"],
                           ["01", "02", "03", "01"],
                           ["01", "01", "02", "03"],
                           ["03", "01", "01", "02"] 
    ])
    return new_message


# Key operation
def ARK(message, key):
    new_message = ""
    return new_message


def key_generator(key):
    keys = []
    return keys


def AES(message, key, mode="encode"):
    new_message = ""
    keys = key_generator(key)

    for i in range(int(len(message)/16)):

        new_local_message = ""

        # Getting hex matrix of chunk 
        local_message = message[i*16:i*16+16]
        if len(local_message) < 16:
            local_message += "x"*(16-len(local_message))
        local_message = util.str_to_ascii_hex(local_message)
        local_message = list(local_message)
        message_matrix = []
        for j in range(4):
            row = []
            for k in range(4):
                item = local_message.pop(0)
                item += local_message.pop(0)
                row.append(item)
            message_matrix.append(row)
        message_matrix = (np.matrix(message_matrix).transpose())
        
        # Initial round


        # AES128 9 rounds


        # Final round


        new_message += new_local_message

    return new_message