def prettyPrint(array: list[str]):
    for i in array:
        print(i.strip())


def getValidAdjacentCoordinates(
    farm: list[str], coordinate: tuple[int, int]
) -> list[tuple[int, int]]:
    r, c = coordinate
    flowerType = farm[r][c]

    newCoord = [
        (r - 1, c),  # top
        (r, c + 1),  # right
        (r + 1, c),  # down
        (r, c - 1),  # left
    ]

    valid: list[tuple[int, int]] = []

    for coord in newCoord:
        if (
            0 <= coord[0] < len(farm)
            and 0 <= coord[1] < len(farm[1])
            and farm[coord[0]][coord[1]] == flowerType
        ):
            valid.append(coord)

    return valid


## input
with open("input.txt", "r") as f:
    textIn = f.readlines()

farm = [x.strip() for x in textIn]

visited = set()
queue = []

for r in range(len(farm) - 1, -1, -1):
    for c in range(len(farm[r]) - 1, -1, -1):
        queue.append((r, c))

cost = 0

currentCount = 0
currentSides = 0
regionQueue = []

while True:
    # prioritize region queue
    if len(regionQueue):
        currentFlower = regionQueue.pop()
    # nothing in region queue
    else:
        # calulate cost
        cost += currentCount * currentSides
        currentCount = currentSides = 0
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
    adjecantCoords = getValidAdjacentCoordinates(farm, currentFlower)
    for coord in adjecantCoords:
        if coord not in visited:
            regionQueue.append(coord)

    # add count and sides
    currentCount += 1
    currentSides += 4 - len(adjecantCoords)

print(cost)
