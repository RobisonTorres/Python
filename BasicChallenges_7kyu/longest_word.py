print('From solo learn.')
print()

def longest_word(string):

    # This code returns the longest word in a text.
    string = string.split()
    return max(string, key=len)

print(longest_word('this is an awesome text '))  # Output - awesome
