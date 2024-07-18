def simulate_function(func):
    print('| a | b | out |')
    print('|---|---|-----|')
    for x in range(0,2):
        for y in range(0,2):
            print(f'| {x} | {y} |  {func(x,y)}  |')


if __name__ == '__main__':
    simulate_function(max)