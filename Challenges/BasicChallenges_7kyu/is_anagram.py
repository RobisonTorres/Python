print('From Code Wars')
print()

def is_anagram(test, original):

    # This function determines whether two words are anagram.
    # Anagram definition : a word, phrase, or name formed by rearranging\
    # the letters of another,\ such as cinema, formed from iceman.
    return sorted(test.lower()) == sorted(original.lower())

print(is_anagram('Buckethead', 'DeathCubeK'))  # Outputs - True.
print(is_anagram('dumble', 'bumble'))  # Outputs - False.
