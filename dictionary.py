car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964,
"year": 2020
}
print('car dictionary', car)
print('car dictionary length', len(car))

# dictionar constructor
people = dict(name = "John", age = 36, country = "Norway")
print('constructed dictionary', people)

# access dictionary items 
print('access dictionary', car["model"])
print('access dictionary with get()', car.get('brand'))

print('get keys', car.keys())
print('get items', car.items())

# check if exist 
if "model" in car:
    print("Yes, 'model' is one of the keys in the car dictionary")

# change values 
car["year"] = 2018
car.update({"color": "red"})
print('dicationary with changed values', car)

# remove dictionary items 
# del car["model"]
# car.clear()
# print('Removed dictionary items', car)

# loop throgh dictionary
for x in car:
    print('dictionary loop', x)

for x in car.keys():
    print('dictionary key loop',x)

for x in car.values():
    print('dictionary values loop',x)

for x, y in car.items():
    print('dictionary item loop',x, y)


# mydict = car.copy()
mydict = dict(car)
print('copied dictionary', mydict)

keys = ['a','b','c','d','e']
values = [1,2,3,4,5]
# but this line shows dict comprehension here
myDict = { k:v for (k,v) in zip(keys, values)}
# We can also use myDict = dict(zip(keys, values))
print ('dictionary comprehenstion', myDict)

# Problem 1:
# Create a dictionary representing information about yourself, including
# your name, age, and favorite hobby. Print the dictionary.
# Problem 2:
# Create a dictionary of fruits with their quantities. Remove one fruit
# from the dictionary and print the updated dictionary.

myInfo = {
    'name':'Nahid',
    'age':24,
    'hobby':'coding'
}

print('my info dictionary', myInfo)

fruits = {
    'apple':2,
    'cherry':5,
    'banana':10
}
del fruits['banana']
print('Fruits dictionary after removal of 2nd item', fruits)