import sys, subprocess
subprocess.run('cls', shell=True)
print('Test Free - Inter. Challenges - 100')
print()
# crt + D / alt + mouse / alt + up or down / shift + alt + up or down / crt + l
# crt + N .. crt + k, m .. crt + s

def get_order(input):

    menu = ['Burger', 'Fries', 'Chicken', 'Pizza', 
            'Sandwich', 'Onionrings', 'Milkshake', 'Coke']
    quantity = [input.count(item.lower()) for item in menu]
    orders = [(x[0] + ' ') * x[1] for x in list(zip(menu, quantity))]
    return ''.join(orders)

print(getOrder("milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"))
