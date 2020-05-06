def to_ascii_binary(message):
    ans = ""
    for i in range(len(message)):
        ans += "0" + str(bin(ord(message[i]))[2:])    
    return ans


def from_ascii_binary(message):
    ans = ""
    for i in range(int(len(message)/8)):
        my_bin = message[i*8:i*8+8]
        my_bin = "0b" + my_bin[1:]
        ascii_code = int(my_bin, 2)
        ans += str(chr(ascii_code))
    return ans


def xor(a, b):
    c = ""
    for i in range(len(a)):
        if a == "0" and b == "0":
            c += "0"
        elif a == "0" and b == "1":
            c += "1"
        elif a == "1" and b == "0":
            c += "1"
        elif a == "1" and b == "0":
            c += "0"
    return c