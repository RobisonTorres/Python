import web_scraper

def score(your_games):
    
    # This function checks the total score hit in each lottery ticket.
    lottery_result = web_scraper.extract_search()
    print(f'\nResult - {lottery_result[0]} : {lottery_result[1]}\n')
    lottery_result = lottery_result[1].replace('-','')
    lottery_result = [int(lottery_result[x: x+2]) for x in range(0, len(lottery_result), 2)]   

    # Comparing the lottery's result with your games.
    result = []
    for num, game in enumerate(your_games, 1):
        result.append(str(num) + '° Game - Score: ' 
                               +  str(15 - len(set(lottery_result) - set(game))))
    return '\n'.join(result)
