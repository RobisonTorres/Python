print('Checking number...')
print()

def score(lottery_numbers, your_numbers):

    # This function checks the total score hit in each lottery ticket.
    result = [int(lottery_numbers[x: x+2]) for x in range(0, len(lottery_numbers), 2)]   
    return 15 - len(set(result) - set(your_numbers))
    
print(score('', 
            []))
