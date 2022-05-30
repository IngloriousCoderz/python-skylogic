import math

math.sin(math.pi / 2) # 1.0
math.log(1024, 2) # 10.0

import random

random.choice(['apple', 'orange', 'banana']) # random item from the list
random.sample(range(100), 10) # list of 10 numbers from 0 to 199
random.random() # floating point between 0 and 1
random.randrange(6) # integer between 0 and 5

import statistics
data = [7, 7, 8, 6, 9, 7, 5, 6]
statistics.mean(data) # 6.875
statistics.median(data) # 7.0 (middle value)
statistics.variance(data) # 1.55... (spread or dispersion)

# For more complex maths @see https://scipy.org/
# Quote Anaconda, a scientific Python distribution