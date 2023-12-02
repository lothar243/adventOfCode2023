import sys

def firstdigit(inputString: str):
    "Takes a string and returns the first number that occurs whether it is numerical or in text"
    numberString_to_digit = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
                             "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
    numberString_to_index = {}
    for numberString in numberString_to_digit:
        numberString_to_index[numberString] = inputString.find(numberString)
    smallestIndex = 99999
    val = -1
    for numberString, numberIndex in numberString_to_index.items():
        if numberIndex >= 0 and numberIndex < smallestIndex:
            smallestIndex = numberIndex
            val = numberString_to_digit[numberString]
    return val

def lastdigit(inputString: str):
    "Takes a string and returns the last number that occurs whether it is numerical or in text"
    numberString_to_digit = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
                             "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
    numberString_to_index = {}
    for numberString in numberString_to_digit:
        numberString_to_index[numberString] = inputString.rfind(numberString)
    largestIndex = -1
    val = -1
    for numberString, numberIndex in numberString_to_index.items():
        if numberIndex > largestIndex:
            largestIndex = numberIndex
            val = numberString_to_digit[numberString]
    return val


def firstLast(inputString):
    "Takes a string and returns the first and last character"
    return(firstdigit(inputString) * 10 + lastdigit(inputString))

if __name__ == "__main__":

    print(sys.argv)
    if len(sys.argv) == 1:
        inputText = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
seven6sevenphjfhdtnrhfsgcfived9seven""".split("\n")
    elif len(sys.argv) == 2:
        with open('input', 'r') as inputfile:
            inputText = inputfile.readlines()
    print(inputText)
    sum = 0
    for line in inputText:
        val = int(firstLast(line))
        print(line.strip(), val)
        sum += val
    print(sum)
