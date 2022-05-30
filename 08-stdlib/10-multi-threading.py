from threading import Thread
import random, time

numbers = range(1, 5)

def long_task(name):
  print(f'Starting task {name}...')
  time.sleep(random.choice(numbers))
  print(f'Task {name} done.')

# create some threads with a list comprehension
threads = [Thread(target=long_task, args=(i,)) for i in numbers] # args can be a tuple or any other sequence, such as list

print('Starting threads...')
for thread in threads:
  thread.start()
print('Waiting for threads to complete...')
for thread in threads:
  thread.join()
print('All done.')

# A simpler example taken from https://realpython.com/intro-to-python-threading/

from concurrent.futures import ThreadPoolExecutor

print('Starting threads with a pool...')
with ThreadPoolExecutor(max_workers=4) as executor:
  executor.map(long_task, numbers)
print('All done.')
