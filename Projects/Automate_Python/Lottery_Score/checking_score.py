import web_scraper, autocheck_score

def score(your_games, round=False):
    
    # This function checks the total score hit in each lottery ticket.
    lottery_result = web_scraper.extract_search(round)
    if type(lottery_result) == str:
        return lottery_result

    else:
        numbers_result = lottery_result[0]            
        round = lottery_result[1]
        print(f'\nRound: {round} - Result: {("-".join(map(str, numbers_result)))}\n')

        # Comparing the lottery's result with your games.
        score_result = []
        for num, game in enumerate(your_games, 1):
            score_result.append(str(num) + '° Game - Score: ' 
                                   +  str(15 - len(set(numbers_result) - set(game))))
        return '\n'.join(score_result)

if __name__ == "__main__":
   
    print('Checking Score.')
    print()
    print(score([[1,3,5,6,7,9,11,12,15,16,18,20,21,22,24],
        [1,3,6,8,10,11,12,13,15,17,19,20,21,23,24],
        [1,3,5,6,8,10,11,12,14,16,18,20,21,23,25],
        [],
        [],
        []]))
    
    compare = input('\nType \'y\' to compare this result with auto check: ')
    if compare == 'y': 
        
        print(autocheck_score.auto_check())