print('From Code Wars.')
print()

def generate_hashtag(s):

    # Task - The marketing team is spending way too much time typing in hashtags.
    # Let's help them with our own Hashtag Generator!
    phrase = '#' + ''.join(map(lambda x : x.capitalize(), s.split()))
    return False if s == '' or len(s) > 140 else phrase

print(generate_hashtag('Codewars is nice'))  # Outputs -  #CodewarsIsNice
