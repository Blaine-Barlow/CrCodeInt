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
    elif abs(len(first) - len(second)) == 0:
        return replace(first, second)
    else:
        return oneEdit(first, second)

def replace(s1, s2):
    firstDifference = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if firstDifference:
                return False
            firstDifference = True
    return True

def oneEdit(s1, s2):
    # one edit is when the length of strings are off by 1. so an add or a delete.
    s1Index = 0
    s2Index = 0
    while s1Index < len(s1) and s2Index < len(s2):
        if s1[s1Index] != s2[s2Index]:
            if s1Index != s2Index:
                return False
            s2Index += 1
        else:
            s1Index += 1
            s2Index += 1
    return True

if __name__ == "__main__":
    print("*****Start of tests for oneAway*****")
    # Test 1
    if oneAway("pale1", "pale2"):
        print("Test 1 Error: strings containing numbers returned true")
    # Test 2
    if oneAway("pale", "pe"):
        print("Test 2 Error: strings of length difference > 1 returned true")
    # Test 3
    if not oneAway("pale", "bale"):
        print("Test 3 Error: replace returned false when it is one away")
    # Test 4 
    if oneAway("pale", "bald"):
        print("Test 4 Error: returned true when 2 replaces exist.")
    # Test 5
    if not oneAway("pale", "pales"):
        print("Test 5 Error: Add one returned false")
    # Test 6
    if not oneAway("pales", "pale"):
        print("Test 6 Error: remove one returned false")
    # Test 7
    if oneAway("exit", "pal"):
        print("Test 7 Error: returned true when more than one edit required")
    
    print("*****End of tests for oneAway*****")