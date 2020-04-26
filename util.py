def generate_ascii_dic():
    ascii_dic = {}
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(alphabet)):
        ascii_dic[alphabet[i]] = i+65
    for i in range(10):
        ascii_dic[str(i)] = i+48
    return ascii_dic
    

def to_ascii_binary(message):
    ascii_dic = generate_ascii_dic()
    ans = ""
    for i in range(len(message)):
        ans += "0" + str(bin(ascii_dic[message[i]])[2:])    
    return ans


def from_ascii_binary(message):
    