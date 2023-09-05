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

    # This function extracts only the lottery result from the scraping,
    # gives it a proper format, and saves new results.
    if not round:
        round = input('What round do you want to check: ')

    try:
        target = web_search(round)
        numbers = target.find('div', class_='resultado-individual-sorteio')

        # Only numbers.
        nums = re.sub(r'[\n\s]', '', numbers.text)
        lottery_result = '-'.join([nums[x:x+2] for x in range(0, len(nums), 2)])

        return [round ,lottery_result]

    except:
        return 'Something went wrong, please try again.'
