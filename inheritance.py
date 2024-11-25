# Data sharing between inheritance
class BaseClass:
    myProperty = 'hello'

class Derivative(BaseClass):
    derivativeProp = 'world'
    def display(self):
        print(self.myProperty,self.derivativeProp)

derivative1 = Derivative()
derivative1.display()

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name, self.age)

# child class
class Student(Person):
    def __init__(self, name, age, dob):
        self.sName = name
        self.sAge = age
        self.dob = dob
        super.__init__(name, age)
    def displayStudent(self):
        print(self.sName, self.sAge) 

student1 = Student('Nahid',24,'20-10-2024')
student1.display()

