# Question: 
# 1. Write a python program to check a character whether it is present or not in a given string and if present, then calculate the percentage value of that character on the given string

givenString = 'Hajee Mohammad Danesh Science and Technology University'
charToCheck = 'a'

if (charToCheck in givenString):
    print(charToCheck, 'is present in',givenString)
    # calculate percentage 
    count = 0
    for c in givenString.lower():
        if (c == charToCheck.lower()):
            count += 1
    percentage = (count / len(givenString)) * 100
    print('total present', count)
    print('Percentage of', charToCheck, 'in ', givenString , 'is ', round(percentage,2),'%' )
else:
    print(charToCheck, 'is not in ', givenString)