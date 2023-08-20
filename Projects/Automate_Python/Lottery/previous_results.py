import googlesearch
import bs4
import requests
import re
print('Checking previous results...')
print()

def score():
    
    # This function checks five last results.
    round = int(input('Type in the last lottery round: '))
    print()
    results = []

    for num in range((round-4), round+1):

        query = f"lotofacil + {num} + noticias.uol.com.br"
        url = googlesearch.search(query, tld="co.in", num=1, stop=1, pause=2)

        source = requests.get(*url).text
        soup = bs4.BeautifulSoup(source, 'html.parser')

        # Extracting the lottery result from the scraping.
        lottery_result = re.findall(r'(?:(?:[0-9]{2}-?){15})', soup.text)[0]

        # Storing the results.
        results.append(f'Round: {num} - Result: {[lottery_result]}')

    return '\n\n'.join(results)

print(score())
print()
