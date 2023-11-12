print('From Code Wars')
print()

def is_sorted_and_how(arr):
    
    # This function determines if a list is or not sorted, if yes it shows how.
    if arr == sorted(arr):
        return 'yes, ascending'
    elif arr == sorted(arr)[::-1]:
        return 'yes, descending'
    else:
        return 'no'
    # return 'yes, ascending' if sorted(arr) == arr else 'yes, descending' if sorted(arr)[::-1] == arr else 'no'

print(is_sorted_and_how([15, 7, 3, -8]))  # Outputs - yes, descending