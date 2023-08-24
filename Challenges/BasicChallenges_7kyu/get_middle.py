print('From Code Wars')
print()

def get_middle(s):

    # This function returns two middle characters of a string
    # if the length is even, and only one middle character if
    # the string length is odd.
    a = int(len(s) / 2)
    return s[a - 1] + s[a] if len(s) % 2 == 0 else s[a]

print(get_middle('Toll'))  # Outputs - ol
