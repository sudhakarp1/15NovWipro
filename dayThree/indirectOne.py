'''
    recursion --> function calling itself indirectly 
    
'''
def funOne(num):
    if num <= 10:
        print(num, end=' ')
        funTwo(num + 1)

def funTwo(num):
    if num <= 10:
        print(num, end=' ')
        funOne(num + 1)

funOne(1)
