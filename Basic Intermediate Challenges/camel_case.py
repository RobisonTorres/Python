print('From Code Wars.')
print()

def camel_case(string):
    
    # All words must have their first letter capitalized without spaces.
    return ''.join([word.capitalize() for word in string.split()])
    # return string.title().replace(" ", "") - Clever.

print(camel_case('hello case'))  # Outputs - HelloCase
