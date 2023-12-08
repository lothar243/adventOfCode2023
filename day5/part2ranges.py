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

def sort_list_of_ranges(list_of_ranges: list):
    indexList = list(range(len(list_of_ranges)))
    list_of_ranges.sort(key=lambda range: range['start'])

def fill_in_ranges(list_of_ranges: list):
    sort_list_of_ranges(list_of_ranges)
    new_ranges = []
    if list_of_ranges[0]['start'] > 0:
        new_ranges.append({'start': 0, 'destination': 0, 'rangeLength': list_of_ranges[0]['start']})
    for rangeIndex in range(1, len(list_of_ranges)):
        previousRangeEnd = list_of_ranges[rangeIndex - 1]['start'] + list_of_ranges[rangeIndex - 1]['rangeLength']
        if list_of_ranges[rangeIndex - 1]['start'] + list_of_ranges[rangeIndex - 1]['rangeLength'] < list_of_ranges[rangeIndex]['start']:
            lengthOfNewRange = list_of_ranges[rangeIndex]['start'] - previousRangeEnd
            new_ranges.append({'start': previousRangeEnd, 'destination': previousRangeEnd, 'rangeLength': lengthOfNewRange})
    previousRangeEnd = list_of_ranges[-1]['start'] + list_of_ranges[-1]['rangeLength']
    new_ranges.append({'start': previousRangeEnd, 'destination': previousRangeEnd, 'rangeLength': 9999999999999999})
    list_of_ranges.extend(new_ranges)
    sort_list_of_ranges(list_of_ranges)

def convert_ranges(inputRanges: list, list_of_ranges: list):
    outputRanges = []
    for i in range(0, len(inputRanges), 2):
        outputRanges.extend(convert_range(inputRanges[i], inputRanges[i+1], list_of_ranges))
    return outputRanges

def convert_range(inputStart: int, numInputs: int, list_of_ranges: list):
    seedsLeft = True
    numberAfterLastSeed = inputStart + numInputs
    rangeIndex = 0
    outputRanges = []
    while inputStart >= list_of_ranges[rangeIndex]['start'] + list_of_ranges[rangeIndex]['rangeLength']:
        rangeIndex += 1
    while seedsLeft:
        rangeStart = list_of_ranges[rangeIndex]['start']
        rangeDestination = list_of_ranges[rangeIndex]['destination']
        rangeLength = list_of_ranges[rangeIndex]['rangeLength']
        nextRangeStart = rangeStart + rangeLength
        if numberAfterLastSeed > nextRangeStart:
            # need to move on to next range
            outputRanges.extend([inputStart - rangeStart + rangeDestination, nextRangeStart - inputStart])
            rangeIndex += 1
            inputStart = nextRangeStart
        else:
            # the last seed is in the current range
            outputRanges.extend([inputStart - rangeStart + rangeDestination, numberAfterLastSeed - inputStart])
            break
    return outputRanges

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
    fill_in_ranges(seed_to_soil)
    soil_ranges = convert_ranges(seedRanges, seed_to_soil)

    soil_to_fertilizer, currentline = readmap("soil-to-fertilizer map:", lines, currentline + 1)
    fill_in_ranges(soil_to_fertilizer)
    fertilizer_ranges = convert_ranges(soil_ranges, soil_to_fertilizer)

    fertilizer_to_water, currentline = readmap("fertilizer-to-water map:", lines, currentline + 1)
    fill_in_ranges(fertilizer_to_water)
    water_ranges = convert_ranges(fertilizer_ranges, fertilizer_to_water)

    water_to_light, currentline = readmap("water-to-light map:", lines, currentline + 1)
    fill_in_ranges(water_to_light)
    light_ranges = convert_ranges(water_ranges, water_to_light)

    light_to_temperature, currentline = readmap("light-to-temperature map:", lines, currentline + 1)
    fill_in_ranges(light_to_temperature)
    temperature_ranges = convert_ranges(light_ranges, light_to_temperature)

    temperature_to_humidity, currentline = readmap("temperature-to-humidity map:", lines, currentline + 1)
    fill_in_ranges(temperature_to_humidity)
    humidity_ranges = convert_ranges(temperature_ranges, temperature_to_humidity)

    humidity_to_location, currentline = readmap("humidity-to-location map:", lines, currentline + 1)
    fill_in_ranges(humidity_to_location)
    location_ranges = convert_ranges(humidity_ranges, humidity_to_location)

    minLocation = min([location for i, location in enumerate(location_ranges) if i % 2 == 0])
    print(minLocation)
    


