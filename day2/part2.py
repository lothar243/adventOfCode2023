import sys
from pprint import pprint

sample_input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""


def splitOnGrabs(multipleGrabStrings):
    "Takes '3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green' and returns a list of color dictionaries"
    grabs = []
    for grabString in multipleGrabStrings.split('; '):
        grabs.append(countCubes(grabString))
    return grabs

def countCubes(grabString):
    "Takes '3 blue, 2 green, 1 red' and returns a dictionary with those values"
    colorStrings = grabString.split(", ")
    colorDictionary = {'red': 0, 'green': 0, 'blue': 0}
    for colorString in colorStrings:
        if "red" in colorString:
            colorDictionary['red'] = int(colorString[:-4])
        elif "green" in colorString:
            colorDictionary['green'] = int(colorString[:-5])
        elif "blue" in colorString:
            colorDictionary['blue'] = int(colorString[:-4])
        else:
            print(f"Unrecognized input: {colorString=}")
    return colorDictionary

def game_possible(colorDictionaries, maxCubes):
    for colorDictionary in colorDictionaries:
        for color, number in maxCubes.items():
            if colorDictionary[color] > number:
                return False
    return True

def min_set_cubes(colorDictionaries):
    minCubes = {'red': 0, 'green': 0, 'blue': 0}
    for colorDictionary in colorDictionaries:
        minCubes['red'] = max(colorDictionary['red'], minCubes['red'])
        minCubes['green'] = max(colorDictionary['green'], minCubes['green'])
        minCubes['blue'] = max(colorDictionary['blue'], minCubes['blue'])
    return minCubes
            

if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        lines = sample_input.split("\n")
    else:
        with open(sys.argv[1]) as inputfile:
            lines = [line.strip() for line in inputfile.readlines()]
    
    
    maxCubes = {'red': 12, 'green': 13, 'blue': 14}

    games = {}
    sum = 0
    # loop for each game
    for line in lines:
        gameString, grabStrings = line.split(": ")
        gameId = int(gameString[5:])
        games[gameId] = splitOnGrabs(grabStrings)
        
        minCubes = min_set_cubes(games[gameId])
        sum += minCubes['red'] * minCubes['blue'] * minCubes['green']

    print(sum)