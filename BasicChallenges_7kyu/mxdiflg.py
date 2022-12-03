print('From Code Wars')
print()

def mxdiflg(a1, a2):

    # This function returns the max difference between two arrays,
    # Or -1 if one of them is empty.
    try:
        a = abs(len(max(a1, key=len)) - len(min(a2, key=len)))
        b = abs(len(min(a1, key=len)) - len(max(a2, key=len)))
        return max(a, b)
    except:
        return -1

print(mxdiflg(["oox", "ejjuyyy", "plmiis", "xxwwkktt", "znnnnfqknaz", "qqquuhii"],
              ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]))
# Outputs - 13
