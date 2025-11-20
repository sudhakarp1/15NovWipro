try:
    num = int(input('Enter a num: '))
    res = 100 // num 
    print(f'Result: {res}')
except ZeroDivisionError:
    print('Cannot divide by zero')
except ValueError:
    print('Invalid Number')
else:
    print('Division done successfully')
finally:
    print('End of the Program')
