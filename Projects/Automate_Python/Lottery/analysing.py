import open_save
import random
print('Simulating.')
print()

def organize_data():
     
     # This function organizes the data to analyze.
    lottery_results = open_save.open_file().values()
    results = ''.join(lottery_results).replace('-', '') 
    numbers = [int(results[x: x+2]) for x in range(0, len(results), 2)]
    return numbers

def check_duplicate():

    # This function checks the data for repeated results.
    lottery_results = open_save.open_file()
    values = list(lottery_results.values())
    count = [v for v in values if values.count(v) >= 2]
    repeat_keys = [k for k in lottery_results.keys() if lottery_results[k] in count]

    if count:
        return(f'Please check the data, these rounds {"-".join(repeat_keys)} '\
               f'have duplicated results.\n')
    return 'Each lottery\'s result is unique in this dataset.\n'

def even_odd():

    # This function returns the percentage of even and odd numbers.
    numbers = organize_data()
    count_even = len([n for n in numbers if n % 2 == 0])
    even_nums = float(f'{(count_even/ len(numbers)*100):.2f}')
    return f'From all numbers drawn in {int(len(numbers)/ 15)} previous games, '\
           f'{even_nums}% of them are even and {100 - even_nums}% are odd.\n'

def frequency():
    
    # This function gets the frequency of each number and shows the five 
    # numbers most and least drawn.    
    result_numbers = organize_data()
    fre_nums = {}
    for num in range(1, 26):
        fre_nums[num] = result_numbers.count(num)
    
    # Numbers most an least drawn.
    fre_num_sorted = sorted(fre_nums.items(),key=lambda x:x[1])[::-1]
    numbers = list(dict(fre_num_sorted).keys())
    
    return f'Numbers most drawn - {sorted(numbers[0:5])}. '\
           f'Numbers least drawn - {sorted(numbers[20:])}.'     

def repetition():

    # This function calculates the frequency of repeated numbers 
    # between current result and previous one, except for the first result.
    numbers = organize_data()
    grouped_results = [numbers[x:x+15] for x in range(0, len(numbers), 15)]
    rep_numbers = [(15 - len(set(grouped_results[x]) - set(grouped_results[x-1])))
                   for x in range(0, len(grouped_results)) if x != 0]
    
    # Frequency of repeated numbers.
    fre_result = {}
    for num in range(6, 16):
        fre_result[num] = rep_numbers.count(num)

    # Games that repeated at least 9 numbers from previous result.
    repeated = sum(list(fre_result.values())[3:]) 
    
    return f'\nThe analysis shows that out of {len(grouped_results) - 1} games analyzed, '\
           f'{((repeated / (len(grouped_results) - 1)) * 100):.2f}% '\
           f'of them repeated at least 9 numbers from the previous result.'          
 
def simulate_games():

    # This function simulates 100,000 games and calculate scores. Each game is a selection of 15 numbers between 1 and 25.
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
    
    return (f"By simulating 100,000 random games, "
        f"the occurrence of each score required to win prizes is:\n"
        f"{score_prizes}.\n")

def main():
    
    # This function brings all the analyse.
    print(simulate_games())
    print("Analyzing Previous Results.\n")
    print(check_duplicate())
    print(even_odd())
    print(frequency())
    print(repetition())

main()
