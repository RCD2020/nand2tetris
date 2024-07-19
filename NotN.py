from Not import Not


def NotN(a, _=0):
    new = []

    for x in a:
        new.append(Not(x))

    return new
