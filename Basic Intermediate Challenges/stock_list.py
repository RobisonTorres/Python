print('From Code Wars.')
print()

def stock_list(list_of_art, list_of_cat):
    
    # This function sums the quantity of items based in their code.
    code = list(zip(list_of_cat, len(list_of_cat) * [0]))
    product = [code.split() for code in list_of_art]
    new = []
    for x in range(len(code)):
        new.append(
            f'({code[x][0]} : {sum([code[x][1] + int(l[1]) for l in product if code[x][0].startswith(l[0][0])])})')
    return '' if [] in (list_of_art, list_of_cat) else ' - '.join(new)


print(stock_list(["ABART 20", "CDXEF 50", "BTSQZ 89", "DRTYM 60"], ["A", "B", "C", "W"]))
# Outputs - (A : 20) - (B : 89) - (C : 50) - (W : 0)
