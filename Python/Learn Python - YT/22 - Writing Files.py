print('Working with Writing Files.')
print()

# Sending "a" means append mode, for adding new content to the end of the file.
text = open('21 - text.txt', 'a')
text.write('\nJohn - Service')

text.close()

'''
# Sending "w" means write mode, for rewriting the contents of a file.
text1 = open('22 - text.txt', 'w')
text1.write('Rob - I.T')

text1.close()
'''

text2 = open('22 - text1.txt', 'w')
text2.write('Jim - Salesman\
            Dwight - Salesman\
            Pam - Receptionist\
             Michael - Manager')

text2.close()

'''
# The "w" mode will create a file, if it does not already exist.
test = open('22 - test.txt', 'w')
test.write('Rob - I.T')

test.close()
'''
'''
# The "w" mode will create a file, if it does not already exist.
test = open('22 - book.txt', 'w')
test.write('Some book')
test.write('Some book')
test.write('Harry Potter')
test.close()
'''

books = open('22 - book.txt', 'w')
books.write('Some Book\nAnother book\nHarry Potter')
books.close()
