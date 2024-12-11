def prettyPrint(array: list):
    for i in array:
        print(i.strip())

def getValidAdjacentCoordinates(daMap, coordinate):
    r,c = coordinate

    newCoord = [
        (r-1,c),    # top 
        (r,c+1),    # right 
        (r+1,c),    # down 
        (r,c-1)     # left
    ]

    valid = []

    for coord in newCoord:
        if 0 <= coord[0] < len(daMap) and 0 <= coord[1] < len(daMap[1]) and daMap[coord[0]][coord[1]] != '.':
            valid.append(coord)

    return valid

## input
with open("input.txt", 'r') as f:
    textIn = f.readlines()
    
prettyPrint(textIn)

topMap = [x.strip() for x in textIn]

trailStarts = []
# get coordinates of start of trail (0)
for r, x in enumerate(topMap):
    for c, y in enumerate(x):
        if y == '0':
            trailStarts.append((r,c))

# go through each starting position
totalRatings = 0
for start in trailStarts:
    queue = [(*start, 0)]

    ratings = 0

    # until no more unvisited
    while len(queue):
        # pop queue
        currentPos = queue.pop()

        # found peak then add 1 to rating 
        if currentPos[2] == 9:
            ratings += 1
            continue

        # get sides
        adjacentCoords = getValidAdjacentCoordinates(topMap, currentPos[:2])

        for coords in adjacentCoords:
            # 1 higher than current height
            if int(topMap[coords[0]][coords[1]]) == currentPos[2]+1:
                # add to queue
                queue.append((*coords, currentPos[2]+1))

    totalRatings += ratings

print(totalRatings)