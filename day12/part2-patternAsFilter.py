import sys
from itertools import combinations

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
?###???????? 3,2,1"""

def unfold_springs(pattern: list):
    output = pattern[:]
    for _ in range(4):
        output.append("?")
        output.extend(pattern)
    return output

def unfold_broken_nums(brokenNums: list):
    return brokenNums * 5

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
                try:
                    pattern.pop(0)
                except:
                    pass
            brokenNums.pop(0)
            changed = True
        if len(pattern) > 0 and pattern[-1] == '#':
            for i in range(brokenNums[-1] + 1):
                try:
                    pattern.pop(-1)
                except:
                    pass
            brokenNums.pop(-1)
            changed = True
        # look for other parts that must be '#', based on them being close to the edge
        if len(brokenNums)> 0 and '#' in pattern[:brokenNums[0] - 1]:
            encounteredFirstBroken = False
            for i in range(brokenNums[0]):
                if encounteredFirstBroken and pattern[i] != '#':
                    pattern[i] = '#'
                    changed = True
                else:
                    if pattern[i] == '#':
                        encounteredFirstBroken = True
        if len(brokenNums)> 0 and '#' in pattern[-brokenNums[-1] + 1:]:
            encounteredFirstBroken = False
            for i in range(-1, -brokenNums[-1] - 1, -1):
                if encounteredFirstBroken and pattern[i] != '#':
                    pattern[i] = '#'
                    changed = True
                else:
                    if pattern[i] == '#':
                        encounteredFirstBroken = True

def possible_patterns(pattern: list, brokenNums):
    if len(brokenNums) == 0:
        yield ['.'] * len(pattern)
        return
    numBroken = sum(brokenNums)
    numWorkingSprings = len(pattern) - numBroken
    combs = combinations(range(numWorkingSprings + 1), len(brokenNums))
    for combination in combs:
        possiblePattern = ['.'] * combination[0]
        for i in range(len(brokenNums) - 1):
            possiblePattern.extend(["#"] * brokenNums[i] + ["."] * (combination[i + 1] - combination[i]))
        possiblePattern.extend(['#'] * brokenNums[-1] + ['.'] * (numWorkingSprings - combination[-1]))
        yield possiblePattern



def is_match(pattern, possibleMatch):
    if len(pattern) != len(possibleMatch):
        print("checking match against lists that are different length")
        return False
    for i, patternChar in enumerate(pattern):
        if patternChar == "#" and possibleMatch[i] != '#':
            return False
        if patternChar == "." and possibleMatch[i] != ".":
            return False
    return True



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
        springs = unfold_springs(springs)
        brokenNums = unfold_broken_nums(brokenNums)
        print(f"before cleaning: {''.join(springs)=}, {brokenNums=}")
        clean_up(springs, brokenNums)
        print(f"after cleaning: {''.join(springs)=}, {brokenNums=}")
        springsBackup = springs[:]
        for possiblePattern in possible_patterns(springs, brokenNums):
            #print(f"{possiblePattern=}")
            if is_match(springs, possiblePattern):
                numPossible += 1
            #groupings = read_groups(possiblePattern)
            # print(f"{possiblePattern} showed a grouping of {groupings}")
            #if groupings == brokenNums:
            #    numPossible += 1
            

        print(f"{''.join(springsBackup)=}, {brokenNums=}, {numPossible=}")
    print(numPossible)
