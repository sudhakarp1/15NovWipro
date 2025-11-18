def printCalendar(w, max):
    print(f'Sun Mon Tue Wed Thu Fri Sat')
    print(' ' * 3 * w, end='') 
    for i in range(1, max + 1):
        print(f'{i:<3}',end='')
        if (i+w) % 7 ==0:
            print()
    print()

printCalendar(4, 30)
printCalendar(0, 31)
printCalendar(1, 31)
printCalendar(3, 28)