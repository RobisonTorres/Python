print('From Code Wars.')
print()

def sort_array(source_array):

    # This function takes an array, puts odd numbers in sequence
    # while letting even numbers in the same position.
    new = []
    odd = sorted([n for n in source_array if n % 2 != 0])[::-1]
    even = [n for n in source_array if n not in odd][::-1]
    [new.append(odd.pop()) if n % 2 != 0 else
     new.append(even.pop()) for n in source_array]
    return new

print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
# Outputs - [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
