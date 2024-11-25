# identify odd or event
def oddEvent(number = 2):
    if(number % 2 == 0):
        print(number,'is even')
    else:
        print(number,'is odd')

oddEvent(5)

def information(name, age,):
    print('Name is', name)
    print('Age is', age)

information('Anik', 35)
information(age = 25, name='Anik') #keyword argument

# Rest parameter 
def restInformation(*argv):
    for info in argv:
        print(info)

restInformation('Welcome', 'to', 'HSTU')

# lambda function \

def lambda_func(a,b):
    c = a + b
    return c
sum = lambda_func(2,3)
print('sum:', sum)

lambda_func_2 = lambda a, b: a+b
print('lambda sum:', lambda_func_2(4,5))