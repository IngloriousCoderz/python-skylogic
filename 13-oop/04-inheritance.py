class Person:
  legs = 2

  def __init__(self, first_name, last_name, date_of_birth):
    self.first_name = first_name
    self.last_name = last_name
    self.date_of_birth = date_of_birth

  def speak(self):
    return f"Hi! My name is {self.first_name} and I have {self.legs} legs."

class Dog(Person):
  legs = 4

  def speak(self):
    message = super().speak()
    tokens = message.split('!')
    return f"Woof!{tokens[1]}"

dog = Dog('Arya', 'Mistretta', '2014-12-10')
dog.speak() #?

# You can even achieve some sort of multiple inheritance, @see https://docs.python.org/3/tutorial/classes.html#multiple-inheritance
# For private variables @see https://docs.python.org/3/tutorial/classes.html#private-variables
