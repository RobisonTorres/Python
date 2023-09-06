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
