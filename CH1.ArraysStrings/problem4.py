# problem 4. is the string a palindrome permutation.

# example:
    # input: tact coa
    # output: True ("taco cat", "atco cta", etc)
    
# if length string odd then only 1 char can have odd count.
# if length string even then no char can have odd count. 

def palPerm1(input):
    strLength = len(input.replace(" ", ""))  # true length of string
    hashy = {}
    for i in range(len(input)):
        if input[i] != " ":
            if input[i] not in hashy.keys():
                hashy[input[i]] = 1
            else: 
                hashy[input[i]] += 1
    if strLength % 2 == 0:          # even
        for value in hashy.values():
            if value % 2 == 1:
                return False
        return True
    else:                           # odd
        foundOdd = False
        for value in hashy.values():
            if value % 2 == 1:
                if not foundOdd:
                    foundOdd = True
                else:
                    return False
        return True

if __name__ == "__main__":
    print("*****Start of tests*****")
    # Test 1 
    if not palPerm1("extxe"):
        print("Test 1 failed, palindrome input returned false")
    if palPerm1("this is a test"):
        print("Test 2: failed non pal returned true")
    if not palPerm1("tact coa"):
        print("Test 3: example input returned false")
    if not palPerm1("a"):
        print("Test 4: returned false on single character")
    if not palPerm1("aa"):
        print("Test 5: returned false on double char")
    print("*****End of tests*****")
    
    
# notes for after reading. 
# this solution is case sensitive but the problem is non case sensitive so need to add a lowercase change. 
# this solution also does not check for special characters. should be a-z only. 
# time is also O(n) for n length of string. 