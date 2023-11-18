print('From Code Wars.')
print()

def score(dice):

    # This function...
    throws = ''.join(sorted(map(str, dice)))
    points = 0
    scores = {'111': 1000, '666': 600, '555': 500, '444': 400,
             '333': 300, '222': 200, '1': 100, '5': 50}

    for n in list(set(dice)):
        numbers = ''.join([m for m in throws if m == str(n)])
        while numbers:
            if numbers[:3] in scores:
                points += scores[numbers[:3]]
                numbers = numbers[3:]
            elif numbers[:1] in scores:
                points += scores[numbers[0]]
                numbers = numbers[1:]
            else:
                numbers = numbers[1:]
    return points

print(score([5, 1, 3, 4, 1]))
print(score([1, 1, 1, 3, 1]))
