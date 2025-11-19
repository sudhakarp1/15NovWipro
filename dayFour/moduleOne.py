dataOne, dataTwo, dataThree = 1000, "Some String", 234.45

def funOne():
    print(f'in funOne()... Module: {__name__}')

def funTwo():
    print(f'in funTwo()... Module: {__name__}')

def funThree():
    print(f'in funThree()... Module: {__name__}')

if __name__ == '__main__':
    funOne()
    funTwo()

