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


if __name__ == '__main__':
    simulate_function(max)
