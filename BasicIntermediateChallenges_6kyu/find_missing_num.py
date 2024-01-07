print('From Code Wars.')
print()

def find_missing(sequence):

    # Given any Arithmetic Progression, this function finds the missing number.
    sequence = sorted(sequence)
    step1 = abs(sequence[1] - sequence[0])
    step2 = abs(sequence[2] - sequence[1])
    original = list(range(sequence[0], sequence[-1] + 1, min(step1, step2)))
    return list(set(original) - set(sequence))[0]
    # return (sequence[-1] + sequence[0]) * (len(sequence) + 1) / 2 - sum(sequence) - clever.

print(find_missing([-3, -29, -42, -55, -68, -81, -94, -107, -120])) # Outputs - -16
