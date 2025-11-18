def funOne():
    print(f'1. funOne()')
    funTwo()
    print(f'2. funOne()')

def funTwo():
    print(f'1. funTwo()')
    funThree()
    print(f'2. funTwo()')

def funThree():
    print(f'1. funThree()')
    funFour()
    print(f'2. funThree()')

def funFour():
    print('funFour')

funOne()