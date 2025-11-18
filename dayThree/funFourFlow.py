'''
    recursion --> function calling itself directly 

'''
def funOne(num):
    if num <= 10:
        print(num, end=' ')
        funOne(num + 1)
        #print(num, end=' ')

funOne(1)
