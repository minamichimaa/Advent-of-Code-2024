import heapq


def prettyPrint(array: list[str]):
    for i in array:
        print(i)


def getValidAdjacentCoordinates(
    grid: list[str], coordinate: tuple[int, int]
) -> list[tuple[int, int]]:
    c, r = coordinate

    newCoord = [
        (c - 1, r),  # top
        (c, r + 1),  # right
        (c + 1, r),  # down
        (c, r - 1),  # left
    ]

    valid: list[tuple[int, int]] = []

    for coord in newCoord:
        if (
            0 <= coord[1] < len(grid)
            and 0 <= coord[0] < len(grid[1])
            and grid[coord[1]][coord[0]] != "#"
        ):
            valid.append(coord)

    return valid


## input
with open("input.txt", "r") as f:
    textIn = f.readlines()

positions = []
numberFallen = 1024
size = 71
startPos = (0, 0)  # col, row # i hate it
endPos = (size - 1, size - 1)
grid = [["." for x in range(size)] for y in range(size)]

# parse
for line in textIn:
    splits = line.split(",")
    positions.append((int(splits[0]), int(splits[1])))

# create obstructions
for i, pos in enumerate(positions):
    if i == numberFallen:
        break

    c, r = pos
    grid[r][c] = "#"

# go until reach end of input
while numberFallen < len(positions):
    # update next coordinate obstruction
    c, r = positions[numberFallen]
    grid[r][c] = "#"

    # initialize dijkstra algorithm
    distance = {startPos: 0}
    visited = set()
    queue = [(distance[startPos], startPos)]
    heapq.heapify(queue)

    # run until found shortest path
    while len(queue):
        # pop queue
        currDist, pos = heapq.heappop(queue)
        # check if visited
        if pos in visited:
            continue
        else:
            visited.add(pos)

        # update adjacent distances
        adjacents = getValidAdjacentCoordinates(grid, pos)
        for adjPos in adjacents:
            if adjPos not in distance or distance[adjPos] > currDist + 1:
                distance[adjPos] = currDist + 1
            heapq.heappush(queue, (distance[adjPos], adjPos))

    # look for path to exit
    try:
        print(numberFallen, distance[endPos])
    # no path found
    except KeyError:
        print(f"no path found at {numberFallen} with coordinate {c},{r}")
        break
    # path found
    numberFallen += 1
