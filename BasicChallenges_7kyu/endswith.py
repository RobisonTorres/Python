print('From Code Wars')
print()

def solution(string, ending):

    # This function checks if the first argument ends with the second.
    return string.endswith(ending)
    # The endswith() method returns True if the string ends\
    # with the specified value, otherwise False.

print(solution('abcde', 'cde'))  # Outputs - True
print(solution('abcde', 'abc'))  # Outputs - False
