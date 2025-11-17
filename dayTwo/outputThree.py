'''
    Using f'strings'
'''

num, name, sal = 10001, 'Sudhakar Palanivelu', 234.456
print(f'Num: {num:d}\t\tName: {name:s}\t\tSal: {sal:.2f}')
print(f'Num: {num:7d}\t\tName: {name:24s}\t\tSal: {sal:10.2f}')
print(f'Num: {num:<7d}\t\tName: {name:<24s}\t\tSal: {sal:<10.2f}')
print(f'Num: {num:>7d}\t\tName: {name:>24s}\t\tSal: {sal:>10.2f}')
print(f'Num: {num:^7d}\t\tName: {name:^24s}\t\tSal: {sal:^10.2f}')