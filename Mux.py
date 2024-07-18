from And import And
from Xor import Xor
from Or import Or


def Mux(a, b, sel):
    return Xor(
        sel, Xor(
            Or(sel, a),
            And(sel, b)
        )
    )
