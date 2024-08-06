print('HalfAdder(a=in[0], b=true, sum=out[0], carry=c0);')
for i in range(1, 16):
    print(
        f'HalfAdder(a=in[{i}], b=c{i-1}, sum=out[{i}], carry=c{i});'
    )