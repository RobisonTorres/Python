print('From Code Wars.')
print()

def find_uniq(arr):

    # This function returns the unique different number in the array.
    new = list(set(arr))
    return min(new, key=arr.count)
    # return min(set(arr), key=arr.count) - Clever

print(find_uniq([1, 1, 2]))  # Outputs - 2
