# Variable scope is 2 type 
# 1. global - Is accessible from anywhere of the program
# 2. local - Accessible within the scope
import math
from math import sqrt
globalVar = "I am global"
def function():
    localVar = 'I am a student'
    print(localVar)
    print(globalVar)

function()
print(globalVar)

print('Square root of 25:', math.sqrt(25))
print('Square root of 144:', sqrt(144))