# match is pretty much like a switch
status = 200
match status:
  case 200:
    print('Ok')
  case 404:
    print('Not found')
  case 500:
    print('Server error')

# match can also extract components
point = [4, 2]
match point:
  case [0, 0]:
    print("Origin")
  case [0, y]:
    print(f"Y={y}")
  case [x, 0]:
    print(f"X={x}")
  case [x, y] if x == y: # guard: an if clause inside of a case!
    print(f"X and Y={x}")
  case [x, y]:
    print(f"X={x}, Y={y}")
  case _:
    print("Not a point")

# For other features of match @see https://docs.python.org/3/tutorial/controlflow.html#match-statements
