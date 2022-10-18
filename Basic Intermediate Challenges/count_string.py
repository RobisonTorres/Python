print('From Code Wars.')
print()

def count(string):
    
    # This function counts all the occurring characters in a string.
    string = ''.join(string.lower().split(' '))
    keys = ''.join(sorted(set(string)))
    occurrence = [string.count(l) for l in keys]
    return dict(zip(keys, occurrence))

print(count('Download Movies'))
