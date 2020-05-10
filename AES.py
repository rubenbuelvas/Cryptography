import numpy as np
import util
from gf256 import GF256

# Galois field 2^8 operations
def add(a, b):
    c = ""
    a = util.hex_to_dec(a)
    b = util.hex_to_dec(b)
    c = util.bin_to_hex(str(GF256(a)+GF256(b))[8:16])
    return c


def mul(a, b):
    a = util.hex_to_dec(a)
    b = util.hex_to_dec(b)
    c = util.bin_to_hex(str(GF256(a)*GF256(b))[8:16])
    return c


def matrix_mul(a, b):
    c = np.full((a.shape[0], b.shape[1]), "00")
    for i in range(a.shape[0]):
        for j in range(b.shape[1]):
            new_item = "00"
            for k in range(a.shape[1]):
                ai = a.item((i, k))
                bi = b.item((k, j))
                new_item = add(new_item, mul(ai, bi))
            c.itemset((i, j), new_item)
    return c


# Subtitute bytes
def SB(byte):
    new_byte = ""
    byte = util.hex_to_dec(byte)
    
    new_byte = util.dec_to_hex(new_byte)
    return new_byte


# Shift rows
def SR(bytes):
    new_bytes = []
    for i in range(4):
        tmp = bytes[i][i:]
        for j in range(i):
            tmp.append(bytes[i][j])  
        new_bytes.append(tmp)
    new_bytes = np.matrix(new_bytes)
    return new_bytes


# Mix columns
def MC(bytes):
    new_bytes = np.full((4, 4), "00")
    mc_matrix = np.matrix([["02", "03", "01", "01"],
                           ["01", "02", "03", "01"],
                           ["01", "01", "02", "03"],
                           ["03", "01", "01", "02"] 
    ])
    new_bytes = matrix_mul(mc_matrix, bytes)
    return new_bytes


# Key operation
def ARK(message, key):
    new_message = ""
    return new_message


# T transformation
def T(key):
    new_key = key[1:]
    new_key.append(key[0])
    new_key = SB(new_key)
    return new_key


def round_constant_generator():
    constants = []
    return constants


def key_generator(key):
    keys = []
    key = util.str_to_ascii_hex(key)
    key = list(key)
    for i in range(4):
        wi = []
        for j in range(4):
            item = key.pop(0)
            item += key.pop(0)
            wi.append(item)
        keys.append(wi)
    for i in range(4, 44):
        if i%4 == 0:
            wi = T(add(keys[i-4], keys[i-1]))
        else:
            wi = add(keys[i-4], keys[i-1])
    return keys


def AES(message, key, mode="encode"):
    new_message = ""
    keys = key_generator(key)
    constants = round_constant_generator()
    states = []

    for i in range(int(len(message)/16)):
        new_local_message = ""
        local_states = []

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


        # AES128 10-1 rounds
        for j in range(1, 10):
            pass

        # Final round


        states.append(local_states)
        new_message += new_local_message

    return new_message

    
def AEStest():
    b = np.matrix([ ["02", "e3", "1d", "45"],
                    ["c1", "19", "91", "e2"],
                    ["96", "f7", "5a", "89"],
                    ["53", "05", "1f", "28"] 
    ])
    print(MC(b))