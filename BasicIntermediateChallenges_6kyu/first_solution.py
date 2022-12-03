print('From Code Wars.')
print()

def solution(s):

    # This function splits a string into pairs of two characters.
    s = list(s + '_')[::-1]
    new = []
    while len(s) > 1:
        new.append(s.pop() + s.pop())
    return new

print(solution('abc'))  # Outputs - ['ab', 'c_']
