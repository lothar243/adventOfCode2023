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

if __name__ == "__main__":
    if len(sys.argv) < 2:
        lines = sample_input2.split("\n")
    else:
        with open(sys.argv[1]) as inputfile:
            lines = [line.strip() for line in inputfile.readlines()]

    leftRight = lines[0]
    instructions = {}
    for line in lines[2:]:
        start, dest = line[:-1].split(" = (")
        dest1, dest2 = dest.split(", ")
        instructions[start] = dest1, dest2
    
    currentLocation = 'AAA'
    leftRightNumber = 0
    numSteps = 0
    while(currentLocation != 'ZZZ'):
        # print(currentLocation)
        if leftRight[leftRightNumber] == 'L':
            currentLocation = instructions[currentLocation][0]
        else:
            currentLocation = instructions[currentLocation][1]
        numSteps += 1
        leftRightNumber = (leftRightNumber + 1) % len(leftRight)
    print(currentLocation, numSteps)