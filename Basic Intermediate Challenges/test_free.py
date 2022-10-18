print('Test Free - keep it clean')
print()

def count(string):
    
    # This function counts all the occurring characters in a string.
    string = ''.join(string.lower().split(' '))  # downloadmovies
    keys = ''.join(sorted(set(string)))  # adeilmnosvw
    occurrence = [string.count(l) for l in keys]  # [1, 2, 1, 1, 1, 1, 1, 3, 1, 1, 1]
    return dict(zip(keys, occurrence))

print(count('Download Movies'))
