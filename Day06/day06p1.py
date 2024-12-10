def prettyPrint(array: list):
    for i in array:
        print(i.strip())

## input
with open("input.txt", 'r') as f:
    textIn = f.readlines()
    
graph = [x.strip() for x in textIn]

def moveDirection(field: list, direction: str, position: tuple):
    currPos = position
    visited = {position}
    exited = False

    dirs = {
        'up': (-1, 0),
        'right': (0, 1),
        'down': (1, 0),
        'left': (0, -1)
    }
    
    while True:
        # move
        print(currPos)
        nextPos = tuple(map(sum, zip(currPos, dirs[direction])))
        # check rows and columns if out of bounds
        if nextPos[0] < 0 or nextPos[0] == len(field) or nextPos[1] < 0 or nextPos[1] == len(field[0]):
            exited = True
            break

        # check for wall
        if field[nextPos[0]][nextPos[1]] == '#':
            break

        # add visited
        currPos = nextPos
        visited.add(currPos)

    return (visited, currPos, exited)

rowGuard = None
colGuard = None

directions = [
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

# do movement
facing = 0
visted = {(rowGuard, colGuard)}

while True:
    print((rowGuard, colGuard))
    # move
    newVisted, newPos, didExit = moveDirection(graph, directions[facing], (rowGuard, colGuard))
    
    # update visited
    visted.update(newVisted)
    rowGuard, colGuard = newPos

    # check if out of bounds
    if didExit:
        break

    # rotate
    facing = (facing + 1) % 4

print(visted, len(visted))