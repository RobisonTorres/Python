print('From Code Wars.')
print()

def sort_array(a):

    # This function takes an array, put odd numbers in ascending order
    # and even numbers in descending order.
    new = []
    odd = sorted([n for n in a if n % 2 != 0])[::-1]
    even = sorted([n for n in a if n not in odd])
    [new.append(odd.pop()) if n % 2 != 0 else
     new.append(even.pop()) for n in a]
    return new

print(sort_array([5, 3, 2, 8, 1, 4]))  # Outputs - [1, 3, 8, 4, 5, 2]
