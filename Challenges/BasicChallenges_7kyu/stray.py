print('From Code Wars')
print()

def stray(arr):

    # This function returns the single different number.
    new = list(set(arr))
    return new[0] if arr.count(new[0]) < arr.count(new[1]) else new[1]
    # return min(arr, key=arr.count) - Clever.

print(stray([1, 1, 2]))  # Outputs - 2
print(stray([17, 17, 3, 17, 17, 17, 17]))  # Outputs - 3
