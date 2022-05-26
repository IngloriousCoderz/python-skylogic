number = 42

guess = int(input('Guess my number: ')) # user input and conversion!

if guess < number:
  print('Too low')
elif guess > number:
  print('Too high')
else:
  print('Kudos!')
