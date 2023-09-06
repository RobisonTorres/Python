import web_scraper

def score(your_games):
    
    # This function checks the total score hit in each lottery ticket.
    lottery_result = web_scraper.extract_search()
    if len(lottery_result) == 1:
        return f'Round: {lottery_result[0]} - Result not found.'
    
    else:            
        print(f'\nResult - {lottery_result[0]} : {lottery_result[1]}\n')
        lottery_result = lottery_result[1].replace('-','')
        lottery_result = [int(lottery_result[x: x+2]) for x in range(0, len(lottery_result), 2)]   

        # Comparing the lottery's result with your games.
        result = []
        for num, game in enumerate(your_games, 1):
            result.append(str(num) + '° Game - Score: ' 
                                   +  str(15 - len(set(lottery_result) - set(game))))
        return '\n'.join(result)

if __name__ == "__main__":
    
    print('Checking Score.')
    print()
    print(score([[1,4,5,6,8,10,11,13,15,16,17,18,20,22,25],
            [1,3,5,6,8,10,11,12,14,16,17,20,21,23,25],
            [1,3,5,6,8,9,10,11,13,15,16,18,20,21,24],
            [1,3,5,6,8,10,11,13,15,16,18,20,21,22,24],
            [1,3,5,6,8,10,11,13,15,16,18,20,21,23,25],
            [1,3,5,6,8,10,11,13,15,16,17,19,21,23,25],
            [2,4,5,6,7,10,11,13,15,16,18,19,20,22,24],
            [2,3,5,6,7,8,10,11,13,15,17,19,21,22,25],
            [1,2,3,4,5,6,8,10,11,12,14,17,20,23,25],
            [1,3,5,6,8,10,11,13,15,16,17,19,20,21,24],
            [1,3,5,6,8,10,11,13,15,16,17,19,21,22,24],
            [1,2,4,5,6,8,10,11,13,15,16,18,20,21,23]]))
