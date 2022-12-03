print('From Code Wars')
print()

def is_isogram(string):

    # This function determines if a string is or not a isogram.
    return True if len(set(string.lower())) == len(list(string.lower()))\
        else False

print(is_isogram('moOse'))  # Outputs - False
print(is_isogram('isogram'))  # Outputs - True
'''
An isogram is a word that has no repeating letters, consecutive
or non-consecutive. Implement a function that determines whether 
a string that contains only letters is an isogram. Assume the empty 
string is an isogram. Ignore letter case.
'''
