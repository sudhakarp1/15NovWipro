while True:
    try:
        num = int(input('Enter a number: '))
        print(f'The number: {num}')
        break
    except ValueError:
        print('Invalid Number')

