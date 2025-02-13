def prettyPrint(array: list[str]):
    for i in array:
        print("".join(i))


def checkBrokenBox(grid):
    for line in grid:
        stringified = "".join(line)
        if (
            "[." in stringified
            or ".]" in stringified
            or "]]" in stringified
            or "[[" in stringified
        ):
            return True


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
        currentLine = []
        for c, v in enumerate(line.strip()):

            if v == "#":
                currentLine += ["#", "#"]
            elif v == ".":
                currentLine += [".", "."]
            elif v == "O":
                currentLine += ["[", "]"]
            else:
                currentLine += ["@", "."]
                coords = complex(r, c * 2)
        grid.append(currentLine)
    elif len(line.split()):
        instructions += list(line.strip())

count = 0
for instruct in instructions:
    count += 1
    moveTo = coords + DIRECTIONS[instruct]

    # check for obstacle
    obstacle = grid[int(moveTo.real)][int(moveTo.imag)]
    # wall
    if obstacle == "#":
        # don't move
        continue
    # empty
    elif obstacle == ".":
        # swap postions
        grid[int(moveTo.real)][int(moveTo.imag)] = "@"
        grid[int(coords.real)][int(coords.imag)] = "."
        # update coords
        coords = moveTo
    # box
    elif instruct == ">" or instruct == "<":
        # horizontal
        currentObs = grid[int(moveTo.real)][int(moveTo.imag)]
        currentObsPos = moveTo
        boxStack = [coords, currentObsPos]
        while currentObs == "[" or currentObs == "]":
            currentObsPos += DIRECTIONS[instruct]
            currentObs = grid[int(currentObsPos.real)][int(currentObsPos.imag)]
            boxStack.append(currentObsPos)
        if currentObs == ".":
            # swap everthing in stack
            for i in range(len(boxStack) - 1, 0, -1):
                grid[int(boxStack[i].real)][int(boxStack[i].imag)] = grid[
                    int(boxStack[i - 1].real)
                ][int(boxStack[i - 1].imag)]
            grid[int(coords.real)][int(coords.imag)] = "."
            # update coords
            coords = moveTo
    else:
        # verical
        visited = {coords}
        boxes = {coords: "@"}
        toVisit = {moveTo}
        currentObsPos = None
        willMove = True
        while len(toVisit):
            currentObsPos = toVisit.pop()
            if currentObsPos in visited:
                continue
            otherHalfPos = None
            # wall
            if grid[int(currentObsPos.real)][int(currentObsPos.imag)] == "#":
                willMove = False
                break
            elif grid[int(currentObsPos.real)][int(currentObsPos.imag)] == ".":
                continue
            # left box [
            elif grid[int(currentObsPos.real)][int(currentObsPos.imag)] == "[":
                otherHalfPos = currentObsPos + DIRECTIONS[">"]
            # right box ]
            elif grid[int(currentObsPos.real)][int(currentObsPos.imag)] == "]":
                otherHalfPos = currentObsPos + DIRECTIONS["<"]

            boxes[currentObsPos] = grid[int(currentObsPos.real)][
                int(currentObsPos.imag)
            ]

            # add side and up
            visited.add(currentObsPos)
            upDownPos = currentObsPos + DIRECTIONS[instruct]
            toVisit.add(upDownPos)
            toVisit.add(otherHalfPos)

        # valid move
        if willMove:
            # clear everything
            for pos in boxes:
                grid[int(pos.real)][int(pos.imag)] = "."

            for pos in boxes:
                newPos = pos + DIRECTIONS[instruct]
                grid[int(newPos.real)][int(newPos.imag)] = boxes[pos]

            coords = moveTo

total = 0
# get sum of coordinates of boxes:
for r in range(len(grid)):
    for c, v in enumerate(grid[r]):
        if v == "[":
            total += 100 * r + c

print(total)
