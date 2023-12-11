import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        with open("/home/jeff/Documents/adventOfCode2023/day10/out1-1") as inputfile:
            lines = [line.strip() for line in inputfile.readlines()]
    else:
        with open(sys.argv[1]) as inputfile:
            lines = [line.strip() for line in inputfile.readlines()]

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
    
    countDecimals = sum([line.count('.') for line in outputLines])
    countIs = sum([line.count('I') for line in outputLines])
    countOs = sum([line.count('O') for line in outputLines])
    print(f'{countDecimals=}, {countIs=}, {countOs=}')
