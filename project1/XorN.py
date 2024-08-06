from Xor import Xor


def XorN(a, b):
    new = []

    for i in range(len(a)):
        new.append(Xor(a[i], b[i]))

    return new
