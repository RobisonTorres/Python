print('From Code Wars.')
print()

def comp(array1, array2):

    # This function compares two array and return if they are equals.
    try:
        return sorted([n**2 for n in array1]) == sorted(array2)
    except:
        return False

print(comp([121, 144, 19, 161, 19, 144, 19, 11],
           [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]))
# Outputs - True
