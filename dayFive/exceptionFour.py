class MyException(Exception): #Custom Exception Type
    pass

try:
    print(f'statement #1')
    raise MyException('No Matter What type')
    print(f'statement #2')    
except MyException as var:
    print(f'1. Messg: {var}')
except ValueError as var:
    print(f'2. Messg: {var}')