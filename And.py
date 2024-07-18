from nand import nand

from Not import Not


def And(a, b):
    return Not(nand(a,b), 0)
