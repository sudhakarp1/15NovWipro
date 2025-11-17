num = int(input('Enter a num: '))
for j in range(2):
    printHeader = 'Odd: ' if num % 2 else 'Even: '
    print(printHeader, end='')
    for i in range(0, 10, 2):
        print(num + i, end='  ')
    print()
    num+=1
