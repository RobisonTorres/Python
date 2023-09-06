import requests
import bs4
import re

def web_search(round):

    # This function accesses the lottery's page and takes the html.
    url = f'https://www.intersena.com.br/lotofacil/resultados/{round}'
    source = requests.get(url).text
    soup = bs4.BeautifulSoup(source, 'html.parser')
    return soup

def extract_search(round=False):

    # This function extracts only the lottery result from 
    # the scraping and gives a proper format.   
    if not round: round = input('What round do you want to check: ')
    
    target = web_search(round)
    round_found = target.find('h1', class_='col-md-6 col-sm-6 col-xs-12')  
    numbers = target.find('div', class_='resultado-individual-sorteio')  
    
    # Only numbers.
    round_found = re.sub('[^0-9]', '', round_found.text)
    numbers = re.sub('[^0-9]', '', numbers.text)
      
    if round != round_found:  
        return f'\nRound: {round} - Result not found.\n'

    else:
        lottery_result = '-'.join([numbers[x:x+2] for x in range(0, len(numbers), 2)])
        return [round, lottery_result]
