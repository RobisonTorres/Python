from bs4 import BeautifulSoup
from googlesearch import search
import requests
import re
print('Checking numbers...')
print()

def score(your_games):
    
    # This function checks the total score hit in each lottery ticket.

    # Taking the lottery result from web scraping.
    query = f"lotofacil + \
            {input('What round do you want to check: ')} + noticias.uol.com.br"
    print()
    url = search(query, tld="co.in", num=1, stop=1, pause=2)
    source = requests.get(*url).text
    soup = BeautifulSoup(source, 'html.parser')

    # Extracting only the lottery result from the scraping,
    # and giving it the proper format.
    lottery_result = re.findall(r'(?:(?:[0-9]{2}-?){15})', soup.text)[0].replace('-','')
    lottery_result = [int(lottery_result[x: x+2]) for x in range(0, len(lottery_result), 2)]   

    # Comparing the lottery's result with your games.
    result = []
    for num, game in enumerate(your_games, 1):
        result.append(str(num) + '° Game - Score: ' 
                               +  str(15 - len(set(lottery_result) - set(game))))
    return '\n'.join(result)

print(score([[2,4,8,9,10,11,12,14,17,18,19,20,21,22,25],
            [2,4,6,7,8,10,12,14,15,16,18,20,23,24,25],
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
