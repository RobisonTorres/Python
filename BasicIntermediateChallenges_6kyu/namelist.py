print('From Code Wars.')
print()

def namelist(names):

    # This function separates names in the list.
    n = [''.join(list(name.values())) for name in names]
    if len(n) >= 2:
        n = [''.join([n + ', ' for n in n[:-2]])\
                + n[-2] + ' & ' + n[-1]]
    return '' if not names else n[0]

print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))
# Outputs - Bart, Lisa & Maggie
print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}]))
# Outputs - Bart & Lisa
