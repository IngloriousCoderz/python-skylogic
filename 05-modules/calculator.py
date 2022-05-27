# import this file as in main

def sum(a, b):
  return a + b


# Usage:
# python calculator.py 2 3

if __name__ == "__main__":
  import sys
  a = int(sys.argv[1])
  b = int(sys.argv[2])
  print(sum(a, b))

