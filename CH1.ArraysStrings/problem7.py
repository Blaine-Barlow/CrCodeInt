# Rotate matrix, Given NxN matrix, rotate it 90 degrees. each value given as an int. 

def rotate(input):
    if len(input) == 0 or len(input) != len(input[0]):
        return False
    n = len(input)
    for layer in range(0, n//2):  # python integer division //
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            # save top
            top = input[first][i]
            
            # left goes to top
            input[first][i] = input[last - offset][first]
            # bottom goes to left
            input[last - offset][first] = input[last][last-offset]
            # right goes to bottom
            input[last][last-offset] = input[i][last]
            # top goes to right
            input[i][last] = top
    return True

if __name__ == "__main__":
    print("***** Start of Tests for Problem 7*****")
    input = [[1,2], [2], [3,4]]
    # Test 1
    if rotate(input):
        print("Test 1 Error: failed to return false when input array is not NxN")
    # Test 2
    if rotate([]):
        print("Test 2 Error: failed to return false when input array is empty")
    # Test 3
    input = [[1,2,3],[4,5,6],[7,8,9]]
    print("Input is: ")
    for line in input:
        print(line)
    rotate(input)
    print("Input after Rotate:")
    for line in input:
        print(line)
    # Test 4
    input = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    print("Input before rotate: ")
    for line in input:
        print(line)
    rotate(input)
    print("Input after Rotate: ")
    for line in input:
        print(line)
    print("*****End of Tests for Problem 7*****")
    
    
    