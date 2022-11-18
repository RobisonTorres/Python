print('From Code Wars')
print()

def filter_list(l):

    # This function removes strings from a list with strings and integers.
    return [num for num in l if type(num) != str]

print(filter_list([1, 2, 3, 'a', 'kajdçlkjfa']))  # Outputs - [1, 2, 3]
