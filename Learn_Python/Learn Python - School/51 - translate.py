print('Working with translate.')
print()

# The translate() method returns a string where some specified\
# characters are replaced with the character described in a dictionary,\
# or in a mapping table.
# Use the maketrans() method to create a mapping table.

# Use a mapping table to replace "S" with "P":

txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))  # Output - Hello Pam!
txt1 = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable1 = txt1.maketrans(x, y)
print(txt1.translate(mytable1))  # Output - Hi Joe!
