from bs4 import BeautifulSoup
from googlesearch import search
import requests
import re
print('Checking the numbers...')
print()

query = f"lotofacil + {input('round: ')} + uol.com.br"
url = search(query, tld="co.in", num=1, stop=1, pause=2)

source = requests.get(*url).text

soup = BeautifulSoup(source, 'html.parser')

numbers = re.findall(r'(?:(?:[0-9]{2}-?){15})', soup.text)[0].replace('-','')
print(numbers)
print()

def score(lottery_numbers, your_games):

    # This function checks the total score hit in each lottery ticket.
    lottery_numbers = [int(lottery_numbers[x: x+2]) for x in range(0, len(lottery_numbers), 2)]   
    result = []
    for num, game in enumerate(your_games, 1):
        result.append(str(num) + '° Game - Score: ' 
                               +  str(15 - len(set(lottery_numbers) - set(game))))
    return '\n'.join(result)

print(score(numbers, 
            [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
            [],
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
