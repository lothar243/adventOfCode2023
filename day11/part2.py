import sys
import heapq

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
    expandedColumns = []
    expandedRows = []
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
    
def manhattan_distance(location1, location2, expandedRows, expandedColumns, expansionMultiple):
    baseDistance = abs(location1[0] - location2[0]) + abs(location1[1] - location2[1])
    horizontalRange = range(min(location1[0], location2[0]))
    numHorizontalExpansions = len([])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        lines = sample_input.split("\n")
    else:
        with open(sys.argv[1]) as inputfile:
            lines = [line.strip() for line in inputfile.readlines()]

    lines = expand_galaxy(lines)

    # for line in lines:
    #     print(line)

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
    
    # add all the inter-galaxy connections
    totalDistance = 0
    connections = []
    for galaxy1 in galaxies:
        for galaxy2 in galaxies:
            if galaxy1 != galaxy2:
                heapq.heappush(connections, (manhattan_distance(galaxy1, galaxy2), galaxy1, galaxy2))
    connectedGalaxies = set()
    while len(connections) > 0:
        distance, galaxy1, galaxy2 = heapq.heappop(connections)
        # if galaxy1 not in connectedGalaxies or galaxy2 not in connectedGalaxies:
        if True:
            connectedGalaxies.add(galaxy1)
            connectedGalaxies.add(galaxy2)
            totalDistance += distance
            #print(distance, galaxy1, galaxy2)
    #print(galaxies)
    print(totalDistance / 2)