from And import And
from Xor import Xor


def Or(a, b):
    return Xor(Xor(a, b), And(a, b))
