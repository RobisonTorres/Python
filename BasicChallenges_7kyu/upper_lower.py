print('From Code Wars')
print()

def solve(s):

    # This function converts the string to lower\
    # or upper case depend on the quantity.
    upper = len([l for l in s if l.isupper()])
    return s.upper() if upper > len(s) / 2 else s.lower()

print(solve('code'))  # Outputs - code
print(solve('CODe'))  # Outputs - CODE
print(solve('COde'))  # Outputs - code
