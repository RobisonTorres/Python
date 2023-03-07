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
    
print(score('010305070809101112151617212223', 
            [[1,4,5,6,8,10,11,13,15,16,17,18,20,22,25],
            [1,3,5,6,8,10,11,12,14,16,17,20,21,23,25],
            [1,3,5,6,8,9,10,11,13,15,16,18,20,21,24],
            [2,4,5,6,7,10,11,13,15,16,18,19,20,22,24],
            [2,3,5,6,7,8,10,11,13,15,17,19,21,22,25],
            [1,2,3,5,6,8,10,11,12,14,17,20,21,23,25]]))
