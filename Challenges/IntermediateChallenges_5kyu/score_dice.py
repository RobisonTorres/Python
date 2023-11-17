print('From Code Wars.')
print()

def score(dice):

    # This function...
    dice = ''.join(sorted(map(str, dice)))
    points = 0
    scores = {'111': 1000, '666': 600, '555': 500, '444': 400,
             '333': 300, '222': 200, '1': 100, '5': 50}
    score = []
    for n in range(1, 7):
        if str(n) in dice:
            if str(n) == '1' or str(n) == '5':
                numbers = ''.join([m for m in dice if m == str(n)])
                if len(numbers) == 5:
                    score.append(numbers[:3])
                    score.append(numbers[3])
                    score.append(numbers[4])
                elif len(numbers) == 4:
                    score.append(numbers[:3])
                    score.append(numbers[3])
                elif len(numbers) == 3 or len(numbers) == 1:
                    score.append(numbers)
                elif len(numbers) == 2:
                    score.append(numbers[0])
                    score.append(numbers[1])
            else:    
                score.append(''.join([m for m in dice if m == str(n)][:3]))

    for n in score:
        if n in scores.keys():
            points += scores[n]

    return points

print(score([5, 1, 3, 4, 1]))
print(score([1, 1, 1, 3, 1]))
