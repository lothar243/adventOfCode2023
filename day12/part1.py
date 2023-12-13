import sys
from itertools import permutations

sample_input2 = """#.#.### 1,1,3
.#...#....###. 1,1,3
.#.###.#.###### 1,3,1,6
####.#...#... 4,1,1
#....######..#####. 1,6,5
.###.##....# 3,2,1"""

sample_input = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
?#??????????????#?? 5,5"""

def read_groups(pattern: list):
    inBroken = False  # True when index is going through broken springs
    numBroken = 0
    brokenList = []
    for i, char in enumerate(pattern):
        if inBroken:
            if char == '#':
                numBroken += 1
            else:
                brokenList.append(numBroken)
                inBroken = False
        else:
            if char == '#':
                numBroken = 1
                inBroken = True
    if inBroken:
        brokenList.append(numBroken)
    return brokenList

def clean_up(pattern: list, brokenNums: list):
    changed = True
    while changed == True and len(pattern) > 0:
        changed = False
        # remove unnecessary characters
        while pattern[0] == ".":
            pattern.pop(0)
        while pattern[-1] == ".":
            pattern.pop(-1)
        # if the pattern begins or ends with a '#', this tells us quite a bit
        if pattern[0] == "#":
            for i in range(brokenNums[0] + 1):
                pattern.pop(0)
            brokenNums.pop(0)
            changed = True
        if pattern[-1] == '#':
            for i in range(brokenNums[-1] + 1):
                pattern.pop(-1)
            brokenNums.pop(-1)
            changed = True
        # look for other parts that must be '#', based on them being close to the edge
        if '#' in pattern[:brokenNums[0] - 1]:
            encounteredFirstBroken = False
            for i in range(brokenNums[0]):
                if encounteredFirstBroken and pattern[i] != '#':
                    pattern[i] = '#'
                    changed = True
                else:
                    if pattern[i] == '#':
                        encounteredFirstBroken = True
        if '#' in pattern[-brokenNums[-1] + 1:]:
            encounteredFirstBroken = False
            for i in range(-1, -brokenNums[-1] - 1, -1):
                if encounteredFirstBroken and pattern[i] != '#':
                    pattern[i] = '#'
                    changed = True
                else:
                    if pattern[i] == '#':
                        encounteredFirstBroken = True

        # look for other parts that must be '#', based on the total length of the list (compared to brokenNums)

def possible_patterns(pattern: list, brokenNums):
    numUnknown = pattern.count("?")
    numBrokenKnown = pattern.count("#")
    numBrokenUnknown = sum(brokenNums) - numBrokenKnown    
    unknownLocations = [i for i, char in enumerate(pattern) if char == "?"]
    # generate a list of . and # so that the total number of broken springs is correct
    unknownSymbols = '#' * numBrokenUnknown + '.' * (numUnknown - numBrokenUnknown)
    allPossibleUnknowns = set(permutations(unknownSymbols))
    for possibleUnknown in allPossibleUnknowns:
        for i, location in enumerate(unknownLocations):
            pattern[location] = possibleUnknown[i]
        yield pattern


if __name__ == "__main__":
    if len(sys.argv) < 2:
        lines = sample_input.split("\n")
    else:
        with open(sys.argv[1]) as inputfile:
            lines = [line.strip() for line in inputfile.readlines()]
    
    numPossible = 0
    for line in lines:
        springs, brokenNums = line.split(" ")
        brokenNums = [int(val) for val in brokenNums.split(",")]
        springs = [char for char in springs]
        print(f"before cleaning: {springs=}")
        clean_up(springs, brokenNums)
        print(f"after cleaning: {springs=}")
        springsBackup = springs[:]
        for possiblePattern in possible_patterns(springs, brokenNums):
            groupings = read_groups(possiblePattern)
            if groupings == brokenNums:
                numPossible += 1
            

        print(f"{springsBackup=}, {brokenNums=}, {numPossible=}")
    print(numPossible)
