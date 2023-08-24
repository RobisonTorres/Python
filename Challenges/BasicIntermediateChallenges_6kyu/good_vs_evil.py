print('From Code Wars.')
print()

def good_vs_evil(good, evil):

    # This function determines the battle result.
    good = sum([x * y for x, y in zip(list(map(int, good.split())), [1, 2, 3, 3, 4, 10])])
    evil = sum([x * y for x, y in zip(list(map(int, evil.split())), [1, 2, 2, 2, 3, 5, 10])])
    return 'Battle Result: ' + ('Good triumphs over Evil' if good > evil 
                 else 'Evil eradicates all trace of Good' if good < evil 
                 else 'No victor on this battle field')

print(good_vs_evil('0 0 0 0 0 0', '0 0 0 0 0 0 0'))  # Outputs - 'No victor on this battle field'
