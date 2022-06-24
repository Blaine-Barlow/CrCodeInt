# Problem 2: given two strings determine if one string is a permutation of the other.

# in python s1 in s2: is O(NM) in Worst case. New Algorithms now O(N + M).  O(N) on average

# attempt one: 

def permutation1(s1, s2):
    """
    Simple implementation s1 and s2 are strings. Could add a check for types passed in. Assumption made is strings passed in.
    Time: O(n) but with worst case O(nm) where n and m are lengths of the strings.
    space: O(1)
    """
    if len(s1) != len(s2): 
        return False
    for c in s2:
        if c not in s1:
            return False
    return True


def permutation2(s1, s2):
    """
    Use a hashtable to track the number of each character in the first string. if at any instance the second string has more than the first of a certain character
    it will go negative. 
    """
    hashtable = {}
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        if s1[i] in hashtable.keys():
                hashtable[s1[i]] += 1
        else:
            hashtable[s1[i]] = 1
    for i in range(len(s2)):
        if s2[i] not in hashtable.keys():
                return False
        hashtable[s2[i]] -= 1
        if hashtable[s2[i]] < 0:
            return False
    return True
            




if __name__ == "__main__":
    # Test 1 
    if permutation1("string", "str"):
        print("Test 1 Failed: strings of different size returned true.")
    # Test 2
    if permutation1("string", "sxcett"):
        print("Test 2 Failed: returned true even though no permutation exists")
    # Test 3
    if not permutation1("String", "trngiS"):
        print("Test 3 Failed: returned false when String 2 is a permutation")
    print("*****End of Tests on Attempt 1*****")
    # Test 4 
    if permutation2("string", "str"):
        print("Test 4 Failed: strings of different size returned true.")
    # Test 5
    if permutation2("string", "sxcett"):
        print("Test 5 Failed: returned true even though no permutation exists")
    # Test 6
    if not permutation2("String", "trngiS"):
        print("Test 6 Failed: returned false when String 2 is a permutation")
    if permutation2("String", "SStrin"):
        print("Test 7 Failed: more characters in string 2 returned True")
    print("*****End of Tests on Attempt 2*****")


