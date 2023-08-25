import json
import random
print('Analyse Previous Results.')
print()

def analyse_results():
    
    # This function analyses previous results from lottery.
    file = open('pre_results.json')   
    results = json.load(file).values()
    results = ''.join(results).replace('-', '') 
    lottery_result = [int(results[x: x+2]) for x in range(0, len(results), 2)]

    count_even = 0
    for num in lottery_result:
        if num % 2 == 0:
            count_even += 1
    even_nums = float(f'{(count_even/ len(lottery_result)*100):.2f}')
    odd_nums = 100 - even_nums

    x = 0
    grouped_results = []
    while x < len(lottery_result):
        grouped_results.append(lottery_result[x:x+15])
        x += 15

    print(f'From all numbers drew in {len(grouped_results)} previous \
results {even_nums}% of them are even, and {odd_nums}% are odd.\n')
    
    frequency = {}
    for num in range(1, 26):
        frequency[num] = lottery_result.count(num)

    print('Frequency of each number.')    
    print(frequency)

    # Numbers to consider based on previous results.
    frequency = sorted(frequency.items(),key=lambda x:x[1])[::-1]
    numbers = list(dict(frequency).keys())
    print('\nNumbers most drew in these rounds.')
    print(sorted(numbers[0:15]))
    
    random_games = []
    for x in range(0, 100):
        random_games.append(random.sample(range(1, 26), 15))
    
    # Compare the each random game with the actual results and calculate scores.
    score = []

    for z in range(0, len(random_games)):
        for n in range(0, len(grouped_results)):
            score.append(15 - len(set(grouped_results[n]) - set(random_games[z])))

    return (f"\nAfter simulating {len(random_games)} random games in {len(grouped_results)} \
previous results, which is {len(score)} scores, the analysis shows that the lowest score \
achieved was {min(score)}, while the highest score reached was {max(score)}.\n")
        
print(analyse_results())
