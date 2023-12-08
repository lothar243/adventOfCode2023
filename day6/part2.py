import sys
sample_input = """Time:      7  15   30
Distance:  9  40  200"""

def read_numbers(timestring: str):
    timestring = timestring.replace(' ', '')
    return [int(val) for val in timestring.split(":") if val != '' and val.isnumeric()]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        lines = sample_input.split("\n")
    else:
        with open(sys.argv[1]) as inputfile:
            lines = [line.strip() for line in inputfile.readlines()]
    times = read_numbers(lines[0])
    distances = read_numbers(lines[1])
    print(times, distances)
    product = 1
    for raceNum in range(len(times)):
        raceTime = times[raceNum]
        numWaysToBeatTarget = 0
        for delayTime in range(1, raceTime):
            if delayTime * (raceTime - delayTime) > distances[raceNum]:
                numWaysToBeatTarget += 1
        product *= numWaysToBeatTarget
    print(product)