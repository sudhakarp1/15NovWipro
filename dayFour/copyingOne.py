lst = [10, 20,[1, 2, 3, 4], 30, 40, 50]

def funOne(arg):
    print(f'arg: {arg}')
    lst.extend((1000,2000,3000))
    lst[2].extend((11,22,33,44))

funOne(lst)
print(f'Lst: {lst}')
