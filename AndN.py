from And import And


def AndN(a, b):
    new = []

    for i in range(len(a)):
        new.append(And(a[i], b[i]))

    return new
