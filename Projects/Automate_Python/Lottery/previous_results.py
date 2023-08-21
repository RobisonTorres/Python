import googlesearch
import bs4
import requests
import re
print('Checking Previous Results.')
print()

def score():
    
    # This function returns ten previous results from the lottery - 'lotofacil'.
    round = int(input('Type in the last lottery round: '))
    print()
    results= []

    for num in range((round-9), round+1):

        query = f"lotofacil + {num} + noticias.uol.com.br"
        url = googlesearch.search(query, tld="co.in", num=1, stop=1, pause=2)
        source = requests.get(*url).text
        soup = bs4.BeautifulSoup(source, 'html.parser')

        # Extracting the lottery result from the scraping.
        lottery_result = re.findall(r'(?:(?:[0-9]{2}-?){15})', soup.text)[0]
        print(f'Round: {num} - Result: {[lottery_result]}')

        # Storing the results.
        results.append(lottery_result)

    print()

    # Getting the frequency of each number.
    frequency = []
    results = ''.join(results).replace('-', '')  
    lottery_result = [int(results[x: x+2]) for x in range(0, len(results), 2)]

    for num in range(1, 26):
        frequency.append(f'num {num}: {lottery_result.count(num)}')

    print('Frequency')    
    return frequency

print(score())
