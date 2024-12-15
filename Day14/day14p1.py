import re

from functools import reduce

def prettyPrint(array: list[str]):
    for i in array:
        print(i)

def complexModulo(cNum:complex, mod:complex) -> complex:
    realModulo = cNum.real % mod.real
    imagModulo = cNum.imag % mod.imag
    return complex(realModulo, imagModulo)

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
time = 100

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

# count quadrants
halfWidth = (width // 2)
halfHeight = (height // 2)
quadCount = [0, 0, 0, 0]
for rob in robots:
    # quadrant 1
    if rob[0].real < halfWidth and rob[0].imag < halfHeight:
        quadCount[0] += 1
    # quadrant 2
    elif rob[0].real > halfWidth and rob[0].imag < halfHeight:
        quadCount[1] += 1
    # quadrant 3
    elif rob[0].real < halfWidth and rob[0].imag > halfHeight:
        quadCount[2] += 1
    # quadrant 4
    elif rob[0].real > halfWidth and rob[0].imag > halfHeight:
        quadCount[3] += 1

# calculate safety factor
print(reduce(lambda x, y: x*y, quadCount, 1))
