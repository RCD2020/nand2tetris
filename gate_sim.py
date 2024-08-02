from multibit_repr import generate_multi, multi2str

from typing import List


def simulate_function(func):
    print('| a | b | out |')
    print('|---|---|-----|')
    for x in range(0,2):
        for y in range(0,2):
            print(f'| {x} | {y} |  {int(func(x,y))}  |')


def simulate_absel(func):
    print('| a | b | sel | out |')
    print('|---|---|-----|-----|')
    for sel in range(0,2):
        for a in range(0,2):
            for b in range(0,2):
                print(
                    f'| {a} | {b} |  {sel}  |  {int(func(a,b,sel))}  |'
                )


def simulate_insel(func):
    print('| in | sel || a | b |')
    print('|----|-----||---|---|')
    for sel in range(0,2):
        for gate_in in range(0,2):
            a, b = func(gate_in, sel)
            print(f'| {gate_in}  |  {sel}  || {int(a)} | {int(b)} |')


def space_text(text, length, minimum, space):
    length = max(minimum, length)
    length -= len(text)
    half = length // 2
    return f'{space*half}{text}{space*(half + length % 2)}'


def line(text: List[str], length, minimum=5, space=' '):
    string = '|'
    for x in text:
        string += space_text(x, length, minimum, space)
        string += '|'
    
    return string


def simulate_multibit(func, bit_length=2):

    multibits = generate_multi(bit_length)

    length = bit_length + 2

    print(line(['a','b','out'], length))
    print(line(['']*3, length, space='-'))
    for a in multibits:
        for b in generate_multi(bit_length):
            print(line([
                multi2str(a), multi2str(b), multi2str(func(a ,b))
            ], length))


def simulate_multi_absel(func, bit_length):

    multibits = generate_multi(bit_length)

    length = bit_length + 2

    print(line(['a','b','sel','out'], length))
    print(line(['']*4, length, space='-'))
    for a in multibits:
        for b in generate_multi(bit_length):
            for sel in range(2):
                print(line([
                    multi2str(a), multi2str(b),
                    str(sel), multi2str(func(a,b,sel))
                ], length))


if __name__ == '__main__':
    simulate_function(max)
