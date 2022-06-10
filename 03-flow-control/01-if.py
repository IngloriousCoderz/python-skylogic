number = 42

guess = int(input('Guess my number: '))

if guess < number:
  print('Too low')
elif guess > number:
  print('Too high')
else:
  print('Kudos!')

# shorthand, @see https://www.w3schools.com/python/python_conditions.asp

a = 2
b = 330
print('A') if a > b else print('B')
