print('From Code Wars.')
print()

def validBraces(s):

    # This function determines if the order of parentheses,
    # brackets and curly braces is valid.
    while '{}' in s or '()' in s or '[]' in s:
        s = s.replace('{}', '')
        s = s.replace('[]', '')
        s = s.replace('()', '')
    return s == ''

print(validBraces('()()'))
print(validBraces('[(])'))
