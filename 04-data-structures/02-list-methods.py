list = [1, 2, 3]

list.append(4)
list[len(list):] = [5] # equivalent to above

list.extend(range(6, 8))
list[len(list):] = [8, 9, 10] # equivalent to above

list.insert(index, item)
list.remove(item) # removes first occurence, raises error if no such item
list.pop(index) # removes item and returns it
list.pop() # removes last item and returns it

list.clear()
del list[:] # equivalent to above
# digression: the del statement removes iems by index(es)
del list[0]
del list[2:4]
del list[:]
del list # removes the variable
del _ # doesn't work!

list.index(item) # returns index of first occurrence
list.index(item, start, end) # optional args limit the search

list.count(item) # counts occurrences
list.sort() # sorts items alphabetically and numerically, for optional args @see https://docs.python.org/3/library/functions.html#sorted
list.reverse() # reverses the list
list.copy() # creates a shallow clone
list[:] # equivalent to above
