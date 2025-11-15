'''
    [] can be used to create a list
    list.append(element(single value)) can be added at the end

    supports/stores different(mixed) data types
    mutable/modifiable --> data can be modified
    allows duplicates
    can access individual elements through indexing 
    can accesss group of elements through  index slicing
'''
listOne = [10,20, 30, 40, 50] # here [] is to create a list 
print(f'1. listOne: {listOne}')
listOne.append('One')
print(f'2. listOne: {listOne}')
listOne.append(False)
print(f'3. listOne: {listOne}')
listOne.pop(5)
print(f'4. listOne: {listOne}')

'''
print(f'3. listOne: {listOne}')
print(f'4. Indexing: {listOne[0]}')#indexing
print(f'5. Indexing: {listOne[0:4]}')#index slicing
print(f'6. Indexing: {listOne[4]}')
print(f'7. Indexing: {listOne[4:]}')#index slicing
'''