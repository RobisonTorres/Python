import sys, subprocess
subprocess.run('cls', shell=True)
print('Test Free')
print()
# crt + D / alt + mouse / alt + up or down / shift + alt + up or down / crt + l
# crt + N .. crt + k, m .. crt + s

def max_sequence(arr):

    if arr == [] or all(n < 0 for n in arr):
        return 0

    elif all(n >= 0 for n in arr):
        return sum(arr)

    else:
            
        new_arr = [sum(arr[:x]) + arr[x] for x in range(0, len(arr))]
        if all(n >= 0 for n in new_arr):
            return sum(arr)
            
        else:
            positive = [n for n in new_arr if n >= 0]
            min_n = new_arr.index(min(positive))
            max_n = new_arr.index(max(positive))
            return new_arr

print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Outputs - 6 -  [4, -1, 2, 1]
print(max_sequence([-2, -1, -3, 4, -1, 2, 1, -5, 4]))
