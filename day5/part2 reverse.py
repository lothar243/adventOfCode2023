import sys
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

def convert_with_map_reverse(list_of_ranges: list, inputVal: int):
    for mapping_range in list_of_ranges:
        startVal = mapping_range['destination']
        if  startVal <= inputVal <= startVal + mapping_range['rangeLength']:
            return inputVal - startVal + mapping_range['start']
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

def is_a_seed(seedRange, seedNum):
    for i in range(0, len(seedRanges), 2):
        if seedRange[i] <= seedNum < seedRange[i] + seedRange[i + 1]:
            return True
    return False

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
    soil_to_fertilizer, currentline = readmap("soil-to-fertilizer map:", lines, currentline + 1)
    fertilizer_to_water, currentline = readmap("fertilizer-to-water map:", lines, currentline + 1)
    water_to_light, currentline = readmap("water-to-light map:", lines, currentline + 1)
    light_to_temperature, currentline = readmap("light-to-temperature map:", lines, currentline + 1)
    temperature_to_humidity, currentline = readmap("temperature-to-humidity map:", lines, currentline + 1)
    humidity_to_location, currentline = readmap("humidity-to-location map:", lines, currentline + 1)
    
    seedNum = 1
    for location in range(1, 999999999):
        humidity = convert_with_map_reverse(humidity_to_location, location)
        temperature = convert_with_map_reverse(temperature_to_humidity, humidity)
        light = convert_with_map_reverse(light_to_temperature, temperature)
        water = convert_with_map_reverse(water_to_light, light)
        fertilizer = convert_with_map_reverse(fertilizer_to_water, water)
        soil = convert_with_map_reverse(soil_to_fertilizer, fertilizer)
        seed = convert_with_map_reverse(seed_to_soil, soil)
        if is_a_seed(seedRanges, seed):
            print(location)
            break
        if location % 1000000 == 0:
            print(location)
