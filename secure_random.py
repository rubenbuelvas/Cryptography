def frecuency_test(bits):
    x1 = 0
    n = len(bits)
    n0, n1 = 0, 0
    for bit in bits:
        if bit == 0:
            n0 += 1
        elif bit == 1:
            n1 += 1
    x1 = ((n0-n1)**2)/n
    return x1


def serial_test(bits):
    x2 = 0
    n = len(bits)
    n0, n1 = 0, 0
    n00, n01, n10, n11 = 0, 0, 0, 0
    for i in range(len(bits)-1):
        if bits[i] == 0:
            n0 += 1
        elif bits[i] == 1:
            n1 += 1
        if bits[i] == 0 and bits[i+1] == 0:
            n00 += 1
        elif bits[i] == 0 and bits[i+1] == 1:
            n01 += 1
        elif bits[i] == 1 and bits[i+1] == 0:
            n10 += 1
        elif bits[i] == 1 and bits[i+1] == 1:
            n11 += 1
    x2 = ((4/(n-1))*(n00**2+n01**2+n10**2+n11**2)) - ((2/n)*(n0+n1))+1
    return x2


def poker_test():
    return 0


def corridos():
    return 0


def autocorrelation_test():
    return 0