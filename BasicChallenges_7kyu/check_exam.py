print('From Code Wars.')
print()

def check_exam(arr1, arr2):

    # This function checks an exam (arr1) with the student's answers (arr2),
    # and return the total points or 0 if the total is negative.
    return max(0, sum([0 if y == '' else 4 if x == y \
        else - 1 for x, y in zip(arr1, arr2)]))

print(check_exam(['a', 'a', 'c', 'b'], ['a', 'a', 'b',  '']))  # Outputs - 7
