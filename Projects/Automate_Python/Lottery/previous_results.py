import googlesearch
import bs4
import requests
import re
print('Checking Previous Results.')
print()

def score():
    
    # This function returns twenty previous results from the 'lotofacil' lottery, 
    # the frequency of each number, and the five numbers most drew.
    round = int(input('Type in the last lottery round: '))
    print()
    results= []

    for num in range((round-19), round+1):

        # Taking the lottery result through web scraping.
        query = f"lotofacil + {num} + noticias.uol.com.br"
        url = googlesearch.search(query, tld="co.in", num=1, stop=1, pause=2)
        source = requests.get(*url).text
        soup = bs4.BeautifulSoup(source, 'html.parser')

        # Extracting only the numbers.
        lottery_result = re.findall(r'(?:(?:[0-9]{2}\s?-?\s?){15})', soup.text)[0].replace(' ', '')  
        print(f'Round: {num} - Result: {[lottery_result]}')

        # Storing the results.
        results.append(lottery_result)
    print()

    # Getting the frequency of each number.
    frequency = {}
    results = ''.join(results).replace('-', '') 
    lottery_result = [int(results[x: x+2]) for x in range(0, len(results), 2)]

    for num in range(1, 26):
        frequency[num] = lottery_result.count(num)

    print('Frequency of each number.')    
    print(frequency)
    print()

    # Numbers to consider based on previous results.
    frequency = sorted(frequency.items(),key=lambda x:x[1])[::-1]
    numbers = list(dict(frequency).keys())
    print('Numbers most drew in recent rounds.')
    return sorted(numbers[0:5])

print(score())

# It's important to remember that past outcomes do not guarantee future results in a lottery.