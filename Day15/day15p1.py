def prettyPrint(array: list[str]):
    for i in array:
        print("".join(i))


DIRECTIONS = {
    "^": complex(-1, 0),
    ">": complex(0, 1),
    "v": complex(1, 0),
    "<": complex(0, -1),
}

## input
with open("input.txt", "r") as f:
    textIn = f.readlines()

grid = []
instructions = []

coords = None

# parse input
for r, line in enumerate(textIn):
    if line.startswith("#"):
        grid.append(list(line.strip()))
        if not coords:
            index = line.find("@")
            if index != -1:
                coords = complex(r, index)
    elif len(line.split()):
        instructions += list(line.strip())

for instruct in instructions:
    moveTo = coords + DIRECTIONS[instruct]

    # check for obstacle
    obstacle = grid[int(moveTo.real)][int(moveTo.imag)]
    # wall
    if obstacle == "#":
        # don't move
        pass
    # empty
    elif obstacle == ".":
        # swap postions
        grid[int(moveTo.real)][int(moveTo.imag)] = "@"
        grid[int(coords.real)][int(coords.imag)] = "."
        # update coords
        coords = moveTo
    # box
    else:
        currentObs = "O"
        currentObsPos = moveTo
        while currentObs == "O":
            currentObsPos += DIRECTIONS[instruct]
            currentObs = grid[int(currentObsPos.real)][int(currentObsPos.imag)]
        if currentObs == ".":
            # make last space a box
            grid[int(currentObsPos.real)][int(currentObsPos.imag)] = "O"
            # move robot to first space
            grid[int(moveTo.real)][int(moveTo.imag)] = "@"
            grid[int(coords.real)][int(coords.imag)] = "."
            # update coords
            coords = moveTo

total = 0
# get sum of coordinates of boxes:
for r in range(len(grid)):
    for c, v in enumerate(grid[r]):
        if v == "O":
            total += 100 * r + c

print(total)
