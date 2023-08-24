print('From Code Wars.')
print()

def solution(s):

    # This function will break up camel casing, using a space between words.
    return ''.join([' ' + l if l.isupper() else l for l in s])

print(solution('helloWorld'))  # Outputs - hello World
