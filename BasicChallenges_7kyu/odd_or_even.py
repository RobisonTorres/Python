print('From Code Wars')
print()

def odd_or_even(arr):

    # This function sums numbers of a list,
    # and determine whether it's even or odd.
    return 'even' if sum(arr) % 2 == 0 else 'odd'

print(odd_or_even([0, -1, -5]))  # Output - even.
