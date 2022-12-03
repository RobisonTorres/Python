print('From Code Wars.')
print()

def to_camel_case(text):

    # This function converts letter to capitalize
    # if dash or underscore is in the left side of it.
    c = text.replace('-', ' ').replace('_', ' ').split()
    return ''.join([w.capitalize() if w != c[0] else w for w in c])

print(to_camel_case('the-stealth_warrior'))  # Outputs - theStealthWarrior
