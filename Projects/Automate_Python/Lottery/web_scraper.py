import googlesearch
import requests
import bs4
import re
import open_save

def web_search(round):

    # This function...
    query = f"lotofacil {round} noticias.uol.com.br"
    url = googlesearch.search(query, tld="co.in", num=1, stop=1, pause=2)
    source = requests.get(*url).text
    soup = bs4.BeautifulSoup(source, 'html.parser')
    return soup

def extract_search(round=False):

    # This function...
    previous_results = open_save.open_file()
    if not round:
         round = input('What round do you want to check: ')
    
    target = web_search(round)

    # Extracting only the lottery result from the scraping,
    # and giving it a proper format.
    lottery_result = re.findall(r'(?:(?:[0-9]{2}\s?\.?-?\s?){14}(?:[0-9]{2}){1})', target.text)[0]
    lottery_result = lottery_result.replace(' ', '').replace('.', '-')

    previous_results[round] = lottery_result
    previous_results = dict(sorted(previous_results.items(),key=lambda x:int(x[0])))
    open_save.save_file(previous_results)   
    return [round ,lottery_result]
