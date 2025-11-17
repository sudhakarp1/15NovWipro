'''
    using str.format()
'''

num, name, sal = 10001, 'Sudhakar Palanivelu', 234.456
res = 'Num: {}\t\tName: {}\t\tSal: {}'.format(num, name, sal)
print(res)

res = 'Num: {2}\t\tName: {0}\t\tSal: {1}'.format(num, name, sal)
print(res)

print('Num: {2}\t\tName: {0}\t\tSal: {1}'.format(num, name, sal))