import sys
sample_input1 = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

sample_input2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

sample_input3 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

def all_end_with_z(currentLocations):
    for currentLocation in currentLocations:
        if not currentLocation.endswith('Z'):
            return False
    return True

def all_empty(startingLocations):
    for startingLocation in startingLocations:
        if startingLocation != '':
            return False
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        lines = sample_input3.split("\n")
    else:
        with open(sys.argv[1]) as inputfile:
            lines = [line.strip() for line in inputfile.readlines()]

    leftRight = lines[0]
    instructions = {}
    for line in lines[2:]:
        start, dest = line[:-1].split(" = (")
        dest1, dest2 = dest.split(", ")
        instructions[start] = dest1, dest2
    
    currentLocations = []
    for instruction in instructions:
        if instruction.endswith('A'):
            currentLocations.append(instruction)
    startingLocations = currentLocations[:]
    print(f"{len(startingLocations)}")
    leftRightNumber = 0
    numSteps = 0
    while(not all_end_with_z(currentLocations)):
        # print(currentLocation)
        if leftRight[leftRightNumber] == 'L':
            for i, currentLocation in enumerate(currentLocations):
                currentLocations[i] = instructions[currentLocation][0]
        else:
            for i, currentLocation in enumerate(currentLocations):
                currentLocations[i] = instructions[currentLocation][1]
        numSteps += 1
        leftRightNumber = (leftRightNumber + 1) % len(leftRight)
        if numSteps % 100000000 == 0:
            print(numSteps)
        # if(leftRightNumber == 0 and numSteps > 0): # detect when there is a cycle
        #     for i, currentLocation in enumerate(currentLocations):
        #         if currentLocation == startingLocations[i]:
        #             print(f"loop detected for {i=}, {numSteps=}")
        #             startingLocations[i] = ''
        #     if(all_empty(startingLocations)):
        #         print("Found all cycles")
        #         exit()
    print(currentLocations, numSteps)