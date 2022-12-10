print('Convert list to string.')
print()

sentence = ['How', 'can', 'mirrors', 'be', 'real', 'if', 'our', 'eyes', "aren't", 'real']

def list_to_string(list):
    string = '-'  # First of all you need to create a string \
    # and the value attribute to it will be the separator.
    return string.join(list)

print(list_to_string(sentence))
