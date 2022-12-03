print('From Code Wars.')
print()

def accum(s):

    # This function takes a group of letters, capitalize each one\
    # and multiple them for their position with dash separating them.
    x = 1
    a = []
    for letter in s:
        a.append((letter * x).capitalize())
        x += 1
    return '-'.join(a)

print(accum('HbideVbxncC'))
# H-Bb-Iii-Dddd-Eeeee-Vvvvvv-Bbbbbbb-Xxxxxxxx-Nnnnnnnnn-Cccccccccc-Ccccccccccc
