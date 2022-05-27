# Usage:
# python hello.py world
# or
# python -m hello world

from sys import argv

print(f"Message from {argv[0]}:")
print(f"Hello {argv[1]}!")

# Sidenote: let's play with the print function

print('Hello', 'world') # multiple args are concatenated

print('Hello', 'world', sep=', ') # custom separator
print('home', 'iceonfire', 'code', sep='/') # useful for paths

print('Hello', 'world', end='!\n') # custom end
print('Checking file integrity...', end='') # prevent line breaks
print('ok')
