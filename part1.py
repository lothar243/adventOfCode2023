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
        

if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        lines = sample_input.split("\n")
    else:
        with open(sys.argv[1]) as inputfile:
            lines = [line.strip() for line in inputfile.readlines()]
    
    # create a bitmap the same size as the input with True in spots that are adjacent to symbols
    # (slightly oversized so that I can cheat with adjacencies)
    height = len(lines)
    width = len(lines[0])
    bitmap = [[False] * (width + 1)] * (height+1)
    # find all the symbols and mark adjacent bit True
    ignoredCharacters = "0123456789."
    for x in range(width):
        for y in range(height):
            if lines[y][x] not in ignoredCharacters:
                # print(x, y, lines[y][x])
                for deltaX in (-1, 0, 1):
                    for deltaY in (-1, 0, 1):
                        bitmap[y + deltaY][x + deltaX] = True
    # pprint(bitmap)
    # for line in lines:
    #     pprint(extractNumbers(line, width))
    sum = 0
    for i in range(height):
        

    # then parase any number that has a digit marked True