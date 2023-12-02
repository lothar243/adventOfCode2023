import sys

def onlydigits(inputString):
    "Takes a string and returns only the digit characters"
    return [char for char in inputString if char.isdigit()]

def firstLast(inputString):
    "Takes a string and returns the first and last character"
    return(inputString[0] + inputString[-1])

if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) == 1:
        inputText = "1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet".split("\n")
    elif len(sys.argv) == 2:
        with open('input', 'r') as inputfile:
            inputText = inputfile.readlines()
    print(inputText)
    sum = 0
    for line in inputText:
        sum += int(firstLast(onlydigits(line)))
    print(sum)
