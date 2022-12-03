print('Find the first non-consecutive number')
print()

def non_consecutive(arr):

    # This function finds the first non-consecutive number in a list.
    first = arr[0]
    for num in arr:
        if num != first:
            return num
        first += 1
    return None

print(non_consecutive([1, 2, 4]))  # Outputs - 4
