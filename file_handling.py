# Opening a file 

# modes 
# r : only reading or read only
# w : open exising file for writing overrite data 
# a : append to exising file content 
# r+ : read and write exisitng file, does not overwrite
# w+ : 


# READ AND WRITE
# file = open('hello.txt','w')
# file.write('hi there')
# file.close()
# openFile = open('hello.txt','r')
# print('file content', openFile.read())

# APPEND TO EXISTING CONTETNT OF FILE
# file = open('hello.txt','a')
# file.write(' Hi!!!')
# file.close()
# openFile = open('hello.txt','r')
# print('file content',openFile.read())

# Open the file in 'r+' mode for reading and writing
# OPEN, READ OVERWRITE AND ADD NEW CONTENT 
# with open('hello.txt', 'r+') as file:
#     # Read the current content of the file
#     content = file.read()
#     print('Original file content:', content)
    
#     # Move the cursor to the end of the file to add more text
#     file.write('\nAdding some new text.')

#     # Move the cursor back to the beginning of the file
#     file.seek(0)
    
#     # Read the updated content
#     updated_content = file.read()
#     print('Updated file content:', updated_content)


# w+ mode 
# READ, WRITE BUT DOES NOT NEED EXSITING FILE

# Open the file in 'w+' mode for both writing and reading
# with open('hello2.txt', 'w+') as file:
#     # Write some text to the file
#     file.write("This is the first line.\n")
#     file.write("This is the second line.\n")

#     # Move the cursor back to the beginning of the file to read from it
#     file.seek(0)

#     # Read the content of the file
#     content = file.read()
#     print("File content after writing:")
#     print(content)

#     # Write more text to the file
#     file.write("This is an additional line.\n")

#     # Move the cursor back to the beginning again to read the updated content
#     file.seek(0)

#     # Read the updated content
#     updated_content = file.read()
#     print("File content after adding more text:")
#     print(updated_content)

# with open('hello')

# closing a file 
# file.close()