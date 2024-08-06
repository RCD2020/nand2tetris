from Mux import Mux


def DMux(gate_in, sel):
    return (
        Mux(gate_in, 0, sel),
        Mux(0, gate_in, sel)
    )
