print('Checking number...')
print()

def score(lottery_numbers, your_games):

    # This function checks the total score hit in each lottery ticket.
    lottery_numbers = [int(lottery_numbers[x: x+2]) for x in range(0, len(lottery_numbers), 2)]   
    result = []
    for num, game in enumerate(your_games, 1):
        result.append(str(num) + '° Game - Score: ' 
                               +  str(15 - len(set(lottery_numbers) - set(game))))
    return '\n'.join(result)
    
print(score('', 
            [[],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            []]))
