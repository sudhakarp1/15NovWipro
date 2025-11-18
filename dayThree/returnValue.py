def funOne():
    return 10

def funTwo():
    return 10,20,30,40,50

def funThree():
    x,y,z=10,20,30
    return f'X: {x}\t\tY: {y}\t\tZ:{z}'

res = funOne()
print(res)
res = funTwo()
print(res)

for i in res:
    print(i, end=',')
print()

res = funThree()
print(res)

