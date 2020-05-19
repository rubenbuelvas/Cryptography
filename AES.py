import numpy as np
import copy
import util
from gf256 import GF256

# Galois field 2^8 operations
def add(a, b):
    c = ""
    a = util.hex_to_bin(a)
    b = util.hex_to_bin(b)
    c = util.xor(a, b)
    c = util.bin_to_hex(c)
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


#AES matrix operations (for bytes)
def matrix_to_text(matrix):
    text = ""
    matrix = np.matrix(matrix)
    for i in range(4):
        for j in range(4):
            text += matrix.item((j, i))
    return text


def text_to_matrix(text):
    matrix = []
    text = list(text)
    for i in range(4):
        wi = []
        for j in range(4):
            item = text.pop(0)
            item += text.pop(0)
            wi.append(item)
        matrix.append(wi)
    matrix = np.matrix(matrix)
    return matrix


# Subtitute bytes
def SB(bytes):
    new_bytes = np.full((4, 4), "00")
    sb_matrix = np.matrix([["63", "7c", "77", "7b", "f2", "6b", "6f", "c5", "30", "01", "67", "2b", "fe", "d7", "ab", "76"], 
                           ["ca", "82", "c9", "7d", "fa", "59", "47", "f0", "ad", "d4", "a2", "af", "9c", "a4", "72", "c0"], 
                           ["b7", "fd", "93", "26", "36", "3f", "f7", "cc", "34", "a5", "e5", "f1", "71", "d8", "31", "15"], 
                           ["04", "c7", "23", "c3", "18", "96", "05", "9a", "07", "12", "80", "e2", "eb", "27", "b2", "75"], 
                           ["09", "83", "2c", "1a", "1b", "6e", "5a", "a0", "52", "3b", "d6", "b3", "29", "e3", "2f", "84"], 
                           ["53", "d1", "00", "ed", "20", "fc", "b1", "5b", "6a", "cb", "be", "39", "4a", "4c", "58", "cf"], 
                           ["d0", "ef", "aa", "fb", "43", "4d", "33", "85", "45", "f9", "02", "7f", "50", "3c", "9f", "a8"], 
                           ["51", "a3", "40", "8f", "92", "9d", "38", "f5", "bc", "b6", "da", "21", "10", "ff", "f3", "d2"], 
                           ["cd", "0c", "13", "ec", "5f", "97", "44", "17", "c4", "a7", "7e", "3d", "64", "5d", "19", "73"], 
                           ["60", "81", "4f", "dc", "22", "2a", "90", "88", "46", "ee", "b8", "14", "de", "5e", "0b", "db"], 
                           ["e0", "32", "3a", "0a", "49", "06", "24", "5c", "c2", "d3", "ac", "62", "91", "95", "e4", "79"], 
                           ["e7", "c8", "37", "6d", "8d", "d5", "4e", "a9", "6c", "56", "f4", "ea", "65", "7a", "ae", "08"], 
                           ["ba", "78", "25", "2e", "1c", "a6", "b4", "c6", "e8", "dd", "74", "1f", "4b", "bd", "8b", "8a"], 
                           ["70", "3e", "b5", "66", "48", "03", "f6", "0e", "61", "35", "57", "b9", "86", "c1", "1d", "9e"], 
                           ["e1", "f8", "98", "11", "69", "d9", "8e", "94", "9b", "1e", "87", "e9", "ce", "55", "28", "df"], 
                           ["8c", "a1", "89", "0d", "bf", "e6", "42", "68", "41", "99", "2d", "0f", "b0", "54", "bb", "16"] 
    ])
    for i in range(4):
        for j in range(4):
            my_byte = bytes.item((i, j))
            y = util.hex_to_dec(my_byte[0])
            x = util.hex_to_dec(my_byte[1])
            new_bytes.itemset((i, j), sb_matrix[y, x])
    return new_bytes


def SB_key(bytes):
    new_byte = ""
    sb_matrix = np.matrix([["63", "7c", "77", "7b", "f2", "6b", "6f", "c5", "30", "01", "67", "2b", "fe", "d7", "ab", "76"], 
                           ["ca", "82", "c9", "7d", "fa", "59", "47", "f0", "ad", "d4", "a2", "af", "9c", "a4", "72", "c0"], 
                           ["b7", "fd", "93", "26", "36", "3f", "f7", "cc", "34", "a5", "e5", "f1", "71", "d8", "31", "15"], 
                           ["04", "c7", "23", "c3", "18", "96", "05", "9a", "07", "12", "80", "e2", "eb", "27", "b2", "75"], 
                           ["09", "83", "2c", "1a", "1b", "6e", "5a", "a0", "52", "3b", "d6", "b3", "29", "e3", "2f", "84"], 
                           ["53", "d1", "00", "ed", "20", "fc", "b1", "5b", "6a", "cb", "be", "39", "4a", "4c", "58", "cf"], 
                           ["d0", "ef", "aa", "fb", "43", "4d", "33", "85", "45", "f9", "02", "7f", "50", "3c", "9f", "a8"], 
                           ["51", "a3", "40", "8f", "92", "9d", "38", "f5", "bc", "b6", "da", "21", "10", "ff", "f3", "d2"], 
                           ["cd", "0c", "13", "ec", "5f", "97", "44", "17", "c4", "a7", "7e", "3d", "64", "5d", "19", "73"], 
                           ["60", "81", "4f", "dc", "22", "2a", "90", "88", "46", "ee", "b8", "14", "de", "5e", "0b", "db"], 
                           ["e0", "32", "3a", "0a", "49", "06", "24", "5c", "c2", "d3", "ac", "62", "91", "95", "e4", "79"], 
                           ["e7", "c8", "37", "6d", "8d", "d5", "4e", "a9", "6c", "56", "f4", "ea", "65", "7a", "ae", "08"], 
                           ["ba", "78", "25", "2e", "1c", "a6", "b4", "c6", "e8", "dd", "74", "1f", "4b", "bd", "8b", "8a"], 
                           ["70", "3e", "b5", "66", "48", "03", "f6", "0e", "61", "35", "57", "b9", "86", "c1", "1d", "9e"], 
                           ["e1", "f8", "98", "11", "69", "d9", "8e", "94", "9b", "1e", "87", "e9", "ce", "55", "28", "df"], 
                           ["8c", "a1", "89", "0d", "bf", "e6", "42", "68", "41", "99", "2d", "0f", "b0", "54", "bb", "16"] 
    ])
    bytes = "".join(bytes)
    for i in range(int(len(bytes)/2)):
        my_byte = bytes[i*2:i*2+i+2]
        y = util.hex_to_dec(my_byte[0])
        x = util.hex_to_dec(my_byte[1])
        new_byte += sb_matrix[y, x]
    return new_byte


# Shift rows
def SR(bytes):
    new_bytes = []
    bytes = bytes.tolist()
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


# Add Round Key
def ARK(message, key):
    new_message = ""
    message = util.hex_to_bin(message)
    key = util.hex_to_bin(key)
    new_message = util.xor(message, key)
    new_message = util.bin_to_hex(new_message)
    return new_message


# T transformation
def T(key, constant):
    new_key = copy.copy(key)
    item = new_key.pop(0)
    new_key.append(item)
    new_key = SB_key(new_key)
    y0 = new_key[:2]
    y0 = add(y0, constant)
    new_key = y0 + new_key[2:]
    return new_key


def round_constant_generator():
    constants = ["01", "02", "04", "08", "10", "20", "40", "80", "1B", "36"]
    return constants


def key_generator(key, is_hex=False):
    keys = []
    constants = round_constant_generator()
    if not is_hex:
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
        wi = []
        key_a = "".join(keys[i-4])
        if i%4 == 0:
            key_b = T(keys[i-1], constants.pop(0))
        else:
            key_b = "".join(keys[i-1])
        wi_raw = add(key_a, key_b)
        wi_raw = list(wi_raw)
        for j in range(4):
            item = wi_raw.pop(0)
            item += wi_raw.pop(0)
            wi.append(item)
        keys.append(wi)
    return keys


def AES128(message, key, mode="encode", mes_is_hex=False, key_is_hex=False):
    new_message = ""
    keys = key_generator(key, is_hex=key_is_hex)
    states = []

    # Getting hex matrix
    if len(message) < 16:
        message += "x"*(16-len(message))
    if mes_is_hex:
        message_hex = message
    else:
        message_hex = util.str_to_ascii_hex(message)
    message_hex = list(message_hex)
    message_matrix = []
    for i in range(4):
        row = []
        for j in range(4):
            item = message_hex.pop(0)
            item += message_hex.pop(0)
            row.append(item)
        message_matrix.append(row)
    message_matrix = (np.matrix(message_matrix).transpose())

    # Initial round
    round_key = matrix_to_text(np.matrix(keys[0:4]).transpose())
    states.append(ARK(matrix_to_text(message_matrix), round_key))

    # AES128 10 rounds
    for i in range(1, 11):
        last_round_message = text_to_matrix(states[i-1])
        last_round_message = last_round_message.transpose()
        round_message = []
        round_message = SB(last_round_message)
        round_message = SR(round_message)
        if i < 10:
            round_message = MC(round_message)
            print(":D")
        round_key = np.matrix(keys[i*4:i*4+4]).transpose()
        states.append(ARK(matrix_to_text(round_message), matrix_to_text(round_key)))

    #Converting ascii hex to plaintext if necessary
    if mes_is_hex:
        new_message = states[-1]
    else:
        new_message = util.ascii_hex_to_str(states[-1])

    return new_message

    
def AEStest():
    k = "2b7e151628aed2a6abf7158809cf4f3c"
    print(key_generator(k, is_hex=True))


def AES(message, key, mode="encode", block_mode="ECB"):
    pass