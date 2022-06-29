# one away problem. 
# make a function that determines if two strings are one edit away or 0 edits, edits are:
# insert , remove , replace. 

#input: S1, S2 


# Example: pale, ple -> true  // remove a
#   pales, pale ->true // remove s
#   pale, bale -> true // replace p with b
#   pale, bake -> false

from itertools import filterfalse
from logging import PlaceHolder


def oneAway(s1, s2):
    if not s1.isalpha() or not s2.isalpha():
        return False
    first = s1.lower()
    second = s2.lower()
    if abs(len(first) - len(second)) > 1:
        return False
    return True

def replace(s1, s2):
    return False

def oneEdit(s1, s2):
    return False

if __name__ == "__main__":
    print("*****Start of tests for oneAway*****")
    # Test 1
    if oneAway("pale1", "pale2"):
        print("Test 1 Error: strings containing numbers returned true")
    # Test 2
    if oneAway("pale", "pe"):
        print("Test 2 Error: strings of length difference > 1 returned true")
    # Test 3
    
    
    print("*****End of tests for oneAway*****")