class Person:
  pass

person = Person()
person.first_name = 'Matteo Antony'
person.last_name = 'Mistretta'
person.date_of_birth = '1982-10-71'
vars(person) #?

def stringify(obj):
  dictionary = vars(obj)
  lines = [f"{key}: {value}" for key, value in dictionary.items()]
  return '\n'.join(lines)

print(stringify(person))

# For objections on OOP @see https://betterprogramming.pub/object-oriented-programming-the-trillion-dollar-disaster-92a4b666c7c7
# Also @see the referenced https://cscalfani.medium.com/goodbye-object-oriented-programming-a59cda4c0e53