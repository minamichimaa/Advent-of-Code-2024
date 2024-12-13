import copy

def prettyPrint(array: list[str]):
    for i in array:
        print(i.strip())

def getSideCoordinates(coordinate: tuple[int, int], direction: str) -> list[tuple[int, int, str]]:
    r,c = coordinate

    directionDict = {
        'up': 0,
        'right': 1,
        'down': 2,
        'left': 3
    }

    newCoords = [
        (r-1, c),     # up 
        (r, c+1),  # right 
        (r+1,c),    # down 
        (r, c-1)    # left
    ]

    i = directionDict[direction]

    return [newCoords[(i + 1) % 4], newCoords[(i + 3) % 4]]

def getAdjacentCoordinatesWithDirections(coordinate: tuple[int, int], directions: list[str] = ['up', 'right' ,'down' ,'left']) -> dict[tuple[int, int], str]:
    r,c = coordinate

    newCoords = {
        (r-1,c): 'up',      # up 
        (r,c+1): 'right',   # right 
        (r+1,c): 'down',    # down 
        (r,c-1): 'left'     # left
    }

    return newCoords

def getValidAdjacentCoordinates(farm: list[str], coordinate: tuple[int, int]) -> list[tuple[int, int]]:
    r,c = coordinate
    flowerType = farm[r][c]

    newCoords = [
        (r-1,c),    # up 
        (r,c+1),    # right 
        (r+1,c),    # down 
        (r,c-1)     # left
    ]

    valid: list[tuple[int, int]] = []

    for coord in newCoords:
        if 0 <= coord[0] < len(farm) and 0 <= coord[1] < len(farm[1]) and farm[coord[0]][coord[1]] == flowerType:
            valid.append(coord)

    return valid

def overwriteValue(dictionary: dict, oldValue: int, newValue: int) -> dict:
    newDict = copy.deepcopy(dictionary)
    for k, v in newDict.items():
        if v == oldValue:
            dictionary[k] = newValue
    
    return newDict

## input
with open("input.txt", 'r') as f:
    textIn = f.readlines()
    
farm = [x.strip() for x in textIn]

visited = set()
queue = []

for r in range(len(farm)-1, -1, -1):
    for c in range(len(farm[r])-1, -1, -1):
        queue.append((r, c))

cost = 0

currentCount = 0
currentSideId = 0
regionQueue = []
sidesDictionary = {}
idSet = set()

while True:
    # prioritize region queue
    if len(regionQueue):
        currentFlower = regionQueue.pop()
    # nothing in region queue 
    else:
        # calulate cost
        cost += currentCount * len(idSet)
        currentCount = currentSideId = 0
        sidesDictionary = {}
        idSet = set()
        # get from queue
        if len(queue):
            currentFlower = queue.pop()
        else:
            break

    # skip current if visited
    if currentFlower in visited:
        continue
    visited.add(currentFlower)

    # add adjacent to beginning if not in visited
    adjacentCoords = getAdjacentCoordinatesWithDirections(currentFlower)
    validAdjacentCoords = getValidAdjacentCoordinates(farm, currentFlower)

    # get sides coorinates
    sidesCoords = set(adjacentCoords.keys()) - set(validAdjacentCoords)
    # check for side-fence
    for side in sidesCoords:
        facing = adjacentCoords[side]
        
        # check adjacent of side for existing side
        foundSideOfSide = None
        sideOfSides = getSideCoordinates(side, facing)

        for pos in sideOfSides:
            # found
            if (pos, facing) in sidesDictionary:
                # only 1 side found
                if foundSideOfSide == None:
                    foundSideOfSide = (pos, facing)
                # found 2 sides
                else:
                    sideSide1 = sidesDictionary[foundSideOfSide]
                    sideSide2 = sidesDictionary[(pos, facing)]

                    # side ids don't match
                    if sideSide1 != sideSide2:
                        small = min(sideSide1, sideSide2)
                        large = max(sideSide1, sideSide2)
                        # overwrite all larger id
                        sidesDictionary = overwriteValue(sidesDictionary, large, small)
                        # remove all larger id from set
                        idSet.remove(large)

        # side found
        if foundSideOfSide:
            # copy side id
            sidesDictionary[(side, facing)] = sidesDictionary[foundSideOfSide]
        # side not found
        else:
            # make new id
            currentSideId += 1
            idSet.add(currentSideId)
            sidesDictionary[(side, facing)] = currentSideId

    # add valid adjacent to beginning if not in visited
    for coord in validAdjacentCoords:
        if coord not in visited:
            regionQueue.append(coord)

    # add count and sides
    currentCount += 1
    
print(cost)