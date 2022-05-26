# lists behave as stacks already
list = [1, 2, 3]
list.append(4)
list.pop()

# using lists as queues is slow, use deque
from collections import deque

queue = deque([1, 2, 3])
queue.append(4)
queue.popleft()
