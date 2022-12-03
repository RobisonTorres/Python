print('From Code Wars.')
print()

def dir_reduction(arr):
    
    # Task - Write a function which will take an array of strings 
    # and returns an array of strings with the needless directions
    # removed (W<->E or S<->N side by side).
    while ("NORTH SOUTH") in ' '.join(arr) or ("SOUTH NORTH") in ' '.join(arr) \
        or ("EAST WEST") in ' '.join(arr) or ("WEST EAST") in ' '.join(arr):
        arr = ' '.join(arr)
        if ("NORTH SOUTH") in arr or ("SOUTH NORTH") \
            or ("EAST WEST") in arr or ("WEST EAST"):
            arr = arr.replace("NORTH SOUTH", '') 
            arr = arr.replace("SOUTH NORTH", '')
            arr = arr.replace("EAST WEST", '')
            arr = arr.replace("WEST EAST", '') 
        arr = arr.split()
    return arr

print(dir_reduction(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
# Outputs - ['WEST']

''' - Clever.
import re

def dirReduc(arr):
    pattern = re.compile('NORTH\s+SOUTH|SOUTH\s+NORTH|EAST\s+WEST|WEST\s+EAST')
    s = ' '.join(arr)
    while pattern.search(s):
        s = pattern.sub('', s)
    return s.split()

Python’s re.compile() method is used to compile a regular expression pattern provided
as a string into a regex pattern object (re.Pattern). Later we can use this pattern 
object to search for a match inside different target strings using regex methods 
such as a re.match() or re.search().
'''
