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

def roll_all_west(field: list):
    height = len(field)
    width = len(field[0])

    for x in range(width):
        for y in range(height):
            if field[y][x] == 'O':
                roll_rock_west(field, x, y)

def roll_rock_west(field: list, x: int, y: int):
    newX = x
    while newX >= 1 and field[y][newX - 1] == '.':
        newX -= 1
    field[y][x] = '.'
    field[y][newX] = 'O'

def roll_all_south(field: list):
    height = len(field)
    width = len(field[0])

    for x in range(width):
        for y in reversed(range(height)):
            if field[y][x] == 'O':
                roll_rock_south(field, x, y)

def roll_rock_south(field: list, x: int, y: int):
    newY = y
    while newY < len(field) - 1 and field[newY + 1][x] == '.':
        newY += 1
    field[y][x] = '.'
    field[newY][x] = 'O'

def roll_all_east(field: list):
    height = len(field)
    width = len(field[0])

    for x in reversed(range(width)):
        for y in range(height):
            if field[y][x] == 'O':
                roll_rock_east(field, x, y)

def roll_rock_east(field: list, x: int, y: int):
    width = len(field[0])
    newX = x
    while newX < width - 1 and field[y][newX + 1] == '.':
        newX += 1
    field[y][x] = '.'
    field[y][newX] = 'O'

def spin_cycle(field):
    roll_all_north(field)
    # print("\nnorth")
    # print_field(field)
    roll_all_west(field)
    # print("\nwest")
    # print_field(field)
    roll_all_south(field)
    # print("\nsouth")
    # print_field(field)
    roll_all_east(field)
    # print("\neast")
    # print_field(field)



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
    print()
    history = dict()
    targetCycle = 1000000000
    targetEquivalent = -1
    modulus = 1
    for cycleNum in range(1, targetCycle):
        spin_cycle(field)
        # print_field(field)
        if cycleNum % 10000000 == 0:
            print(cycleNum)
        cycleHash = hash(tuple(["".join(line) for line in field]))
        # print()
        # print_field(field)
        if cycleHash in history:
            print(f"encountered repeat, {cycleNum=} and {history[cycleHash]=}")
            modulus = cycleNum - history[cycleHash]
            targetEquivalent = targetCycle % modulus
        if cycleNum % modulus == targetEquivalent:
            print("equivalent state found at cycle", cycleNum)
            print_field(field)
            break
        history[cycleHash] = cycleNum
    
    print(calculate_total_load(field))
