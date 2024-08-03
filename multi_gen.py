for i in range(4):
    for i2 in range(4):
        print(f'Mux(a=a[{4*i+i2}], b=b[{4*i+i2}], sel=sel, out=out[{4*i+i2}]);')
    print()