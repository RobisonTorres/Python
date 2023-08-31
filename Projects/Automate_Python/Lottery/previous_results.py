import open_save
import web_scraper
print('Gathering Previous Results.')
print()

def score():

    # This function retrieves twenty previous results from the lottery, 
    # through web scraping or local file, and saves new results for future use.
    previous_results = open_save.open_file()
    round = int(input('Type in the lottery round: '))
    
    for num in range((round - 19), round + 1):
        if str(num) in previous_results.keys():
            # If the result for this round is already in the saved results, display it.
            print(f'Round: {num} - Result: {previous_results[str(num)]}')

        else:
            # If the result is not saved, retrieve it through web scraping.
            lottery_result = web_scraper.extract_search(num)
            print(f'Round: {num} - Result: {lottery_result[1]}') 

    return '\nNews results have been saved.'

print(score())
