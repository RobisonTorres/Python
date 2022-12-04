print('Working with reading files.')
print()

# Sending "r" means open in read mode, which is the default.
text = open('21 - text.txt', 'r')

# print(text.readable()) - To know if the file is readble.
print(text.read())
# .read shows all the information inside a file.

# .readline shows only one line at time.
print(len(text.readline()))  # Jim - Salesman
print(text.readline())  # Dwight - Salesman
print(text.readline())  # Pam - Receptionist



#.readlines put the information inside a list.
personal = text.readlines()
print(personal)


for people in text.readlines():
    print(people)

text.close()

with open('21 - text.txt', 'r') as f:
    print(f.read())
#  The file is automatically closed at the end of the with statement,\
#  even if exceptions occur within it.
