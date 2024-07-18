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


if __name__ == '__main__':
    simulate_function(max)
