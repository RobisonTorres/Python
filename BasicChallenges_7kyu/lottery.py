from bs4 import BeautifulSoup
import requests
print('Checking number...')
print()

game = input('Please, type in the number of the round ')
print()
source = requests.get('https://www.google.com/search?q=lotofacil+'+game).text
soup = BeautifulSoup(source, 'html.parser')
numbers_result = soup.find('span', class_="FCUp0c rQMQod").text.replace('-','')
print(numbers_result)

def score(lottery_numbers, your_games):

    # This function checks the total score hit in each lottery ticket.
    lottery_numbers = [int(lottery_numbers[x: x+2]) for x in range(0, len(lottery_numbers), 2)]   
    result = []
    for num, game in enumerate(your_games, 1):
        result.append(str(num) + '° Game - Score: ' 
                               +  str(15 - len(set(lottery_numbers) - set(game))))
    return '\n'.join(result)

print(score(numbers_result, 
            [[1,3,5,6,8,10,11,13,15,16,17,19,20,21,24],
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
