# Usage:
# python hello.py world
# or
# python -m hello world

from sys import argv

print(f"Message from {argv[0]}:")
print(f"Hello {argv[1]}!")
