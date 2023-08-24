print('From Code Wars.')
print()

def valid_parentheses(string):
   
    # This function checks if a string has a valid parentheses.
    string = ''.join([l for l in string if l in('()')])
    while '()' in string:
        string = string.replace("()", '')
    return string == ''

print(valid_parentheses("Hello(World)"))  # Outputs - True
print(valid_parentheses("(()))"))  # Outputs - False
