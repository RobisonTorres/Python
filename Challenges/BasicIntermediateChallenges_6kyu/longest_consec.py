print('From Code Wars.')
print()

def longest_consec(strarr, k):

    # Your task is to return the first longest string consisting
    # of k consecutive strings taken in the array.
    m = 0
    new = []
    while m < len(strarr) - (k - 1):
        new.append(''.join(strarr[m:k + m]))
        m += 1
    return '' if strarr == [] or k > len(strarr) or k <= 0 else max(new, key=len)
print(longest_consec(['tree', 'foling', 'trashy', 'blue', 'abcdef', 'uvwxyz'], 2))
# Outputs - folingtrashy
print(longest_consec(['tree', 'foling', 'trashy', 'blue', 'abcdef', 'uvwxyz'], 3))
# Outputs - treefolingtrashy
