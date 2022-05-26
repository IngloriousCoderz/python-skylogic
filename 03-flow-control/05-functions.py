# invoking prior to defining leads to an error
# print_sum(2, 3)

def print_sum(a, b):
  print(a + b)

print(print_sum)
print_sum(2, 3)

def sum(a, b):
  return a + b

print(sum(2, 3))

def to_be_implemented(): # use snake case as a naming convention
  pass # use pass as a placeholder

def create_point(x=0, y=0): # default argument values
  return [x, y]

 # positional argument + keyword argument
print(sum(2, b=3)) # kw args must always follow pos args

# dynamic positional and keyword arguments
def define_person(name, *arguments, **keywords):
  print(name)
  for arg in arguments:
    print(arg)
  for kw in keywords:
    print(f"{kw}: {keywords[kw]}")

define_person('Antony', 'JavaScript', 'Python', date_of_birth='1982-10-17', eyes=2)

# For extra features of function @see https://docs.python.org/3/tutorial/controlflow.html#special-parameters

# lambdas are small anonymous functions
square = lambda num: num**2
sum = lambda a, b: a + b

# annotations and documentation
def sum(a: float, b:float) -> float:
  """
  Functions are documented with
  multiline strings
  """
  return a + b

print(sum.__doc__)
print(sum.__annotations__)

# functions can mute code without having to comment it out!
