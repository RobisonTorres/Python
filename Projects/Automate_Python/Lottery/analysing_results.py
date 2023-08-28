import json
import random
print('Analyzing Previous Results.')
print()

def analyse_results():
    
    # This function analyses previous results from lottery, gives frequency 
    # of each number, and shows the probability of winning prizes.

    # Opening the file.
    file = open('pre_results.json')   
    results = json.load(file).values()

    # Arranging the data to analyse.
    results = ''.join(results).replace('-', '') 
    lottery_result = [int(results[x: x+2]) for x in range(0, len(results), 2)]
    x = 0
    grouped_results = []
    while x < len(lottery_result):
        grouped_results.append(lottery_result[x:x+15])
        x += 15

    # Even or Odd.
    count_even = 0
    for num in lottery_result:
        if num % 2 == 0:
            count_even += 1
    even_nums = float(f'{(count_even/ len(lottery_result)*100):.2f}')
    odd_nums = 100 - even_nums
    print(f'From all numbers drew in {len(grouped_results)} previous \
results {even_nums}% of them are even, and {odd_nums}% are odd.\n')

    # Frequency of each number in previous results.    
    frequency = {}
    for num in range(1, 26):
        frequency[num] = lottery_result.count(num)
    print('Frequency of each number.')    
    print(frequency)

    # Numbers most drew in these previous results.
    frequency = sorted(frequency.items(),key=lambda x:x[1])[::-1]
    numbers = list(dict(frequency).keys())
    print('\nNumbers most drew in these rounds.')
    print(sorted(numbers[0:10]))

    # Simulate random games and calculate scores.
    random_games = []
    for x in range(0, 100_000):  
        random_games.append(random.sample(range(1, 26), 15))
  
    score = []
    random_result = random.choice(grouped_results)
    for num in range(0, len(random_games)):
            score.append(15 - len(set(random_result) - set(random_games[num])))

    # Probability of winning prizes.    
    score_prizes = {}
    for num in range(11, 16):
        score_prizes[str(num) + ' pts'] = score.count(num)

    return (f"\nAfter simulating 100,000 random games based in one previous results, "
        f"the analysis indicates the frequency of each score required to win prizes is:\n"
        f"{score_prizes}.\n")
      
print(analyse_results())
