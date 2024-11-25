# List 
# What is list?
# Lists are used to store multiple element in a single variable
# List items are ordered, changable, and allow duplicate values
# It can contain any type of data 
fruites = ['apple', 'banana', 'cherry', 'orange']
print('Lenght of fruits list is: ', len(fruites), fruites)

mixedList = [1,'string', True,'string 2', False]
print(mixedList)

constructedList = list(('hello', 'world'))
print(constructedList)
print('First item of fruits is:', fruites[0])

print('Range in fruits',fruites[0:2])
print('second range',fruites[0:])

# check if an element exist in the list 
if 'apple' in fruites:
    print('apple is present in fruits')
else:
    print('apple is not in the fruits')

# for fruit in fruites:
#     print(fruite)

# changing an item of list 
fruites [1] = 'kiwi'
print(fruites)
fruites.insert(3,'avocado')
fruites.append('banana')
fruites.extend(mixedList)
fruites.remove('banana')
fruites.pop()
fruites.clear()
print(fruites)