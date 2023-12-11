import sys
from pprint import pprint

sample_input = """S-7F--7..
|.||.FJ..
|.LJ.L7..
L---7.|..
....L-J.."""



    # | is a vertical pipe connecting north and south.
    # - is a horizontal pipe connecting east and west.
    # L is a 90-degree bend connecting north and east.
    # J is a 90-degree bend connecting north and west.
    # 7 is a 90-degree bend connecting south and west.
    # F is a 90-degree bend connecting south and east.
    # . is ground; there is no pipe in this tile.
    # S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

def dump_error(lines: list, message: str):
    print(message)
    dumplines = []
    for line in lines:
        dumplines.append("".join(line))
    with open ('errorOutput', 'w') as outputfile:
        outputfile.write(message + "\n")
        outputfile.write("\n".join(dumplines))
    exit()

def traverse(charMap: list, x, y, xFrom, yFrom):
    # print(x, y, xFrom, yFrom)
    width = len(charMap[0])
    height = len(charMap)
    bitmap = [[False] * width for _ in range(height)]
    length = 0
    # check for out-of-bounds
    if x < 0 or x >= width or y < 0 or y >= height:
        return -1e99, bitmap
    char = charMap[y][x]
    while(char != 'S'):
        # check for out-of-bounds
        if x < 0 or x >= width or y < 0 or y >= height:
            return -1e99, bitmap
        bitmap[y][x] = True
        length += 1
        if x - xFrom == 1:
            # Coming from the left
            xFrom = x
            if char == '-':     # go right
                x += 1
            elif char == 'J':   # go up
                y -= 1
            elif char == '7':   # go down
                y += 1
            else:
                return -1e98, bitmap
        elif x - xFrom == -1:
            # coming from the right
            xFrom = x
            if char == '-':
                x -= 1          # continue left
            elif char == 'L':
                y -= 1          # go up
            elif char == 'F':
                y += 1          # go down
            else:
                return -1e97, bitmap
        elif y - yFrom == 1:
            # coming from above
            yFrom = y
            if char == '|':
                y += 1          # continue down
            elif char == 'L':
                x += 1          # go right
            elif char == 'J':
                x -= 1          # go left
            else:
                pass
                return -1e96, bitmap
        elif y - yFrom == -1:
            # coming from below
            yFrom = y
            if char == '|':
                y -= 1          # continue up
            elif char == '7':
                x -= 1          # go left
            elif char == 'F':
                x += 1          # go right
            else:
                return -1e95, bitmap
        char = charMap[y][x]
    bitmap[y][x] = True
    return length, bitmap

def explode(lines):
    replacementAboveLine = {
    ".": "...",
    "|": ".|.",
    "-": "...",
    "L": ".|.",
    "J": ".|.",
    "7": "...",
    "F": "...",
    "S": ".|.",

    }
    replacementSameLine = {
    ".": "...",
    "|": ".|.",
    "-": "---",
    "L": ".L-",
    "J": "-J.",
    "7": "-7.",
    "F": ".F-",
    "S": "-S-",

    }
    replacementBelowLine = {
    ".": "...",
    "|": ".|.",
    "-": "...",
    "L": "...",
    "J": "...",
    "7": ".|.",
    "F": ".|.",
    "S": ".|.",

    }
    outputLines = []
    for line in lines:
        aboveLine = [replacementAboveLine[char] for char in line]
        outputLines.append("".join(aboveLine))
        midLine = [replacementSameLine[char] for char in line]
        outputLines.append("".join(midLine))
        bottomLine = [replacementBelowLine[char] for char in line]
        outputLines.append("".join(bottomLine))
    return outputLines

def unexplode(lines: list):
    outputLines = []
    for y in range(1, len(lines), 3):
        newline = []
        for x in range(1, len(lines[y]), 3):
            newline.append(lines[y][x])
        outputLines.append("".join(newline))
    
    if len(sys.argv) < 3:
        for line in outputLines:
            print(line)
    else:
        with open(sys.argv[2], 'w') as outputfile:
            outputfile.write('\n'.join(outputLines))
    return outputLines

def shade(lines: list):
    for i, line in enumerate(lines):
        lines[i] = [char for char in line]

    height = len(lines)
    width = len(lines[0])

    # start by marking the border as "O"
    for x in range(width):
        if lines[0][x] == '.':
            lines[0][x] = 'O'
        if lines[-1][x] == '.':
            lines[-1][x] = 'O'
    for y in range(height):
        if lines[y][0] == '.':
            lines[y][0] = 'O'
        if lines[y][-1] == '.':
            lines[y][-1] = 'O'

    changed = True
    while changed:
        changed = False
        for y in range(height):
            for x in range(width):
                curChar = lines[y][x]
                if curChar not in {'O', 'I'}:
                    continue
                otherChar = {'O', 'I'}.difference(curChar).pop()
                # check above
                if y >= 1 and lines[y - 1][x] == '.':
                    changed = True
                    lines[y - 1][x] = curChar
                if y >= 2 and lines[y - 1][x] == '-' and lines[y - 2][x] == '.':
                    changed = True
                    lines[y - 2][x] = otherChar
                if y >= 1 and lines[y - 1][x] == otherChar:
                    dump_error(lines, f"{x=}, {y=}, {curChar=} next to {otherChar=}")
                if y >= 2 and lines[y - 1][x] == '-' and lines[y - 2][x] == curChar:
                    dump_error(lines, f"{x=}, {y=}, {curChar=} across from {curChar=}")
                # check below
                if y < height - 1 and lines[y + 1][x] == '.':
                    changed = True
                    lines[y + 1][x] = curChar
                if y < height - 2 and lines[y + 1][x] == '-' and lines[y + 2][x] == '.':
                    changed = True
                    lines[y + 2][x] = otherChar
                if y < height - 1 and lines[y + 1][x] == otherChar:
                    dump_error(lines, f"{x=}, {y=}, {curChar=} next to {otherChar=}")
                if y < height - 2 and lines[y + 1][x] == '-' and lines[y + 2][x] == curChar:
                    dump_error(lines, f"{x=}, {y=}, {curChar=} across from {curChar=}")
                # check left
                if x >= 1 and lines[y][x - 1] == '.':
                    changed = True
                    lines[y][x - 1] = curChar
                if x >= 2 and lines[y][x - 1] == '|' and lines[y][x - 2] == '.':
                    changed = True
                    lines[y][x - 2] = otherChar
                if x >= 1 and lines[y][x - 1] == otherChar:
                    dump_error(lines, f"{x=}, {y=}, {curChar=} next to {otherChar=}")
                if x >= 2 and lines[y][x - 1] == '|' and lines[y][x - 2] == curChar:
                    dump_error(lines, f"{x=}, {y=}, {curChar=} across from {curChar=}")
                # check right
                if x < width - 1 and lines[y][x + 1] == '.':
                    changed = True
                    lines[y][x + 1] = curChar
                if x < width - 2 and lines[y][x + 1] == '|' and lines[y][x + 2] == '.':
                    changed = True
                    lines[y][x + 2] = otherChar
                if x < width - 1 and lines[y][x + 1] == otherChar:
                    dump_error(lines, f"{x=}, {y=}, {curChar=} next to {otherChar=}")
                if x < width - 2 and lines[y][x + 1] == '|' and lines[y][x + 2] == curChar:
                    dump_error(lines, f"{x=}, {y=}, {curChar=} across from {curChar=}")
    for y, line in enumerate(lines):
        lines[y] = "".join(line)

def find_start(charMap: list):
    for y, line in enumerate(charMap):
        x = line.find('S')
        if x >= 0:
            return x, y
    return None

def clean_charmap(charMap: list, bitmap: list):
    for y in range(len(charMap)):
        newLine = []
        for x in range(len(charMap[y])):
            if bitmap[y][x]:
                newChar = charMap[y][x]
            else:
                newChar = "."
            newLine.append(newChar)
        charMap[y] = "".join(newLine)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        lines = sample_input.split("\n")
    else:
        with open(sys.argv[1]) as inputfile:
            lines = [line.strip() for line in inputfile.readlines()]

    lines = explode(lines)
    startLoc = find_start(lines)
    print(f"{startLoc=}")
    maxDistance = 0
    goodBitmap = None
    length, bitmap = traverse(lines, startLoc[0] + 1, startLoc[1], *startLoc)
    if length > maxDistance:
        maxDistance = length
        goodBitmap = bitmap
    length, bitmap = traverse(lines, startLoc[0] - 1, startLoc[1], *startLoc)
    if length > maxDistance:
        maxDistance = length
        goodBitmap = bitmap
    length, bitmap = traverse(lines, startLoc[0], startLoc[1] + 1, *startLoc)
    if length > maxDistance:
        maxDistance = length
        goodBitmap = bitmap
    if maxDistance == 0:
        print("No path found")
        exit()
    # No need to check the fourth direction - it would have already been found

    clean_charmap(lines, goodBitmap)
    shade(lines)
    lines = unexplode(lines)

    countDecimals = sum([line.count('.') for line in lines])
    countIs = sum([line.count('I') for line in lines])
    countOs = sum([line.count('O') for line in lines])
    print(f'{countDecimals=}, {countIs=}, {countOs=}')
