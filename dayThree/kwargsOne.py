'''
    Purpose:
      Demonstrate kwargs 
      Demonstrate all types of arguments 
            positional arguments
            variable(arbitrary) number of args 
            kwargs (key word args)
'''

def funOne(**kwargs):
    '''
        usage of funOne() 
            funOne(taking key word arguments only)
            print the arguments using key() and values()
    '''
    print(f'kwargs: {kwargs}')
    print(f'Keys: {kwargs.keys()}')
    print(f'Values: {kwargs.values()}')
    '''
        Additional Comments added here
    '''

def funTwo(x,y,*args, **kwargs):
    '''
        usage of funTwo() 
            positional parameters
            variable number of arguments
            funTwo(taking key word arguments)
            print the arguments using key() and values()
    '''
    print(f'X: {x}\tY: {y}\tArgs: {args}\nkwargs: {kwargs}')

def funThree():
    '''
        Usage of funThree()
            an empty function
    '''
    pass 

print(f'funThree: {funThree()}')
funOne(x=1, y=2, name='Sudhakar', fname='Palanivelu')
funTwo(10,20,30,40,50,name='Sachin',name2='Virat')

print(__doc__) #dunder doc 
print(funOne.__doc__)
print(funTwo.__doc__)
print(funThree.__doc__)
'''
help(funOne)
help(funTwo)
help(funThree)

help('__main__') #dunder main
'''