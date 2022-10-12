a:int = int(input('dszh egyik befogója (cm): '))
b:int = int(input('dszh másik befogója (cm): '))

if a <= 0 or b <= 0:
    print('ez nem lehet háromszög')
else:
    print(f'átfogó hossza: {(a ** 2 + b ** 2) ** .5} cm')