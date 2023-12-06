import sys
from pprint import pprint

sample_input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

def extractNumbers(lineString: str, width):
    "Takes a linestring input, returns a list of dictionaries for each number present (along with start and stop indices)"
    readingNumber = False
    numbers = []
    for i in range(width):
        currentChar = lineString[i]
        if not readingNumber: # encountered a new number
            if currentChar.isdigit():
                readingNumber = True
                currentNumber = {'value': currentChar, 'start': i}
            else: # still not reading a number
                pass
        else:
            if currentChar.isdigit(): # continue reading the number
                currentNumber['value'] += currentChar
            else: # you're done reading the number, finish up
                readingNumber = False
                currentNumber['stop'] = i - 1
                numbers.append(currentNumber)
    if readingNumber: # the line ended with a number... finish up
        readingNumber = False
        currentNumber['stop'] = width
        numbers.append(currentNumber)
    for number in numbers:
        number['value'] = int(number['value'])
    return numbers
        
def gearRatio(lineNumbers, x, y):
    "Returns the gear ratio for an asterisk located at x,y (or 0 if it's not a gear)"
    yRange = range(max(0, y - 1), min(len(lineNumbers), y + 1) + 1)
    numAdjacentNumbers = 0
    productOfNumbers = 1
    for newY in yRange:
        for lineNumber in lineNumbers[newY]:
            if is_adjacent_to_x(lineNumber, x):
                numAdjacentNumbers += 1
                productOfNumbers *= lineNumber['value']
    if numAdjacentNumbers == 2:
        return productOfNumbers
    else:
        return 0

def is_adjacent_to_x(lineNumber, x):
    "Returns True if x is adjacent to linenumber."
    # achieve this by x being between 'start - 1' and 'stop + 1'
    return lineNumber['start'] - 1 <= x <= lineNumber['stop'] + 1

if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        lines = sample_input.split("\n")
    else:
        with open(sys.argv[1]) as inputfile:
            lines = [line.strip() for line in inputfile.readlines()]
    height = len(lines)
    width = len(lines[0])
    # get all the numbers
    lineNumbers = [] # This will be a list of lists, first indexed by line number, then which number
    for i in range(height):
        lineNumbers.append(extractNumbers(lines[i], width))

    # find each asterisk and add its gear ratio
    sum = 0
    for y in range(height):
        for x in range(width):
            if lines[y][x] == "*":
                sum += gearRatio(lineNumbers, x, y)

    print(sum)