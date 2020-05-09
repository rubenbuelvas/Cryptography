import numpy as np
import util


def rotation(message, n):
    message = list(message)
    for i in range(n):
        tmp = message.pop(0)
        message.append(tmp)
    message = "".join(message)
    return message


def pc1(key):
    new_key = np.zeros(56)
    permutation_positions = [57, 49, 41, 33, 25, 17, 9, 
                             1, 58, 50, 42, 34, 26, 18, 
                             10, 2, 59, 51, 43, 35, 27, 
                             19, 11, 3, 60, 52, 44, 36, 
                             63, 55, 47, 39, 31, 23, 15, 
                             7, 62, 54, 46, 38, 30, 22, 
                             14, 6, 61, 53, 45, 37, 29, 
                             21, 13, 5, 28, 20, 12, 4]
    for i in range(56):
        new_key[i] = key[permutation_positions[i]-1]
    new_key = "".join(new_key)
    return new_key


def pc2(key):
    new_key = np.zeros(48)
    permutation_positions = [14, 17, 11, 24, 1, 5, 
                             3, 28, 15, 6, 21, 10,
                             23, 19, 12, 4, 26, 8, 
                             16, 7, 27, 20, 13, 2,
                             41, 52, 31, 37, 47, 55, 
                             30, 40, 51, 45, 33, 48, 
                             44, 49, 39, 56, 34, 53, 
                             46, 42, 50, 36, 29, 32]
    for i in range(48):
        new_key[i] = key[permutation_positions[i]-1]
    new_key = "".join(new_key)
    return new_key


def LS(ci, di, i):
    if i == 1 or i == 2 or i == 9 or i == 16:
        ci = rotation(ci, 1)
        di = rotation(di, 1)
    else:
        ci = rotation(ci, 2)
        di = rotation(di, 2)
    return ci, di


def fill_message(message):
    n = len(message)%64
    message += "0"*n
    return message


def ip(message):
    new_message = np.zeros(64)
    permutation_positions = [58, 50, 42, 34, 26, 18, 10, 2, 
                             60, 52, 44, 36, 28, 20, 12, 4, 
                             62, 54, 46, 38, 30, 22, 14, 6, 
                             64, 56, 48, 40, 32, 24, 16, 8,
                             57, 49, 41, 33, 25, 17, 9, 1, 
                             59, 51, 43, 35, 27, 19, 11, 3, 
                             61, 53, 45, 37, 29, 21, 13, 5, 
                             63, 55, 47, 39, 31, 23, 15, 7]
    for i in range(64):
        new_message[i] = message[permutation_positions[i]-1]
    new_message = "".join(new_message)
    return new_message


def fp(message):
    new_message = np.zeros(64)
    permutation_positions = [40, 8, 48, 16, 56, 24, 64, 32,
                             39, 7, 47, 15, 55, 23, 63, 31, 
                             38, 6, 46, 14, 54, 22, 62, 30, 
                             37, 5, 45, 13, 53, 21, 61, 29,
                             36, 4, 44, 12, 52, 20, 60, 28, 
                             35, 3, 43, 11, 51, 19, 59, 27, 
                             34, 2, 42, 10, 50, 18, 58, 26, 
                             33, 1, 41, 9, 49, 17, 57, 25]
    for i in range(64):
        new_message[i] = message[permutation_positions[i]-1]
    new_message = "".join(new_message)
    return new_message
    

def generate_keys(key):
    keys = []
    cs = []
    ds = []
    keys.append(pc1(key))
    cs.append(keys[0][0:28])
    ds.append(keys[0][28:56])
    for i in range(15):
        ci, di = LS(cs[i], ds[i], i)
        cs.append(ci)
        ds.append(di)
        new_key = pc2(ci + di)
        keys.append(new_key)
    return keys


def DES(message, key, mode="encode"):
    new_message = ""
    message = fill_message(message)
    bin_message = str(util.str_to_ascii_binary(message))
    bin_key = str(util.str_to_ascii_binary(key))
    keys = generate_keys(bin_key)
    ls = [bin_message[0:32]]
    rs = [bin_message[32:64]]
    for i in range(16):
        li = rs[i]
        
    new_message = util.from_ascii_binary(bin_message)
    return new_message