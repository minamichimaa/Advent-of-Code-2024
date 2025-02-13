from typing import TypeAlias, Literal


def prettyPrint(array: list[str]):
    for i in array:
        print(i.strip())


## input
with open("input.txt", "r") as f:
    textIn = f.readlines()

grid: list[str] = [x.strip() for x in textIn]

Direction: TypeAlias = Literal["up", "right", "down", "left"]
Coordinate: TypeAlias = tuple[int, int]

# directions and their offset
DIRECTIONS: dict[Direction, tuple[int, int]] = {
    "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0),
    "left": (0, -1),
}
DIRKEYS = tuple(DIRECTIONS.keys())


def moveDirection(
    field: list[list[str]], direction: Direction, position: Coordinate
) -> tuple[set[Coordinate], Coordinate, bool]:
    currPos = position
    visited = {position}
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

# do movement
facing = 0
visited: set[Coordinate] = {(rowGuard, colGuard)}

while True:
    # move
    newVisted, newPos, didExit = moveDirection(
        grid, DIRKEYS[facing], (rowGuard, colGuard)
    )

    # update visited
    visited.update(newVisted)
    rowGuard, colGuard = newPos

    # check if out of bounds
    if didExit:
        break

    # rotate
    facing = (facing + 1) % 4

print(len(visited))
