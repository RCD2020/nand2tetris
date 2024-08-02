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
from OrN import OrN
from MuxN import MuxN


# simulate_function(Xor)
# simulate_absel(Mux)
# simulate_insel(DMux)
# simulate_multibit(OrN, 2)
simulate_multi_absel(MuxN, 1)
