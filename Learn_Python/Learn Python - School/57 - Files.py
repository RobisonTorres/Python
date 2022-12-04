print('3W School.')
print()

'''
The key function for working with files in Python is the open() function.
The open() function takes two parameters; filename, and mode.
There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, 
error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
'''

# To open a file for reading it is enough to specify the name of the file:
my_file = open('57.1- requirements.txt')
print(my_file.read())

# By default the read() method returns the whole text,
# but you can also specify how many characters you want to return:
my_file = open('57.1- requirements.txt')
print(my_file.read(10))

# You can return one line by using the readline() method:
my_file = open('57.1- requirements.txt')
print(my_file.readline())

# It is a good practice to always close the file when you are done with it.
my_file.close()
