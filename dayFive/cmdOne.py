'''
    10 * 20 - 40 --> (eval())
'''
import argparse

parse = argparse.ArgumentParser(description='Simple calc')

parse.add_argument('operand1', type=int, help='First Number')
parse.add_argument('operator', choices=['+', '-', '*', '/'], help='Operator(+, -, *, /)')
parse.add_argument('operand2', type=int, help='second Number')

args = parse.parse_args()
if args.operator == '+':
    res = args.operand1 + args.operand2
elif args.operator == '-':
    res = args.operand1 - args.operand2
elif args.operator == '*':
    res = args.operand1 * args.operand2
elif args.operator == '/':
    res = args.operand1 // args.operand2
else:
    print('Invalid Operator')

print(f'Result: {res}')
#print(f'Eval: {eval("10 * 20 - 40")}')