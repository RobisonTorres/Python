import googlesearch
import requests
import bs4
import re
print('Checking numbers...')
print()

def score(your_games):
    
    # This function checks the total score hit in each lottery ticket.
    round = input('What round do you want to check: ')
    print()

    # Taking the lottery result through web scraping.
    query = f"lotofacil {round} noticias.uol.com.br"
    url = googlesearch.search(query, tld="co.in", num=1, stop=1, pause=2)
    source = requests.get(*url).text
    soup = bs4.BeautifulSoup(source, 'html.parser')

    # Extracting only the lottery result from the scraping,
    # and giving it a proper format.
    lottery_result = re.findall(r'(?:(?:[0-9]{2}\s?-?\s?){15})', soup.text)[0].replace(' ', '')
    print(f'Result - {round} : {lottery_result}')
    print()
    lottery_result = lottery_result.replace('-','')
    lottery_result = [int(lottery_result[x: x+2]) for x in range(0, len(lottery_result), 2)]   

    # Comparing the lottery's result with your games.
    result = []
    for num, game in enumerate(your_games, 1):
        result.append(str(num) + '° Game - Score: ' 
                               +  str(15 - len(set(lottery_result) - set(game))))
    return '\n'.join(result)

print(score([[2,4,8,9,10,11,12,14,17,18,19,20,21,22,25],
            [2,4,6,7,8,10,12,14,15,16,18,20,23,24,25],
            [1,4,6,7,9,10,11,12,15,16,18,19,20,21,23],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            []]))
