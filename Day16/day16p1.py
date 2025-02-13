import heapq


def prettyPrint(array: list[str]):
    for i in array:
        print(i.strip())


def getAdjacentCoordinates(
    grid: list[list[str]], coordinate: tuple[int, int]
) -> list[tuple[tuple[int, int], str]]:
    r, c = coordinate

    directions = {
        "N": (-1, 0),
        "E": (0, 1),
        "S": (1, 0),
        "W": (0, -1),
    }

    valid = []

    for dir, v in directions.items():
        r1, c1 = v
        r2 = r + r1
        c2 = c + c1
        if grid[r2][c2] != "#":
            valid.append(((r2, c2), dir))

    return valid


## input
with open("input.txt", "r") as f:
    textIn = f.readlines()

grid = [list(x.strip()) for x in textIn]

# starting position and facing direction
startPos = (len(grid) - 2, 1)
endPos = (1, len(grid[1]) - 2)
startFacing = "E"

cost = {startPos: 0}
visited = {startPos}

# to be visted
# heap with key of cost (cost[startPos])
queue = [(cost[startPos], startPos, startFacing)]
heapq.heapify(queue)

# do until every position is visited
while len(queue):
    # visit next position
    costco, pos, facing = heapq.heappop(queue)
    visited.add(pos)

    # get next coordinates
    adjacent = getAdjacentCoordinates(grid, pos)
    for adjPos, adjFacing in adjacent:
        # only unvisited
        if adjPos not in visited:
            # calculate how much it should cost
            calcCost = cost[pos] + (1 if adjFacing == facing else 1001)
            # check if cost already exists and if lower
            if adjPos not in cost or cost[adjPos] > calcCost:
                cost[adjPos] = calcCost
            # add new positions
            heapq.heappush(queue, (cost[adjPos], adjPos, adjFacing))

print(cost[endPos])
