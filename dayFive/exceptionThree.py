try:
    print(f'statement #1')
    #raise TypeError('No Matter What type')
    print(f'statement #2')
    raise ValueError('Some message')
    print(f'statement #3')
except TypeError as var:
    print(f'1. Messg: {var}')
except ValueError as var:
    print(f'2. Messg: {var}')

