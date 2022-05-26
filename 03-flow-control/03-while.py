i = 0
while i < 6:
  print(i)
  i = i + 1

# break and else
num = 1
while num < 6:
  if num % 2 == 0:
    print('Found an even number:', num)
    break
  num = num + 1
else: # Python-only, @see https://www.pythontutorial.net/python-basics/python-while-else/
  print('No even numbers found')

number = 42
game_over = False

while game_over == False:
  guess = int(input('Guess my number: '))

  if guess < number:
    print('Too low')
  elif guess > number:
    print('Too high')
  else:
    print('Kudos!')
    game_over = True
