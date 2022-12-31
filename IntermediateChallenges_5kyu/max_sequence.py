print('From Code Wars.')
print()

def max_sequence(arr):

    # Task - The maximum sum sub array problem consists in finding the maximum 
    # sum of a contiguous subsequence in an array or list of integers.
    try:
        max_sum = [max(0, arr[0])]
        for n in range(1, len(arr)):
            max_sum.append(max(0, arr[n] + max_sum[-1]))
        return max(max_sum)
    except: return 0

print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  
# [4, -1, 2, 1] - Outputs - 6
