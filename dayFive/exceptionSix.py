class MyException(Exception): #Custom Exception Type
    def __init__(self, msg, num):
        self.num = num
        self.mesg = msg
        super().__init__(f'{msg}: {num}')

try:
    print(f'statement #1')
    raise MyException('No Matter What type', 100)
    print(f'statement #2')    
except ValueError as var:
    print(f'2. Messg: {var}')
except MyException as var:
    print(f'1. Messg: {var}')
