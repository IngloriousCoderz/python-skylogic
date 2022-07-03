def add(a):
  def inner_function(b):
    return a + b
  
  return inner_function

add_two = add(2) #?
add_two(3) #?
add(2)(3) #?

for num in range(1, 5):
  add_two(num) #?