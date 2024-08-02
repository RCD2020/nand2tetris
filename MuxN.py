from Mux import Mux


def MuxN(a,b,sel):
    new = []

    for i in range(len(a)):
        new.append(Mux(a[i],b[i],sel))

    return new
