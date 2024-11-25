user_input = input('Please enter a sentence: ')
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0

for vowel in vowels:
    tempCount = user_input.lower().count(vowel)  
    count += tempCount

print('Total vowels:', count)
