import copy

lst = [10, 20,[1, 2, 3, 4], 30, 40, 50]

copyOne = copy.copy(lst) #shallow copy
copyTwo = copy.deepcopy(lst) #Deep copy
lst[2].extend((11,22,33,44))

print(f'lst: {lst}')
print(f'copyOne: {copyOne}')
print(f'copyTwo: {copyTwo}')
