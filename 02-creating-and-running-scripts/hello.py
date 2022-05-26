# Usage:
# python hello.py world
# or
# python -m hello world

from sys import argv

print("Message from " + argv[0] + ":")
print("Hello " + argv[1] + "!")
