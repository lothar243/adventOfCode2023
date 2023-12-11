import sys

sample_input = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

def expand_galaxy(lines: list):
    "Doubles any row or column in which there are no galaxies"
    # starting with columns
    width = len(lines[0])
    height = len(lines)

    expandedHorizontal = [[] for _ in range(height)]
    for x in range(width):
        column = [line[x] for line in lines]
        doubleUp = "".join(column).find('#') == -1
        for y in range(height):
            expandedHorizontal[y].append(lines[y][x])
            if doubleUp:
                expandedHorizontal[y].append(lines[y][x])
    outputLines = []
    for y in range(height):
        joinedLine = "".join(expandedHorizontal[y])
        outputLines.append(joinedLine)
        if joinedLine.find('#') == -1:
            outputLines.append(joinedLine)
    return outputLines
    

if __name__ == "__main__":
    if len(sys.argv) < 2:
        lines = sample_input.split("\n")
    else:
        with open(sys.argv[1]) as inputfile:
            lines = [line.strip() for line in inputfile.readlines()]

    lines = expand_galaxy(lines)

    galaxies = []
    for y, line in enumerate(lines):
        startingX = 0
        while True:
            galX = line.find('#', startingX)
            if galX == -1:
                break
            else:
                startingX = galX + 1
                galaxies.append((galX, y))
    print(galaxies)