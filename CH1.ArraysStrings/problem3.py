# Problem 3 URLify 
# input: "string to replace     ", 16
# replace all spaces with "%20"

# Obvious loop attempt. 

def urlify1(input, numChar):
    output = ""
    for i in range(numChar):
        if input[i] == " ":
            output += "%20"
        else:
            output += input[i]
    return output


if __name__ == "__main__":
    print("*****Start of tests*****")
    print(urlify1("test 1   ", 6))
    print(urlify1("t e s t 1       ", 9))
    print("*****End of Tests*****")
    
    
# Notes from reading solution.
# solution is very similar but dealt in java
# if implemented in Java. need to consider char arrays.
# need to count spaces and adjust based on index in array. 
# python returns a new string. 
# it is dependent on language both are acceptable. 