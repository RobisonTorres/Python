import numpy as np
import sys, subprocess
subprocess.run('cls', shell=True)
print('Test Free - keep it clear')
print()
# crt + D / alt + mouse / alt + up or down / shift + alt + up or down / crt + l

def find_missing(sequence):

    # This function...
    sequence = sorted(sequence)
    step1 = abs(sequence[1] - sequence[0])
    step2 = abs(sequence[2] - sequence[1])
    original = list(range(sequence[0], sequence[-1] + 1, min(step1, step2)))
    return list(set(original) - set(sequence))[0]

print(find_missing([-3, -29, -42, -55, -68, -81, -94, -107, -120])) # -16
print(find_missing([17, -27, -49, -71, -93, -115, -137, -159, -181])) # -5
