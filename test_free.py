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
        return 'ToDo'
        
print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print('something')
print('something')
print('something')
