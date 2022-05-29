# number = int(input('Please enter a number: ')) # raises ValueError for non-numbers

number = None
while number is None:
  try:
    number = int(input('Please enter a number: '))
  except ValueError:
    print("Oops, that's not a number!")

print('Your number is ', number)

# Catching multiple exceptions at once

try:
  pass
except (RuntimeError, TypeError, NameError):
  pass

# Catching exceptions individually

import sys

try:
  f = open('myfile.txt')
  s = f.readline()
  i = int(s.strip())
except OSError as err:
  print("OS error: {0}".format(err))
except ValueError:
  print("Could not convert data to an integer.")
except BaseException as err: # all exceptions inherit from BaseException, so we can catch anything that wasn't caught before
  print(f"Unexpected {err=}, {type(err)=}")

# The else clause is executed after the try if no exception was raised, Python-only

try:
  f = open('myfile.txt', 'r')
except OSError:
  print('Cannot open file')
else:
  print('File has', len(f.readlines()), 'lines')
  f.close()

# For extra exception features @see https://docs.python.org/3/tutorial/errors.html