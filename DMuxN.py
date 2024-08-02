from DMux import DMux


def DMuxN(gate_in, sel):
    newa, newb = [], []

    for i in range(len(gate_in)):
        a, b = DMux(gate_in[i], sel)

        newa.append(a)
        newb.append(b)

    return newa, newb
