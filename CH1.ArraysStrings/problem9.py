
def isSubstring(s1, s2):
    return s2 in s1

def isRotation(s1, s2):
    if len(s1) == len(s2) and len(s1) > 0:
        newString = s1 + s1
        return isSubstring(newString, s2)
    return False

if __name__ == "__main__":
    print("*****Start of tests for problem 9*****")
    s1 = "waterbottle"
    s2 = "terbottlewa"
    outcome = isRotation(s1, s2)
    print("Test 1: S1: " +  s1 + " S2: " + s2 + " OUTCOME: " + str(outcome))

    # s1 = "waterbottle"
    # s2 = "retawbottle"
    # print("Test 1: S1: " +  s1 + " S2: " + s2 + " OUTCOME: " + str(outcome)) # should be false.
