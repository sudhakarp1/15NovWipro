'''
    List comprehension
        It is a one liner (single line syntax) for creating 
        a list with some values in a short value
    Syntax:
        [expression for var in iterable]

#Example 1:
lst = [i for i in range(11)]
print(lst)

#Example 2:
lst = [i for i in range(11) if i % 2]
print(lst)

#Example 3:
inpStr = '1 2 3 4 10 20 30 40 50'
lst = [int(i) for i in inpStr.split()]
print(lst)
#Example 4:
lst = [i * i if i % 2 == 0 else i+1 for i in range(11)]
print(lst)
'''
#Example 5:
lst = [i * j for i in range(1,5) for j in range(1,5)]
print(lst)

#Example 6:
lst = [[i * j for i in range(1,5)] for j in range(1,5)]
print(lst)
