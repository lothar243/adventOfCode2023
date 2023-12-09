import sys
sample_input = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

def find_differences(numberList: list):
    diffList = []
    for i in range(1, len(numberList)):
        diffList.append(numberList[i] - numberList[i - 1])
    return diffList

def all_zero(numberList: list):
    return all([val == 0 for val in numberList])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        lines = sample_input.split("\n")
    else:
        with open(sys.argv[1]) as inputfile:
            lines = [line.strip() for line in inputfile.readlines()]

    lineSums = 0
    for line in lines:
        numListStack = [ [int(num) for num in line.split(" ")], ]
        while not all_zero(numListStack[-1]):
            numListStack.append(find_differences(numListStack[-1]))
        # extrapolate the previous value
        newPreviousValue = 0
        for numList in numListStack[-2::-1]:
            newPreviousValue = numList[0] - newPreviousValue
        print(newPreviousValue)
        lineSums += newPreviousValue

        
    print(lineSums)