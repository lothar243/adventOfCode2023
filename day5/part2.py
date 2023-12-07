import sys
from datetime import datetime
sample_input = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

def convert_with_map(list_of_ranges: list, inputVal: int):
    for mapping_range in list_of_ranges:
        startVal = mapping_range['start']
        if  startVal <= inputVal <= startVal + mapping_range['rangeLength']:
            return inputVal - startVal + mapping_range['destination']
    return inputVal

def lineString_to_range(lineString):
    values = [int(val) for val in lineString.split()]
    return {'destination': values[0], 'start': values[1], 'rangeLength': values[2]}

def readmap(mapString, lines, currentLineNumber):
    """expects 'mapstring' for the first line, converts lines to ranges until it reaches a blank line
    returns a list of ranges, and the blank line (or -1 for end of list)"""
    try:
        assert lines[currentLineNumber] == mapString
    except:
        print(f"expected {mapString}, encountered {lines[currentLineNumber]}")
    currentLineNumber += 1
    currentLine = lines[currentLineNumber]
    map_ranges = []
    while currentLine != "":
        map_ranges.append(lineString_to_range(currentLine))
        currentLineNumber += 1
        try:
            currentLine = lines[currentLineNumber]
        except:
            currentLine = ""
    return map_ranges, currentLineNumber

def seeds(seedRanges):
    for i in range(0, len(seedRanges), 2):
        for j in range(seedRanges[i + 1]):
            yield seedRanges[0] + j

def calc_num_seeds(seedRanges):
    return sum(seedRanges[1::2])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        lines = sample_input.split("\n")
    else:
        with open(sys.argv[1]) as inputfile:
            lines = [line.strip() for line in inputfile.readlines()]
    
    seedRanges = [int(val) for val in lines[0][6:].split()]
    
    # Read seed-to-soil map
    currentLine = 2
    seed_to_soil, currentline = readmap("seed-to-soil map:", lines, currentLine)
    soil_to_fertilizer, currentline = readmap("soil-to-fertilzer map:", lines, currentline + 1)
    fertilizer_to_water, currentline = readmap("fertilizer-to-water map:", lines, currentline + 1)
    water_to_light, currentline = readmap("water-to-light map:", lines, currentline + 1)
    light_to_temperature, currentline = readmap("light-to-temperature map:", lines, currentline + 1)
    temperature_to_humidity, currentline = readmap("temperature-to-humidity map:", lines, currentline + 1)
    humidity_to_location, currentline = readmap("humidity-to-location map:", lines, currentline + 1)
    
    minLocation = 999999999999999999999
    numSeeds = calc_num_seeds(seedRanges)
    startTime = datetime.now()
    print(f"Total number of seeds: {numSeeds}, starting at {startTime}")
    seedNum = 1
    for seed in seeds(seedRanges):
        soil = convert_with_map(seed_to_soil, seed)
        fertilizer = convert_with_map(soil_to_fertilizer, soil)
        water = convert_with_map(fertilizer_to_water, fertilizer)
        light = convert_with_map(water_to_light, water)
        temperature = convert_with_map(light_to_temperature, light)
        humidity = convert_with_map(temperature_to_humidity, temperature)
        location = convert_with_map(humidity_to_location, humidity)
        # minLocation = min(location, minLocation)
        if location < minLocation:
            minLocation = location
            completion = seedNum / numSeeds
            elapsedTime = datetime.now() - startTime
            predictedTime = elapsedTime / completion
            expectedCompletion = datetime.now() + predictedTime
            print(f"new min location: {minLocation:>16}, {seed=:>16}, Completion={completion * 100:>6.2f}%, expected to be done: {expectedCompletion}")
        seedNum += 1

    print(minLocation)