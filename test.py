from gate_sim import *

from nand import nand
from Not import Not
from And import And
from Xor import Xor
from Or import Or
from Mux import Mux
from DMux import DMux
from NandN import NandN
from NotN import NotN
from AndN import AndN
from XorN import XorN


# simulate_function(Xor)
# simulate_absel(Mux)
# simulate_insel(DMux)
simulate_multibit(XorN, 2)
