print('From Code Wars.')
print()

def find_outlier(integers):

    # This function finds and return the only\
    # odd or even number present in an array.
    return min([num for num in integers if num % 2 == 0],
               [num for num in integers if num % 2 != 0], key=len)[0]

print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))  # Outputs - 160
print(find_outlier([2, 4, 6, 8, 10, -1]))  # Outputs - -1
