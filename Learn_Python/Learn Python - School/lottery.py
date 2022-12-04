print('Checking number...')
print()

def score(game, result):

    # This function checks the total score in each game.
    return 15 - len(set(result) - set(game))

print(score([3,5,6,7,9,10,13,15,16,18,20,21,22,24,25], 
            [3,6,7,8,9,11,12,13,15,16,18,19,20,21,25]))
