#!/usr/bin/env python3
# isUnique: implement an algorithm to determine if a string has all unique characters. And what if you cant use other data structures?

# Obvious answer first approach.


def isUnique1(input):
    """
    Obvious attempt nested for loop. 
    Space O(1) only requires storing initial string. 
    Time O(n^2)
    assume that capitalization matters. 
    """
    for i in range(0, len(input) -1):
        for j in range(i+1, len(input)):
            if input[i] == input[j]:
                return False
    return True


def isUnique2(input):
    """
    Second attempt uses hashtable if entry already exists then exit. 
    Space O(n) 
    Time O(n) 
    """
    hashtable = {}
    for i in input:
        if i in hashtable.keys():
            return False
        hashtable[i] = i;
    return True



if __name__ == "__main__":
    # Testing isUnique1
    # Test1 
    if not isUnique1("string"):
        print("Test 1 Failed: input = 'string' expected True")
    # Test2
    if isUnique1("ss"):
        print("Test 2 Failed: input = 'ss' expected False")
    # Test3 
    if not isUnique1("Strings"):
        print("Test 3 Failed: input = 'Strings' expected True")
    if not isUnique1("!@#$^&*sEmx"):
        print("Test 4 Failed: input = '!@#$^&*sEmx' expected True")
    print("*****End of Tests attempt 1*****")
    
    if not isUnique2("string"):
            print("Test 1 Failed: input = 'string' expected True")
    # Test2
    if isUnique2("ss"):
        print("Test 2 Failed: input = 'ss' expected False")
    # Test3 
    if not isUnique2("Strings"):
        print("Test 3 Failed: input = 'Strings' expected True")
    if not isUnique2("!@#$^&*sEmx"):
        print("Test 4 Failed: input = '!@#$^&*sEmx' expected True")
    print("*****End of tests attempt 2*****")