import requests
import bs4
import re
import open_save

def web_search(round):

    # This function accesses the lottery page and takes the result.
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

    try:
        target = web_search(round)
        numbers = target.find('div', class_='resultado-individual-sorteio')

        # Only numbers.
        nums = re.sub(r'[\n\s]', '', numbers.text)
        lottery_result = '-'.join([nums[x:x+2] for x in range(0, len(nums), 2)])

        # Save.
        previous_results[round] = lottery_result
        previous_results = dict(sorted(previous_results.items(),key=lambda x:int(x[0])))
        open_save.save_file(previous_results)   
        return [round ,lottery_result]

    except:
        return 'Something went wrong, please try again.'
