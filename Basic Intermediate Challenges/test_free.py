print('Test Free - keep it clean')
print()

def good_vs_evil(good, evil):
    good = sum([int(n) for n in good.split(' ')])
    evil = sum([int(n) for n in evil.split(' ')])
    if good >  evil:
        return 'Battle Result: Good triumphs over Evil'
    elif evil >  good:
        return 'Battle Result: Evil eradicates all trace of Good'
    else:
        return'Battle Result: No victor on this battle field'

print(good_vs_evil('1 1 1 1 1 1 1', '1 1 1 1 1 1'))
