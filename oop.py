# terminologies 
# 1. Inheritance
# 2. Encaptulation
# 3. Instance 
# 4. Polymorphism
#  Defining a new class 

class Player:
    pass

# A class is consist of State, Behavior (function) and  Identify 

class Dog:
    color = 'Red'
    age = 2
    def display(self): # this = self in python
        print(self.color)
        print(self.age)

dog1 = Dog()
print(dog1.color)
dog1.display()
print(type(Dog))

# Passing user input to a class 
class User:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def show(self):
        print(self.name)
        print(self.country)
user1 = User('Nahid', 'Bangladesh')
print(user1.name)
