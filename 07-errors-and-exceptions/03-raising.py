raise NameError('What an ugly name!')
raise ValueError # same as raise ValueError()

try:
  raise NameError('What an ugly name!')
except NameError as error:
  print(error)
  raise # try with and without raising

# Exception chaining

try:
  raise NameError('What an ugly name!')
except NameError as error:
  raise RuntimeError('Script exploded') from error

# Some exceptions are chained by default

try:
  open('myfile.txt')
except OSError:
  raise RuntimeError from None # prevents chaining

try:
  raise KeyboardInterrupt
finally: # executed as the last task before the try statement completes
  print('Goodbye world!')
