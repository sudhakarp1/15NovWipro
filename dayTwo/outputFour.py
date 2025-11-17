'''
    Using f'strings'
'''
nuWidth, naWidth, sWidth = 7, 24, 10.2

num, name, sal = 10001, 'Sudhakar Palanivelu', 234.456
print(f'Num: {num:d}\t\tName: {name:s}\t\tSal: {sal:.2f}')
print('-' * 60)
print(f'Num: {num:{nuWidth}d}\t\tName: {name:{naWidth}s}\t\tSal: {sal:{sWidth}f}')
