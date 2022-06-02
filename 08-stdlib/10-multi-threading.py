from threading import Thread
import random, time

numbers = range(1, 5)

# Simple multi-threading: just wait for tasks to complete

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

# Collecting the results is trickier: we need to store results in a list

results = [None for _ in numbers]

def long_task(name):
  print(f'Starting task {name}...')
  time.sleep(random.choice(numbers))
  print(f'Task {name} done.')
  index = name - 1
  results[index] = name

threads = [Thread(target=long_task, args=(i,)) for i in numbers]

print('Starting threads...')
for thread in threads:
  thread.start()
print('Waiting for threads to complete...')
for thread in threads:
  thread.join()
print('Tasks', [result for result in results], ': all done.')

# A simpler and better way, taken from https://realpython.com/intro-to-python-threading/

from concurrent.futures import ThreadPoolExecutor

def long_task(name):
  print(f'Starting task {name}...')
  time.sleep(random.choice(numbers))
  print(f'Task {name} done.')
  return name

print('Starting threads with a pool...')
with ThreadPoolExecutor(max_workers=4) as executor:
  results = executor.map(long_task, numbers)
print('Tasks', [result for result in results], ': all done.')
