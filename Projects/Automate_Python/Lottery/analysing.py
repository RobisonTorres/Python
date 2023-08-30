import json
import random
print('Analyzing Previous Results.')
print()


def open_json():
     
     # This function opens the file pre_results.json, and organizes the data to analysis.
     try:
        file = open('pre_results.json')
        lottery_results = json.load(file).values()
        results = ''.join(lottery_results).replace('-', '') 
        numbers = [int(results[x: x+2]) for x in range(0, len(results), 2)]
        return numbers
     
     except:
         return 'File not found.'

def even_odd():

    # This function returns the percentage of even and odd numbers.
    numbers = open_json()
    count_even = len([n for n in numbers if n % 2 == 0])
    even_nums = float(f'{(count_even/ len(numbers)*100):.2f}')
    return f'From all numbers drew in previous results '\
           f'{even_nums}% of them are even, and {100 - even_nums}% are odd.\n'

def frequency():
    
    # This function gets the frequency of each number 
    # and shows the five numbers most and least drawn.    
    result_numbers = open_json()
    fre_nums = {}
    for num in range(1, 26):
        fre_nums[num] = result_numbers.count(num)
    
    # Numbers most an least drawn.
    fre_num_sorted = sorted(fre_nums.items(),key=lambda x:x[1])[::-1]
    numbers = list(dict(fre_num_sorted).keys())
    return f'The frequency of each number in previous result is: \n{fre_nums}.\n\n'\
           f'Most drawn - {sorted(numbers[0:5])}. '\
           f'Least drawn - {sorted(numbers[20:])}.'     
    
def simulate_games():

    # This function simulates 100,000 games and calculate scores.
    random_games = []
    for x in range(0, 100_000):  
        random_games.append(random.sample(range(1, 26), 15))
  
    score = []
    random_result = random.sample(range(1, 26), 15)
    for num in range(0, len(random_games)):
            score.append(15 - len(set(random_result) - set(random_games[num])))

    # Frequency of winning prizes.    
    score_prizes = {}
    for num in range(11, 16):
        score_prizes[str(num) + ' pts'] = score.count(num)
    
    return (f"\nAfter simulating 100,000 random games, "
        f"the frequency of each score required to win prizes is:\n"
        f"{score_prizes}.\n")

def main():
    
    print(even_odd())
    print(frequency())
    print(simulate_games())
      
main()
