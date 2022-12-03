print('From Code Wars.')
print()

def in_array(array1, array2):

    # This function verifies and return the elements
    # of array1 only if they are in array2.
    return sorted([a for a in set(array1) if a in ' '.join(array2)])

a1 = ['arp', 'live', 'strong', 'ect', 'ect']
a2 = ['lively', 'alive', 'harp', 'sharp', 'armstrong', 'ect']

print(in_array(a1, a2))  # Outputs - ['arp', 'ect', 'live', 'strong']
