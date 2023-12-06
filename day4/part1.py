import sys

sample_input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

def readCard(lineString):
    "Reads in a line and returns a tuple of (cardNum, list1, list2)"
    cardString, listStrings = lineString.split(":")
    list1String, list2String = listStrings.split("|")
    cardNum = int(cardString[5:])
    list1 = [int(val.strip()) for val in list1String.split()]
    list2 = [int(val.strip()) for val in list2String.split()]
    return cardNum, list1, list2

def numberMatching(set1: set, set2: set):
    return len(set1.intersection(set2))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        lines = sample_input.split("\n")
    else:
        with open(sys.argv[1]) as inputfile:
            lines = [line.strip() for line in inputfile.readlines()]
    
    sum = 0
    for line in lines:
        cardNum, list1, list2 = readCard(line)
        matches = numberMatching(set(list1), set(list2))
        if matches == 0:
            continue
        else:
            sum += 2 ** (matches - 1)

    print(sum)