# filePath = '../tryJS/Hello world.txt'
# with open('../tryJS/Hello world.txt','r+') as file:
#     fileContent = file.read()
#     print('initital file content', fileContent)
#     file.seek(0)
#     file.writelines('Hello World! \n Python is awesome!\n')
#     file.truncate()
#     file.seek(0)
#     newFileContent = file.read()
#     print('New file content:\n', newFileContent)

# file = open('D:/tryJS/Hello World.txt','r')
# print(file.read())
# file.close()

file = open('python_file.txt', 'r')
print(file.read())