from nand import nand


def NandN(a, b):
    new = []

    for i in range(len(a)):
        new.append(nand(a[i], b[i]))

    return new
