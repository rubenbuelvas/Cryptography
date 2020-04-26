def generate_ascii_dict():
    ascii_dic = {}
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(alphabet)):
        ascii_dic[alphabet[i]] = i+65
        ascii_dic[i+65] = alphabet[i]
    for i in range(10):
        ascii_dic[str(i)] = i+48
        ascii_dic[i+48] = str(i)
    return ascii_dic
    
ascii_dict = generate_ascii_dict()


def to_ascii_binary(message, ascii_dict=ascii_dict):
    ans = ""
    for i in range(len(message)):
        ans += "0" + str(bin(ascii_dict[message[i]])[2:])    
    return ans


def from_ascii_binary(message, ascii_dict=ascii_dict):
    ans = ""
    for i in range(int(len(message)/8)):
        my_bin = message[i*8:i*8+8]
        my_bin = "0b" + my_bin[1:]
        ascii_code = int(my_bin, 2)
        ans += str(ascii_dict[ascii_code])
    return ans