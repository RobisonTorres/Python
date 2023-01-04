from collections import Counter
print('From Code Wars.')
print()

def scramble(s1, s2):
   
    # This fuction checks if a portion of str1 characters 
    # can be rearranged to match str2.
    return Counter(s1) >= Counter(s2)

print(scramble("camtjtfhooex", "hotjotac"))  # True.
