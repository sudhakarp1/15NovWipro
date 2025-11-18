x, y, z = 10, 20, 30
print(f'X: {x}\t\tY:{y}\t\tZ:{z}')
x, y, *z = 10, 20, 30, 40, 50
print(f'X: {x}\t\tY:{y}\t\tZ:{z}')
x, *y, z = 10, 20, 30, 40, 50
print(f'X: {x}\t\tY:{y}\t\tZ:{z}')
*x, y, z = 10, 20, 30, 40, 50
print(f'X: {x}\t\tY:{y}\t\tZ:{z}')
x, y, *z = 10, 20
print(f'X: {x}\t\tY:{y}\t\tZ:{z}')