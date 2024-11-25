firstTuple = (1,2,3)
statusTuple = ('active', 'inactive')

print('Tuples', firstTuple, statusTuple)
print('length of first tuple', len(firstTuple))

tupleWithDuplicate = ('apple', 'cherry', 'banana', 'cherry')
print('duplicate tuple', tupleWithDuplicate, len(tupleWithDuplicate))

# Tuple constructor
constructedTuple = tuple(('hello','world'))
print('constructed tuple', constructedTuple)

# single item tuple 
singleElemTuple = tuple("apple",)
print('Single element tuple', singleElemTuple)

# access tuple items 
fruits = ("apple", 'banana', 'orange','apple','cherry')
print('first item of fruits', fruits[0]) #indexing same as list

# Change Tuple value 
xfruits = ("Apple", "Banana", "Cherry")
xFruitList = list(xfruits)
xFruitList[0] = 'cherry'
xfruits = tuple(xFruitList)
print('changed tuple', xfruits)

# add items to tuple 
xFruitList2 = list(xfruits)
xFruitList2.append('kiwi')
print('item added to tuple', tuple(xFruitList2))

# Merge 2 tuples 
tupleToMerge = ("Lichee",)
xfruits += tupleToMerge  # This is valid
print('merged tuple', xfruits)  # Printing the merged tuple


# loop throgh tuple 
# for fruit in xfruits:
#     print(fruit)

# for l in range(0, len(xfruits)):
#     print(xfruits[l])

fruitLength = len(xfruits)
index = 0
while(index < fruitLength):
    print(xfruits[index])
    index += 1

# Join two tuple 

print('joined tuple', xfruits + statusTuple)

#multiply items in tuple
print('Multiply tuple items', xfruits * 2)

# Methods of tuple 
# only 2 methods of tuple count() and index()
print('Tuple count',fruits.count("apple"))
print('Tuple index method', fruits.index('cherry'))

# Problem 1
height = 172
weight = 67
age = 24
bodyTuple = (height, weight, age)
print('body tuple: ', bodyTuple)

# problem 2 
numbersToTen = (1,2,3,4,5,6,7,8,9,10)
numbersToTenList = list(numbersToTen)
print('Slice of tuple', numbersToTenList[3:7])