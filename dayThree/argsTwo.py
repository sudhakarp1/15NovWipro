
def funOne(x,y,z):
    print(f'X: {x}\t\tY:{y}\t\tZ:{z}')

def funTwo(x,y,*z):
    print(f'X: {x}\t\tY:{y}\t\tZ:{z}')

def funThree(x,z,*y):
    print(f'X: {x}\t\tY:{y}\t\tZ:{z}')

funOne(10, 20, 30)
funTwo(10, 20, 30, 40, 50)
funThree(10, 20, 30, 40, 50)