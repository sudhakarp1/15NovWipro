'''
   python cmdTwo.py "10 * 20 - 40"
   # --> (eval()
'''
import argparse

parse = argparse.ArgumentParser(description='Expression')
parse.add_argument('expr',  help='Expression evaluation(10 * 20 - 30)')

args = parse.parse_args()
res = eval(args.expr)
print(f'Result: {res}')
