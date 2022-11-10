print('From Code Wars.')
print()

def title_case(title, minor_words=''):

    # This function capitalizes all words if not presents in 
    # the second argument, although the first word is always capitalized.
    if minor_words:
        words = [w.title() if w not in minor_words.lower().split() 
                 else w for w in title.lower().split()]
        words[0] = words[0].capitalize()
        return ' '.join(words)
    return title.title()

print(title_case('THE WIND IN THE WILLOWS', 'THE in'))
# Outputs - The Wind in the Willows
