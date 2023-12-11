import sys

"Expands a map so that there are blank spaces"
replacementAboveLine = {
".": "...",
"|": ".|.",
"-": "...",
"L": ".|.",
"J": ".|.",
"7": "...",
"F": "...",
"S": ".-.",

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

if __name__ == "__main__":
    if len(sys.argv) < 2:
        with open("/home/jeff/Documents/adventOfCode2023/day10/out1") as inputfile:
            lines = [line.strip() for line in inputfile.readlines()]
    else:
        with open(sys.argv[1]) as inputfile:
            lines = [line.strip() for line in inputfile.readlines()]

    outputLines = []
    for line in lines:
        aboveLine = [replacementAboveLine[char] for char in line]
        outputLines.append("".join(aboveLine))
        midLine = [replacementSameLine[char] for char in line]
        outputLines.append("".join(midLine))
        bottomLine = [replacementBelowLine[char] for char in line]
        outputLines.append("".join(bottomLine))


    if len(sys.argv) < 3:
        for line in outputLines:
            print(line)
    else:
        with open(sys.argv[2], 'w') as outputfile:
            outputfile.write('\n'.join(outputLines))
