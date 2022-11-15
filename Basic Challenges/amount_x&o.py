print('From Code Wars')
print()

def xo(s):

    # This function checks whether a string has the same amount of 'x' and 'o's.
    s = s.lower()
    return s.count('x') == s.count('o')

print(xo('Xo'))  # Outputs - True
