print('From Code Wars.')
print()

def get_order(input):

    # This function makes a string (order) readable.
    orders = []
    menu = ['Burger', 'Fries', 'Chicken', 'Pizza', 'Sandwich', 'Onionrings', 'Milkshake', 'Coke']
    quantity = [input.count(item.lower()) for item in menu]
    menu_quantity = [list(item) for item in zip(menu, quantity)]
    for i in menu_quantity:
        while i[1] > 0:
            orders.append(i[0])
            i[1] -= 1
    return ' '.join(orders)

print(get_order("milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"))
# Outputs - Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke
