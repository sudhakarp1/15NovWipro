'''
    Introduction to modules in python
'''

data = 100

def funOne():  
    print(f'Inside funOne() data: {data}')

def funTwo():  
    print(f'Inside funTwo() data: {data}')

def funThree():  
    print(f'Inside funThree() data: {data}')

if __name__ == '__main__':
    funOne()
    funTwo()
    funThree()