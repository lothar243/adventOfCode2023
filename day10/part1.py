import sys

sample_input = """S-7F--7..
|.||.FJ..
|.LJ.L7..
L---7.|..
....L-J..
"""



    # | is a vertical pipe connecting north and south.
    # - is a horizontal pipe connecting east and west.
    # L is a 90-degree bend connecting north and east.
    # J is a 90-degree bend connecting north and west.
    # 7 is a 90-degree bend connecting south and west.
    # F is a 90-degree bend connecting south and east.
    # . is ground; there is no pipe in this tile.
    # S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.


def traverseRecursion(charMap: list, x, y, xFrom, yFrom):
    # print(x, y, xFrom, yFrom)
    width = len(charMap[0])
    height = len(charMap)
    # check for out-of-bounds
    if x < 0 or x >= width or y < 0 or y >= height:
        return -1e99
    char = charMap[y][x]
    if char == 'S':
        return 0
    if x - xFrom == 1:
        # Coming from the left
        if char == '-':
            return traverse(charMap, x + 1, y, x, y) + 1
        elif char == 'J':
            return traverse(charMap, x, y - 1, x, y) + 1
        elif char == '7':
            return traverse(charMap, x, y + 1, x, y) + 1
        else:
            return -1e98
    elif x - xFrom == -1:
        # coming from the right
        if char == '-':
            return traverse(charMap, x - 1, y, x, y) + 1
        elif char == 'L':
            return traverse(charMap, x, y - 1, x, y) + 1
        elif char == 'F':
            return traverse(charMap, x, y + 1, x, y) + 1
        else:
            return -1e97
    elif y - yFrom == 1:
        # coming from above
        if char == '|':
            return traverse(charMap, x, y + 1, x, y) + 1
        elif char == 'L':
            return traverse(charMap, x + 1, y, x, y) + 1
        elif char == 'J':
            return traverse(charMap, x - 1, y, x, y) + 1
        else:
            return -1e96
    elif y - yFrom == -1:
        # coming from below
        if char == '|':
            return traverse(charMap, x, y - 1, x, y) + 1
        elif char == '7':
            return traverse(charMap, x - 1, y, x, y) + 1
        elif char == 'F':
            return traverse(charMap, x + 1, y, x, y) + 1
        else:
            return -1e95

def traverse(charMap: list, x, y, xFrom, yFrom):
    # print(x, y, xFrom, yFrom)
    width = len(charMap[0])
    height = len(charMap)
    length = 0
    # check for out-of-bounds
    if x < 0 or x >= width or y < 0 or y >= height:
        return -1e99

    char = charMap[y][x]
    while(char != 'S'):
        # check for out-of-bounds
        if x < 0 or x >= width or y < 0 or y >= height:
            return -1e99
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
                return -1e98
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
                return -1e97
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
                return -1e96
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
                return -1e95
        char = charMap[y][x]
    return length


def find_start(charMap: list):
    for y, line in enumerate(charMap):
        x = line.find('S')
        if x >= 0:
            return x, y
    return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        lines = sample_input.split("\n")
    else:
        with open(sys.argv[1]) as inputfile:
            lines = [line.strip() for line in inputfile.readlines()]

    startLoc = find_start(lines)
    distances = []
    distances.append(traverse(lines, startLoc[0] + 1, startLoc[1], *startLoc))
    distances.append(traverse(lines, startLoc[0] - 1, startLoc[1], *startLoc))
    distances.append(traverse(lines, startLoc[0], startLoc[1] + 1, *startLoc))
    distances.append(traverse(lines, startLoc[0], startLoc[1] - 1, *startLoc))
    print(distances)
    print((max(distances) + 1) // 2)