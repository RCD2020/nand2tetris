from Or import Or


def OrN(a,b):
    new = []

    for i in range(len(a)):
        new.append(Or(a[i], b[i]))

    return new
