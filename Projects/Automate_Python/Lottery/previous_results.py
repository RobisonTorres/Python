import googlesearch
import bs4
import requests
import re
import json

print('Gathering Previous Results.')
print()

def score():

    # This function retrieves twenty previous results from the 'lotofacil' lottery, 
    # either from a local JSON file or through web scraping.
    
    file = open('pre_results.json')
    round = int(input('Type in the last lottery round: '))
    print()
    results = json.load(file)
    
    for num in range((round - 19), round + 1):
        if str(num) in results.keys():
            # If the result for this round is already in the saved results, display it.
            print(f'Round: {num} - Result: {results[str(num)]}')

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
            
            # Store the result in the 'results' dictionary.
            results[num] = lottery_result
    
    # Save the updated results dictionary back to the JSON file for future use.
    with open('pre_results.json', 'w') as file:
        json.dump(results, file)
            
    return '\nResults have been saved.'

print(score())