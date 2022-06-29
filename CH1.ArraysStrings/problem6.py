# string compression: compress a string to its counts of characters. 'ccc' = c3, "aaabbbccc" = "a3b3c3"
# can assume the string contains only uppercase and lowercase letters. 


# Runtime O(n) at most iterate through every character twice second - 1 iteration
def compress(myString):
    myTable = {}
    for character in myString:
        if character not in myTable.keys():
            myTable[character] = 1
        else:
            myTable[character] += 1
    if len(myTable) == len(myString):
        return myString
    temp = ""
    for key in myTable.keys():
        temp += key + str(myTable[key])
    return temp 

if __name__ == "__main__":
    print("*****Start of test Cases for Problem 6******")
    # Test 1
    if compress("ccc") != "c3":
        print("Test 1 Error: single result of compressed single letter failed")
    # Test 2
    if compress("aaabbbccc") != "a3b3c3":
        print("Test 2 Error: main example failed to return correct string")
    # Test 3
    if compress("CAD") != "CAD":
        print("Test 3 Error: Failed to return same string.")
    # Test 4
    if compress("A") != "A":
        print("Test 4 Error: Failed to return single letter string uncompressed.")        
    
    
    
    
    
    print("*****End of test cases for problem 6******")