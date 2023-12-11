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

def find_empty_parts(lines: list):
    "Doubles any row or column in which there are no galaxies"
    # starting with columns
    width = len(lines[0])
    height = len(lines)
    emptyColumns = []
    for x in range(width):
        column = [line[x] for line in lines]
        doubleUp = "".join(column).find('#') == -1
        if doubleUp:
            emptyColumns.append(x)
    emptyRows = []
    for y in range(height):
        if lines[y].find('#') == -1:
            emptyRows.append(y)
    return emptyRows, emptyColumns
    
def manhattan_distance(location1, location2, emptyRows, emptyColumns, expansionMultiple):
    baseDistance = abs(location1[0] - location2[0]) + abs(location1[1] - location2[1])
    minX = min(location1[0], location2[0])
    maxX = max(location1[0], location2[0])
    minY = min(location1[1], location2[1])
    maxY = max(location1[1], location2[1])
    numHorizontalExpansions = len([colNum for colNum in emptyColumns if minX < colNum < maxX])
    numVerticalExpansions = len([rowNum for rowNum in emptyRows if minY < rowNum < maxY])
    return baseDistance + (numHorizontalExpansions + numVerticalExpansions) * (expansionMultiple - 1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        lines = sample_input.split("\n")
    else:
        with open(sys.argv[1]) as inputfile:
            lines = [line.strip() for line in inputfile.readlines()]

    emptyRows, emptyColumns = find_empty_parts(lines)

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
    for i, galaxy1 in enumerate(galaxies):
        for j, galaxy2 in enumerate(galaxies):
            if i != j:
                connection = (manhattan_distance(galaxy1, galaxy2, emptyRows, emptyColumns, 1000000), galaxy1, galaxy2)
                heapq.heappush(connections, connection)
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