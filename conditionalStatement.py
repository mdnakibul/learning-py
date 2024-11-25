# check number
i = 10
if(i < 15):
    print(i," is greater than 15")
else:
    print(i," is less than 15")

isItRaingin = True
if(isItRaingin):
    print("We should take an umbrella today")
else:
    print("We don't need to take an umbrella today")
print("I am not in if")

isPlaneTicketAvailable = True
if(isPlaneTicketAvailable):
    print('I will go to Dhaka by Plane')
else:
    print("I will go to Dhaka by Bus or Train")

# Nested if

studentMark = 50
passMark = 40
if(studentMark < passMark):
    print('Student Failed!')
else:
    print('Student passed!')
    if((studentMark >= 40) and (studentMark <= 45)):
        print('Your got C grade')

# tarnery operator

a = True
b = False
print('A is true') if a else print('B is true')