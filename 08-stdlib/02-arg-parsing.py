
import sys

print(sys.argv) # ['02-args-parsing.py'] at first, then it contains the args

import argparse

parser = argparse.ArgumentParser(description='Sums two numbers')
parser.add_argument('a', type=int, help="First number")
parser.add_argument('b', type=int, help="Second number")
parser.add_argument('-v', '--verbose', action='store_true', help='Pretty print the result')

namespace = parser.parse_args()
args = vars(namespace) # built-in function, @see https://docs.python.org/3/library/argparse.html#the-namespace-object
print(args)

result = args['a'] + args['b']

if args['verbose']:
  print('The sum of', args['a'], 'and', args['b'], 'is', result)
else:
  print(args['a'], '+', args['b'], '=', result)

# python 02-arg-parsing.py
# python 02-arg-parsing.py -h
# python 02-arg-parsing.py 2 3
# python 02-arg-parsing.py -v 2 3

# For more sofisticated arg parsing @see https://docs.python.org/3/library/argparse.html
