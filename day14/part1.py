import sys

sample_input = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

def roll_all_north(field: list):
    height = len(field)
    width = len(field[0])

    for x in range(width):
        for y in range(height):
            if field[y][x] == 'O':
                roll_rock_north(field, x, y)

def roll_rock_north(field: list, x: int, y: int):
    newY = y
    while newY >= 1 and field[newY - 1][x] == '.':
        newY -= 1
    field[y][x] = '.'
    field[newY][x] = 'O'

def calculate_total_load(field: list):
    height = len(field)
    totalLoad = 0
    for i, line in enumerate(field):
        totalLoad += line.count('O') * (height - i)
    return totalLoad

def print_field(field: list):
    for line in field:
        print( "".join(line))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        lines = sample_input.split("\n")
    else:
        with open(sys.argv[1]) as inputfile:
            lines = [line.strip() for line in inputfile.readlines()]

    field = []
    for line in lines:
        field.append([char for char in line])
    print_field(field)
    roll_all_north(field)
    print("---------")
    print_field(field)
    print(calculate_total_load(field))