person = {'name': 'Antony', 'date_of_birth': '1982-10-17', 'eyes': 2}
person['name'] # there is no dot notation, like 'person.name'
person['nose'] = 1 # add
person['nose'] = 2 # change
del person['nose'] # delete
list(person) # list of keys
sorted(person) # sorted list of keys
'name' in person # returns True

dict([('name', 'Antony'), ('date_of_birth', '1982-10-17'), ('eyes', 2)]) # build from list of tuples

# For extra features of dict @see https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

person.items() # returns a list of tuples

for key, value in person.items(): # iterate over dictionary
  print(key, value)

for index, item in enumerate(['tic', 'tac', 'toe']): # iterate over both index and item
  print(index, item)