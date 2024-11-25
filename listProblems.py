numbers = [1, 2, 3,4 ,5, 123,454,12]
modifiedList = []
count = 0
for i in numbers:
    count = count + i

print('Ttotal is :', count)
numberToMultiply = 2
for j in numbers:
    tempNum = j * numberToMultiply
    modifiedList.append(tempNum)

print('Modified numbers', modifiedList)

#print largest number
largestNum = numbers[0]
for k in numbers:
    if(k > largestNum):
        largestNum = k

print('largest number', largestNum)

# print smallest number in list 
