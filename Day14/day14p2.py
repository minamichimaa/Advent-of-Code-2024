import re

def prettyPrint(array: list[str]):
    for i in array:
        print(i)

def prettyPrintGrid(grid: list[list[str]]):
    for line in grid:
        print(''.join(line))

def complexModulo(cNum:complex, mod:complex) -> complex:
    realModulo = cNum.real % mod.real
    imagModulo = cNum.imag % mod.imag
    return complex(realModulo, imagModulo)

def robotsAsGrid(robots:list[list[complex, complex]], width: int, height: int) -> list[list[str]]:
    newGrid = [['.' for x in range(width)] for y in range(height)] 

    for rob in robots:
        col = int(rob[0].real)
        row = int(rob[0].imag)
        newGrid[row][col] = '#'

    return newGrid

def gridAsStr(grid:list[list[str]]) -> str:
    stringList = []

    for line in grid:
        stringList.append(''.join(line))
    
    return '\n'.join(stringList)

regex = re.compile(r'p=(\-?[0-9]+),(\-?[0-9]+) v=(\-?[0-9]+),(\-?[0-9]+)')

## input
with open("input.txt", 'r') as f:
    textIn = f.readlines()

# parse data
robots = []
for line in textIn:
    # get nums
    nums = regex.findall(line)

    coords = complex(int(nums[0][0]), int(nums[0][1]))
    vel = complex(int(nums[0][2]), int(nums[0][3]))

    robots.append([coords, vel])

# initalized robot simulation
width = 101
height = 103
complexGrid = complex(width, height)
time = 100000

# simulate robots
for sec in range(time):
    # do each robot
    for rob in robots:
        # move
        newCoords = rob[0] + rob[1]
        # calulate teleport (if off screen)
        newCoordsMod = complexModulo(newCoords, complexGrid)
        # update
        rob[0] = newCoordsMod
    
    # look for border of tree
    if (sec - 22) % 101 == 0 or (sec - 88) % 103 == 0:
        grid = robotsAsGrid(robots, width, height)
        gridStr = gridAsStr(grid)
        if '###############################' in gridStr:
            print(f'found tree on {sec+1}')
            print(gridStr)

            break
