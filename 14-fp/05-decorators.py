def say_hello():
  return 'hello world!'

print('Logging no-arg function:')

def add_logging(func):
  print('Before function...')
  result = func()
  print('After function.')
  return result

print(add_logging(say_hello))

print('Logging function with args:')

def subtract(a, b):
  return a - b

def add_logging(func, *args):
  print('Before function...')
  result = func(*args)
  print('After function.')
  return result

print(add_logging(subtract, 2, 3))

print('Higher-order function:')

def add_logging(func):
  def inner_func(*args):
    print('Before function...')
    result = func(*args)
    print('After function.')
    return result
  
  return inner_func

subtract_with_logging = add_logging(subtract)
print(subtract_with_logging(2, 3))

print('Decorator:')

@add_logging
def subtract(a, b):
  return a - b

print(subtract(2, 3))

print('Cached results:')

from functools import cache

@cache
def performant_factorial(n):
  print('Computing factorial of ', n)
  return n * performant_factorial(n - 1) if n > 1 else 1

print('Factorial of 5:', performant_factorial(5))
print('Factorial of 3:', performant_factorial(3))
print('Factorial of 7:', performant_factorial(7))
