print('Checking number...')
print()

def score(game, result):

    # This function checks the total score in each game.
    return 15 - len(set(result) - set(game))

print(score([numbers],
            [result]))
