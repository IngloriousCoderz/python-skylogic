basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
basket # prints {'banana', 'pear', 'orange', 'apple'}, in a seemingly random order
'orange' in basket # returns True

a = set('abracadabra')
a # prints {'c', 'd', 'b', 'r', 'a'}
b = set('alacazam')
a - b # difference
a & b # intersection
a | b # union
a ^ b # union minus intersection

my_list = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
my_list = list(set(my_list)) # doesn't preserve items order!
print(my_list)
