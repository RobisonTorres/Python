print('From Code Wars.')
print()

def score(dice):

    # This function calculates the total score in the Greed game.
    throws = ''.join(sorted(map(str, dice)))
    points = 0
    scores = {'111': 1000, '666': 600, '555': 500, '444': 400, 
              '333': 300, '222': 200, '1': 100, '5': 50}
    
    for n in set(dice):
        numbers = ''.join([m for m in throws if m == str(n)])
        while numbers:
            for n in [3, 1, 1]:
                if numbers[:n] in scores:
                    points += scores[numbers[:n]]
                    numbers = numbers[n:]
            numbers = numbers[1:]            
    return points

print(score([5, 1, 3, 4, 1]))  # Outputs - 250 points