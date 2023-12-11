import sys

def dump_error(lines: list, message: str):
    print(message)
    dumplines = []
    for line in lines:
        dumplines.append("".join(line))
    with open ('errorOutput', 'w') as outputfile:
        outputfile.write(message + "\n")
        outputfile.write("\n".join(dumplines))
    exit()

with open (sys.argv[1]) as inputfile:
    lines = [line.strip() for line in inputfile.readlines()]

for i, line in enumerate(lines):
    lines[i] = [char for char in line]

print(lines)

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



for line in lines:
    print("".join(line))


countDecimals = sum([line.count('.') for line in lines])
countIs = sum([line.count('I') for line in lines])
countOs = sum([line.count('O') for line in lines])
print(f'{countDecimals=}, {countIs=}, {countOs=}')

with open (sys.argv[2], 'w') as outputfile:
    for y, line in enumerate(lines):
        lines[y] = "".join(line)
    outputfile.write('\n'.join(lines))
