from typing import TypeAlias, Literal

def prettyPrint(array: list[str]):
    for i in array:
        print(i.strip())

## input
with open("input.txt", 'r') as f:
    textIn = f.readlines()
    
graph: list[str] = [x.strip() for x in textIn]

Direction: TypeAlias = Literal['up', 'right', 'down', 'left']
Point: TypeAlias = tuple[int, int]

def moveDirection(field: list[list[str]], direction: Direction, position: Point) -> tuple[list[Point], Point, bool]:
    currPos = position
    visited = [position]
    exited = False

    dirs: dict[str, Point] = {
        'up': (-1, 0),
        'right': (0, 1),
        'down': (1, 0),
        'left': (0, -1)
    }
    
    while True:
        # move
        nextPos: Point = tuple(map(sum, zip(currPos, dirs[direction])))
        # check rows and columns if out of bounds
        if nextPos[0] < 0 or nextPos[0] == len(field) or nextPos[1] < 0 or nextPos[1] == len(field[0]):
            exited = True
            break

        # check for wall
        if field[nextPos[0]][nextPos[1]] == '#':
            break

        # add visited
        currPos = nextPos
        visited.append(currPos)

    return (visited, currPos, exited)

rowGuard = None
colGuard = None

directions: list[Direction] = [
    'up',
    'right',
    'down',
    'left'
]

# find guard
for rNum, rVal in enumerate(graph):
    colGuard = rVal.find('^')
    if colGuard != -1:
        rowGuard = rNum
        break

rowGuard: int
colGuard: int

graph[rowGuard] = graph[rowGuard][:colGuard] + '.' + graph[rowGuard][colGuard+1:] 

# do movement
facing: int = 0
visited: list[tuple[int, int, int]] = []

while True:
    # move
    newVisted, newPos, didExit = moveDirection(graph, directions[facing], (rowGuard, colGuard))
    
    # update visited
    visited += [(x[0],x[1],facing) for x in newVisted]
    rowGuard, colGuard = newPos

    # check if out of bounds
    if didExit:
        break

    # rotate
    facing = (facing + 1) % 4

validObstructionCount: int = 0
for i, pos in reversed(list(enumerate(visited))[1:]):
    print(f'obstructing: {pos}')
    # make copy of map
    newGraph = [x for x in graph]
    # put object in position
    newLine: str = newGraph[pos[0]][:pos[1]] + '#' + newGraph[pos[0]][pos[1]+1:]
    newGraph[pos[0]] = newLine
    
    # continue simulation movement
    oldVisited = {x for x in visited[:i]}
    simRowGuard, simColGuard = visited[i-1][:2]
    simFacing = (visited[i-1][2] + 1) % 4
    while True:
        # move
        newVisted, newPos, didExit = moveDirection(newGraph, directions[simFacing], (simRowGuard, simColGuard))

        # check if postition is already visited # has loop
        simulatedVisited = set([(x[0], x[1], simFacing) for x in newVisted])
        intersection = oldVisited & simulatedVisited
        if len(intersection):
            print(intersection)
            validObstructionCount += 1
            break

        # check if out of bounds # no loop
        if didExit:
            break

        oldVisited |= simulatedVisited

        # continue simulation
        simRowGuard, simColGuard = newPos

        # rotate
        simFacing = (simFacing + 1) % 4

print(validObstructionCount)

