print('HalfAdder(a=a[0], b=b[0], sum=out[0], carry=c0);')

for x in range(1, 16):
    print(f'FullAdder(a=a[{x}], b=b[{x}], c=c{x - 1}, sum=out[{x}], carry=c{x});')