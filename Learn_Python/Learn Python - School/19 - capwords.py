import string

print('Using Cap Words')
print()

sentence = 'Python is one of the best programming languages.'
jordan = 'How can mirrors be real if our eyes aren\'t real'

def cap_words(any_string):  # This function takes a string\
    # and capitalize every single word.
    return string.capwords(any_string)  # 'capwords' in this case \
    # is a method from library 'string'.

print(cap_words(sentence))
print(cap_words(jordan))
