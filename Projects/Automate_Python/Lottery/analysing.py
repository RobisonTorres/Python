import open_save
import random
print('Analyzing Previous Results.')
print()

def organize_data():
     
     # This function organizes the data to analysis.
    lottery_results = open_save.open_file().values()
    results = ''.join(lottery_results).replace('-', '') 
    numbers = [int(results[x: x+2]) for x in range(0, len(results), 2)]
    return numbers

def even_odd():

    # This function returns the percentage of even and odd numbers.
    numbers = organize_data()
    count_even = len([n for n in numbers if n % 2 == 0])
    even_nums = float(f'{(count_even/ len(numbers)*100):.2f}')
    return f'From all numbers drew in {int(len(numbers)/ 15)} previous games, '\
           f'{even_nums}% of them are even and {100 - even_nums}% are odd.\n'

def frequency():
    
    # This function gets the frequency of each number 
    # and shows the five numbers most and least drawn.    
    result_numbers = organize_data()
    fre_nums = {}
    for num in range(1, 26):
        fre_nums[num] = result_numbers.count(num)
    
    # Numbers most an least drawn.
    fre_num_sorted = sorted(fre_nums.items(),key=lambda x:x[1])[::-1]
    numbers = list(dict(fre_num_sorted).keys())
    
    return f'Numbers most drawn - {sorted(numbers[0:5])}.\n'\
           f'Numbers least drawn - {sorted(numbers[20:])}.'     

def repetition():

    # This function calculates the frequency of repeated numbers 
    # between current result and previous one, except for the first result.
    numbers = organize_data()
    
    # Each result has 15 numbers.
    grouped_results = [numbers[x:x+15] for x in range(0, len(numbers), 15)]

    # Calculate the frequency of repeated numbers.
    rep_numbers = [(15 - len(set(grouped_results[x]) - set(grouped_results[x-1])))
                   for x in range(0, len(grouped_results)) if x != 0]
    
    fre_result = {}
    for num in range(6, 14):
        fre_result[num] = rep_numbers.count(num)

    repeated = sum(list(fre_result.values())[3:]) # games that repeated at least 9 numbers.

    return f'\nThe analysis shows that out of {len(grouped_results) - 1} games analyzed, '\
        f'{((repeated / (len(grouped_results) - 1)) * 100):.2f}% '\
        f'of them repeated at least 9 numbers from the previous result.'          
    
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
    
    return (f"\nAnd after simulating 100,000 random games, "
        f"the frequency of each score required to win prizes is:\n"
        f"{score_prizes}.\n")

def main():
    
    print(even_odd())
    print(frequency())
    print(repetition())
    print(simulate_games())

main()
