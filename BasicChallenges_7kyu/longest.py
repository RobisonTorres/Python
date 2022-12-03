print('From Code Wars')
print()

def longest(a1, a2):

    # This function will combine two strings,\
    # remove duplicates letters, and put the result in alphabetical order.
    return ''.join(sorted(set((a1 + a2))))

print(longest('rob', 'torresrob'))  # Outputs - beorst
