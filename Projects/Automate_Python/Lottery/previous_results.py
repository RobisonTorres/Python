import open_save
import googlesearch
import bs4
import requests
import re

print('Gathering Previous Results.')
print()

def score():

    # This function retrieves twenty previous results from the lottery, 
    # through web scraping or local file, and saves new results for future use.

    previous_results = open_save.open_file()
    round = int(input('Type in the last lottery round: '))
    
    for num in range((round - 19), round + 1):
        if str(num) in previous_results.keys():

            # If the result for this round is already in the saved results, display it.
            print(f'Round: {num} - Result: {previous_results[str(num)]}')

        else:

            # If the result is not saved, retrieve it through web scraping.
            query = f"lotofacil + {num} + noticias.uol.com.br"
            url = googlesearch.search(query, tld="co.in", num=1, stop=1, pause=2)
            source = requests.get(*url).text
            soup = bs4.BeautifulSoup(source, 'html.parser')
            
            # Extracting only the numbers from the scraped text.
            lottery_result = re.findall(r'(?:(?:[0-9]{2}\s?\.?-?\s?){14}(?:[0-9]{2}){1})', soup.text)[0]
            lottery_result = lottery_result.replace(' ', '').replace('.', '-')
            print(f'Round: {num} - Result: {lottery_result}')
            
            # Save new results.
            previous_results[num] = lottery_result
            open_save.save_file(previous_results)

    # Sorted the dictionary and save.
    previous_results = dict(sorted(previous_results.items(),key=lambda x:int(x[0])))
    open_save.save_file(previous_results)        

    return '\nNews results have been saved.'

print(score())
