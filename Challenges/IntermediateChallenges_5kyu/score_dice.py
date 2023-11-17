print('From Code Wars.')
print()

def score(dice):

    # This function...
    dice = ''.join(sorted(map(str, dice)))
    points = 0
    scores = {'111': 1000, '666': 600, '555': 500, '444': 400,
             '333': 300, '222': 200, '1': 100, '5': 50}

    for n in range(1, 7):
        if str(n) in dice:
            if str(n) == '1' or str(n) == '5':
                numbers = ''.join([m for m in dice if m == str(n)])
                if len(numbers) == 5:
                    points += scores[numbers[:3]]
                    points += scores[numbers[3]]
                    points += scores[numbers[4]]
                elif len(numbers) == 4:
                    points += scores[numbers[:3]]
                    points += scores[numbers[3]]
                elif len(numbers) == 3 or len(numbers) == 1:
                    points += scores[numbers]
                elif len(numbers) == 2:
                    points += scores[numbers[0]]
                    points += scores[numbers[1]]
            else:
                numbers = ''.join([m for m in dice if m == str(n)][:3])
                if numbers in scores:
                    points += scores[numbers]
    return points

print(score([5, 1, 3, 4, 1]))
print(score([1, 1, 1, 3, 1]))
