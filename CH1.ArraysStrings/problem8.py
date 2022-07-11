# Zero Matrix: given a matrix if an element is 0 then set that entire row and column to 0. 

import array
from socket import AF_NETROM


def make2Zeros(inputArray):
    rows = []
    cols = []
    
    for row in range(len(inputArray)):
        for col in range(len(inputArray[0])):
            if inputArray[row][col] == 0:
                rows.append(row)
                cols.append(col)
    for row in rows:
        for col in range(len(inputArray[0])):
            inputArray[row][col] = 0
    for col in cols:
        for row in range(len(inputArray)):
            inputArray[row][col] = 0
                    
def arrayPrinter(Arr):
    for row in Arr:
        print(row)

if __name__ == "__main__":
    print("*****Start of Tests for Problem 8*******")
    firstArray = [[0,1], [1,1]]
    print("First Array:")
    arrayPrinter(firstArray)
    print("After Function:")
    make2Zeros(firstArray)
    arrayPrinter(firstArray)

    firstArray = [[1,1,1],[1,0,1]]
    print("Test 2: First Array")
    arrayPrinter(firstArray)
    make2Zeros(firstArray)
    print("After Function:")
    arrayPrinter(firstArray)    
    
    
    firstArray = [[1, 1, 1, 1, 1, 1,], [2,4,5, 1, 1, 1], [0, 0, 1, 1, 1, 1,], [1, 1, 1, 1, 1, 0],[1, 1, 1, 1, 1, 1], [1,1,1,1,1,1]]
    print("Test 3: first array")
    arrayPrinter(firstArray)
    make2Zeros(firstArray)
    print("After function:")
    arrayPrinter(firstArray)
    print("*****End of Tests*****")