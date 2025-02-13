from copy import deepcopy
from ordered_set import OrderedSet
from typing import TypeAlias


def prettyPrint(array: list[str]):
    for i in array:
        print(i.strip())


## input
with open("input.txt", "r") as f:
    textIn = f.readlines()

grid: list[str] = [x.strip() for x in textIn]

Coordinate: TypeAlias = tuple[int, int]

# directions and their offset
DIRECTIONS: dict[str, tuple[int, int]] = {
    "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0),
    "left": (0, -1),
}
DIRKEYS: tuple[str] = tuple(DIRECTIONS.keys())


def moveDirection(
    field: list[list[str]], direction: str, position: Coordinate
) -> tuple[OrderedSet[Coordinate], Coordinate, bool]:
    currPos = position
    visited = OrderedSet()
    visited.add((position))
    exited = False

    while True:
        # move
        nextPos: Coordinate = tuple(map(sum, zip(currPos, DIRECTIONS[direction])))
        # check rows and columns if out of bounds
        if (
            nextPos[0] < 0
            or nextPos[0] == len(field)
            or nextPos[1] < 0
            or nextPos[1] == len(field[0])
        ):
            exited = True
            break

        # check for wall
        if field[nextPos[0]][nextPos[1]] == "#":
            break

        # add visited
        currPos = nextPos
        visited.add(currPos)

    # returns 3 values as a tuple
    # all the positions in the path traveled,
    # the position before the wall or leaving,
    # and if exited the grid or not
    return (visited, currPos, exited)


rowGuard: int | None = None
colGuard: int | None = None

# find guard
for rNum, rVal in enumerate(grid):
    colGuard = rVal.find("^")
    if colGuard != -1:
        rowGuard = rNum
        break

originalGuardPos = (rowGuard, colGuard)

# do movement
facing = 0
visited = OrderedSet()
visited.add((rowGuard, colGuard, facing))

while True:
    # move
    newVisted, newPos, didExit = moveDirection(
        grid, DIRKEYS[facing], (rowGuard, colGuard)
    )

    # update visited
    visited.update((x[0], x[1], facing) for x in newVisted)
    rowGuard, colGuard = newPos

    # check if out of bounds
    if didExit:
        break

    # rotate
    facing = (facing + 1) % 4

validObstructions = set()
for pos in reversed(list(visited)[1:]):
    # make copy of map
    newGrid = deepcopy(grid)
    # put object in position
    newLine: str = newGrid[pos[0]][: pos[1]] + "#" + newGrid[pos[0]][pos[1] + 1 :]
    newGrid[pos[0]] = newLine

    # continue simulation movement
    freshVisited = set()
    simRowGuard, simColGuard = originalGuardPos
    simFacing = 0
    while True:
        # move
        newVisted, newPos, didExit = moveDirection(
            newGrid, DIRKEYS[simFacing], (simRowGuard, simColGuard)
        )

        # check if out of bounds # no loop
        if didExit:
            break

        # check if position is already visited # has loop
        simulatedVisited = set(((x[0], x[1], simFacing) for x in newVisted))
        intersection = freshVisited & simulatedVisited
        if len(intersection):
            validObstructions.add(pos[:2])
            break

        freshVisited.update(simulatedVisited)

        # continue simulation
        simRowGuard, simColGuard = newPos

        # rotate
        simFacing = (simFacing + 1) % 4

print(len(validObstructions))
