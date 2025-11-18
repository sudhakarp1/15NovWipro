def funOne(arg):#one positional parameter    
    if type(arg) == type(int()):
        print(f'Int arg: {arg}')
    elif type(arg) == type(list()):
        print(*arg)
    else:
        print(f'Other: {arg} type: {type(arg)}')

funOne(10)
funOne((10,))
funOne((10,20,30,40,50))
funOne([10,20,30,40,50])