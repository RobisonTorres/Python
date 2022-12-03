print('From Code Wars.')
print()

def move_zeros(array):
    
    # This function takes all zeros within an array and put them in the end.
    nums = [n for n in array if n != 0]
    return nums + array.count(0) * [0]

print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
