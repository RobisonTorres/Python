import requests
import bs4
import re
import open_save

def web_search(round):

    # This function accesses the lottery's page and takes the html.
    url = f'https://www.intersena.com.br/lotofacil/resultados/{round}'
    source = requests.get(url).text
    soup = bs4.BeautifulSoup(source, 'html.parser')
    return soup

def extract_search(round=False):

    # This function extracts only the lottery result from the scraping,
    # gives it a proper format, and saves new results.
    previous_results = open_save.open_file()
    
    if not round:
        round = input('What round do you want to check: ')
        
    if str(round) in previous_results.keys():
        return [round, previous_results[str(round)]]
    
    target = web_search(round)
    round_found = target.find('h1', class_='col-md-6 col-sm-6 col-xs-12')
    numbers = target.find('div', class_='resultado-individual-sorteio')

    # Only numbers.
    nums = re.sub('[^0-9]', '', numbers.text)
    round_found = re.sub('[^0-9]', '', round_found.text)
      
    if round != round_found:
        return [round]

    else:
        lottery_result = '-'.join([nums[x:x+2] for x in range(0, len(nums), 2)])
        
        # Save.
        previous_results[round] = lottery_result
        previous_results = dict(sorted(previous_results.items(),key=lambda x:int(x[0])))
        open_save.save_file(previous_results)   
        return [round, lottery_result]
    
'''
Old version.

import googlesearch
import requests
import bs4
import re
print('Checking numbers.')
print()

def score(your_games):
    
    # This function checks the total score hit in each lottery ticket.
    round = input('What round do you want to check: ')
    
    # Taking the lottery result through web scraping.
    query = f"lotofacil {round} noticias.uol.com.br"
    url = googlesearch.search(query, tld="co.in", num=1, stop=1, pause=2)
    source = requests.get(*url).text
    soup = bs4.BeautifulSoup(source, 'html.parser')

    # Extracting only the lottery result from the scraping,
    # and giving it a proper format.
    lottery_result = re.findall(r'(?:(?:[0-9]{2}\s?\.?-?\s?){14}(?:[0-9]{2}){1})', soup.text)[0]
    lottery_result = lottery_result.replace(' ', '').replace('.', '-')
    print(f'\nResult - {round} : {lottery_result}\n')
    lottery_result = lottery_result.replace('-','')
    lottery_result = [int(lottery_result[x: x+2]) for x in range(0, len(lottery_result), 2)]   

    # Comparing the lottery's result with your games.
    result = []
    for num, game in enumerate(your_games, 1):
        result.append(str(num) + '° Game - Score: ' 
                               +  str(15 - len(set(lottery_result) - set(game))))
    return '\n'.join(result)

print(score([[1,4,5,6,8,10,11,13,15,16,17,18,20,22,25],
            []]))
'''
