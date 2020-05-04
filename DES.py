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
    message = list(message)
    for i in range(n):
        tmp = message.pop(0)
        message.append(tmp)
    message = "".join(message)
    return message


def pc1(key):
    new_key = ""
    new_key = delete_extra_bits(key)
    #permutation
    return new_key


def pc2(key):
    new_key = ""
    new_key = delete_extra_bits(key)
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
    cs.append(keys[0][0:28])
    ds.append(keys[0][28:56])
    for i in range(15):
        ci, di = LS(cs[i], ds[i], i)
        cs.append(ci)
        ds.append(di)
        new_key = pc2(ci + di)
        keys.append(new_key)
    return keys


def DES_algorithm(message, key, mode="encode"):
    key = str(to_ascii_binary(key))
    new_message = ""
    keys = generate_keys(key)
    print(len(keys))
    print(keys)
    return new_message