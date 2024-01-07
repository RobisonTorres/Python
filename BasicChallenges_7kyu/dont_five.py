print('From Code Wars')
print()

def dont_give_me_five(start, end):

    # This function counts how many numbers are in a range without '5' in it.
    return len([num for num in range(start, end + 1) if '5' not in str(num)])

print(dont_give_me_five(4, 17))  # Output - 12
