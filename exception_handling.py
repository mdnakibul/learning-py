# There are two type of error:
# 1. Syntax error - where we miss any rule
# 2. Exception

# i. SyntaxError
# ii. TypeError - Different type mixing
# iii. NameError - Access something that does not exis
# iv. IndexError - Accessing non-exising error
# v. KeyError - Accessing non existing key of dictionary
# vi. AttributeError - non existing method of a class
# vii. ValueError  - Converting to a data to another type that is not possible
# viii. I/O Error - can't read or write something
# ix. ZeroDivisionError - dividing something with 0
# x. ImportError - Can't import something

# HANDLING EXCEPTIONS 
a = [1,2,3]
try:
    print('hello world')
    print('Fourht element',a[3])
except:
    print('failed to print')

raise TypeError("Hudai")