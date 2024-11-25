# there are two type of function
# 1. library function
# 2. User defined function
import math
print('Square root of 25 is', math.sqrt(25))

# def function_name(parameters):
# statements 
# return expresssion 

def addTwoNumber(a,b):
    return a + b
print('Sum of two number:', addTwoNumber(5,10))

# return of a function can be stored in a variable 

number1 = float(input('Enter a number of for square root:'))
sqrtOfNum = math.sqrt(number1)
print('Square root of',number1 ,'is', sqrtOfNum)

def sqroot(n):
    sqr = math.sqrt(n)
    print(sqr)

sqroot(number1)
