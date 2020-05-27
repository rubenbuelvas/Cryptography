import util


def frecuency_test(bits):
    x = 0
    n = len(bits)
    n0, n1 = 0, 0
    for bit in bits:
        if bit == "0":
            n0 += 1
        elif bit == "1":
            n1 += 1
    print(n0, n1)
    x = ((n0-n1)**2)/n
    return x


def serial_test(bits):
    x = 0
    n = len(bits)
    n0, n1 = 0, 0
    n00, n01, n10, n11 = 0, 0, 0, 0
    for i in range(len(bits)):
        if bits[i] == "0":
            n0 += 1
        elif bits[i] == "1":
            n1 += 1
    for i in range(len(bits)-1):
        if bits[i] == "0" and bits[i+1] == "0":
            n00 += 1
        elif bits[i] == "0" and bits[i+1] == "1":
            n01 += 1
        elif bits[i] == "1" and bits[i+1] == "0":
            n10 += 1
        elif bits[i] == "1" and bits[i+1] == "1":
            n11 += 1
    x = ((4/(n-1)) * (n00**2+n01**2+n10**2+n11**2)) - ((2/n)*(n0**2+n1**2)) + 1
    return x


def poker_test(bits, m):
    x = 0
    n = len(bits)
    ms = []
    ns = []
    k = int(n/m)
    for i in range(2**m):
        c = str(int(util.dec_to_bin(i)))
        c = ("0"*(m-len(c))) + c
        ms.append(c)
    for i in range(2**m):
        ni = 0
        for j in range(k):
            sub_bits = bits[j*m:j*m+m]
            if sub_bits == ms[i]:
                ni += 1
        ns.append(ni)
    for i in range(2**m):
        x += ns[i]**2
    x = ((2**m)/k) * x
    x = x - k
    return x


def corridos():
    return 0


def autocorrelation_test():
    return 0


s = "e3114ef249e3114ef249e3114ef249e3114ef249"
s = util.hex_to_bin(s)
print(frecuency_test(s))
print(serial_test(s))
print(poker_test(s, 3))