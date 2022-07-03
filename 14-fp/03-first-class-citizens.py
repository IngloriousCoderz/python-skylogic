def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def perform_calculation(calculation, operands):
  return [calculation(a, b) for a, b in operands]

operands = [(2, 3), (3, -5), (42, 39)]

perform_calculation(add, operands) #?
perform_calculation(subtract, operands) #?
