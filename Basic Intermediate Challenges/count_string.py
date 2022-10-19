print('From Code Wars.')
print()

def count(string):
    
    # This function counts all the occurring characters in a string.
    string = string.replace(' ', '')
    occurrence = [string.count(l) for l in string]
    return dict(zip(string, occurrence))
    ''' - Clever
    from collections import Counter
    def count(string):
        return Counter(string)
    ''' 

print(count('Download'))  # {'D': 1, 'o': 2, 'w': 1, 'n': 1, 'l': 1, 'a': 1, 'd': 1}
