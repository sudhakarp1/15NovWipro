num = int(input('Enter a num: '))
printHeader = 'Odd: ' if num % 2 else 'Even: '
print(printHeader, end='')
for i in range(0, 10, 2):
    print(num + i, end='  ')
num+=1
printHeader = 'Odd: ' if num % 2 else 'Even: '
print(f'\n{printHeader}', end='')
for i in range(0, 10, 2):
    print(num + i, end='  ')
print()
