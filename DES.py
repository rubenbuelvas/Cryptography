from util import * 

def delete_extra_bits(key):
    new_key = ""
    if len(key) == 56:
        new_key = key
    else:
        for i in range(8):
            new_key += key[i*8:i*8+7]
    return new_key


def rotation(message, n):
    for i in range(n):
        tmp = message.pop(0)
        message.append(tmp)
    return message


def pc1(key):
    new_key = ""
    key = delete_extra_bits(key)
    #permutation
    return new_key


def pc2(key):
    new_key = ""
    key = delete_extra_bits(key)
    #permutation
    return new_key


def LS(ci, di, i):
    if i == 1 or i == 2 or i == 9 or i == 16:
        ci = rotation(ci, 1)
        di = rotation(di, 1)
    else:
        ci = rotation(ci, 2)
        di = rotation(di, 2)
    return ci, di


def generate_keys(key):
    keys = []
    cs = []
    ds = []
    keys.append(pc1(key))
    for i in range(16):
        cs.append(keys[i][0:28])
        ds.append(keys[i][28:56])
        ci, di = LS(cs[i], ds[i], i)
        new_key = pc2(int(str(ci)+str(di)))
        keys.append(new_key)
    return keys


def DES_algorithm(message, key, mode="encode"):
    new_message = ""
    keys = generate_keys(key)
    return new_message