from nand import nand

from Not import Not
from And import And


def Xor(a, b):
    return And(nand(a, b), Not(And(Not(a), Not(b))))
