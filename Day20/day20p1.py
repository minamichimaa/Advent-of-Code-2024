from collections import defaultdict
from itertools import combinations

def prettyPrint(array: list[str]):
    for i in array:
        print(i)

def getValidAdjacentCoordinates(grid: list[str], coordinate: tuple[int, int]) -> list[tuple[int, int]]:
    r,c = coordinate

    newCoord = [
        (r-1,c),    # top 
        (r,c+1),    # right 
        (r+1,c),    # down 
        (r,c-1)     # left
    ]

    valid: list[tuple[int, int]] = []

    for coord in newCoord:
        if grid[coord[0]][coord[1]] != '#':
            valid.append(coord)

    return valid

def distanceBetween(coord1: tuple[int, int], coord2: tuple[int, int]) -> int:
    a, b = coord1
    c, d = coord2
    
    distance = abs(a-c) + abs(b-d)
    return distance

## input
with open("input.txt", 'r') as f:
    textIn = f.readlines()

grid = []

# parse
startPos = None
endPos = None

for r, line in enumerate(textIn):
    currLine = line.strip()
    newLine = []
    for c, v in enumerate(currLine):
        newLine.append(v)
        if v == 'S':
            startPos = (r, c)
        if v == 'E':
            endPos = (r, c)
    grid.append(newLine)

# initialize algorithm
distanceFromStart = {startPos: 0}
currDist = 0
currPos = startPos

# run until found shortest path
while True:
    # found end
    if currPos == endPos:
        break
    # not end yet
    # get next
    adjacents = getValidAdjacentCoordinates(grid, currPos)
    for adjPos in adjacents:
        # is the next position
        if adjPos not in distanceFromStart:
            # add distance to next
            distanceFromStart[adjPos] = currDist + 1
            currDist = distanceFromStart[adjPos]
            currPos = adjPos

distanceFromEnd = {x:(distanceFromStart[endPos] - distanceFromStart[x]) for x in distanceFromStart}

# get all combinations of point to point
combos = combinations(distanceFromStart.keys(), 2)
# filter only ones where distance is acceptable
distanceFromPoints = {}
maxDistance = 2

for i, j in combos:
    if (dist := distanceBetween(i, j)) <= maxDistance:
        distanceFromPoints[(i, j)] = dist

# calculate distance from start to end using the shortcut
lengthCount = defaultdict(int)

for combo, dist in distanceFromPoints.items():
    i, j = combo
    runDist = distanceFromStart[i] + dist + distanceFromEnd[j]
    lengthCount[runDist] += 1

# count the number of time saved
originalLength = distanceFromStart[endPos]
minPicoSecondsSaved = 100
count = 0
for i in lengthCount:
    if originalLength - i >= minPicoSecondsSaved:
        count += lengthCount[i]

print(count)