print('Single qotation string')
print("Double qotation 'string'")
string1 = 'PYTHON'
# accessing the string element 
print('First character of', string1, 'is:',string1[0])

# String slicing
print('First 4 character of',string1,string1[0:5])

# reversing a string 
print('Reverse of', string1, string1[::-1])

# reversing a part of string 
print('Reversing a part of', string1, string1[4:2:-1])

# replacing a part of string

helloString = 'Hello World'
indexToBeReplaced = 4
newCharToInsert = 'a'

listOfHelloStr = list(helloString)
listOfHelloStr[indexToBeReplaced] = newCharToInsert
print('Replaced', indexToBeReplaced,'index by "', newCharToInsert, '" is', ''.join(listOfHelloStr) )

# another method of replacing a part of string 
replaceIndex = 2
strPart1 = string1[0:2]
strPart2 = string1[replaceIndex + 1:]
print('Replaced string in another method:', strPart1 + newCharToInsert + strPart2)

# Deleting & updating a string 
print('Replacing "T" in string', string1, 'with "a"', string1.replace("T","a"))

# Deleting a string
# del string1
# print(string1)

# Check if a character exist or not 
if "T" in string1:
    print("T is present in", string1)

if 'o' not in 'PYTHON':
    print('o is not in PYTHON')

# capitalize a string 
strInSmall = 'hello, how are you? I am fine'
print('Capitalizing a string:',strInSmall.capitalize())

# uppercase a string 
print('Upper case a string:', strInSmall.upper())

# lowercase a string 
print('Lower case a string:', helloString.lower())