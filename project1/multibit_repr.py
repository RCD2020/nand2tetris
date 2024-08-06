from typing import List


def multi(multibit_repr: str) -> List[int]:
    return [int(x) for x in multibit_repr]


def multi2str(multibit: List[int]) -> str:
    return ''.join((str(int(x)) for x in multibit))


def generate_multi(bit_length: int) -> List[int]:
    multis = []

    for x in range(2**bit_length):
        binary = bin(x)[2:]
        multis.append('0'*(bit_length - len(binary)) + binary)

    return [multi(x) for x in multis]


if __name__ == '__main__':
    # a = multi('1001010110')
    # print(a)
    # print(multi2str(a))

    print(generate_multi(4))
