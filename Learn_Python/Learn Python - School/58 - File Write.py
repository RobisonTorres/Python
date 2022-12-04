import os
print('3W School.')
print()

# To write to an existing file, you must add a
# parameter to the open() function:

# "a" - Append - will append to the end of the file.
# "w" - Write - will overwrite any existing content.
my_file = open('57.1- requirements.txt', 'a')
my_file.write('Now the file has more content.')
my_file.close()

# Verify the change.
my_file = open('57.1- requirements.txt')
print(my_file.read())

# Open the file "58.1 - test.txt" and overwrite the content:
my_file = open('58.1 - test.txt', 'w')
my_file.write('Now the file has a new content.')
my_file.close()

'''
Create a New File - To create a new file in Python,
use the open() method, with one of the following parameters:
"x" - Create - will create a file, returns an error if the file exist
"w" - Write - will create a file if the specified file does not exist
'''
# Create a file called "my_file.txt":
f1 = open("my_file1.txt", "x")

# Create a new file if it does not exist:
f2 = open("my_file2.txt", "w")

# Delete a File - To delete a file, you must import
# the OS module, and run its os.remove() function:
os.remove('my_file1.txt')
