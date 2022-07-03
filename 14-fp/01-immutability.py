person = {'name': 'Matteo Antony', 'age': 39 }

def impure_increase_age(person):
  person['age'] += 1
  return person

new_person = impure_increase_age(person) #?
person #?
print(new_person == person)

def pure_increase_age(person):
  new_person = person.copy()
  new_person['age'] += 1
  return new_person

new_person = pure_increase_age(person) #?
person #?
print(new_person == person)
