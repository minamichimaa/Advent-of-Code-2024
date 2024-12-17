import heapq

def prettyPrint(array: list[str]):
    for i in array:
        print(i.strip())

def getAdjacentCoordinates(grid: list[list[str]], coordinate: tuple[int, int]) -> list[tuple[tuple[int, int], str]]:
    r, c = coordinate

    directions = {
        'N': (-1,0),
        'E': (0,1),
        'S': (1,0),
        'W': (0,-1),
    }

    valid = []

    for dir, v in directions.items():
        r1, c1 = v
        r2 = r+r1
        c2 = c+c1
        if grid[r2][c2] != '#':
             valid.append(((r2,c2), dir))
        
    return valid

## input
with open("input.txt", 'r') as f:
    textIn = f.readlines()

grid = [list(x.strip()) for x in textIn]

# starting position and facing direction
startPosDir = ((len(grid) - 2, 1), 'E')
# costs and parents
positions = {
    (startPosDir): {
        'cost': 0, 
        'parent': {}
    }
}
visited = {(startPosDir)}

# to be visted
# heap with key of cost (positions[(startPosDir)]['cost'])
queue = [(positions[(startPosDir)]['cost'], startPosDir)]
heapq.heapify(queue)

# do until every position is visited
while len(queue):
    # visit next position
    costco, posDir = heapq.heappop(queue)
    visited.add(posDir)
    
    # get next coordinates
    adjacent = getAdjacentCoordinates(grid, posDir[0])
    for adj in adjacent:
        # only unvisited
        if adj not in visited:
            # calculate how much it should cost
            calcCost = positions[posDir]['cost'] + (1 if adj[1] == posDir[1] else 1001)
            # check if cost already exists and if lower
            if adj not in positions or positions[adj]['cost'] > calcCost:
                positions[adj] = {'cost': calcCost, 'parent': {posDir}}
            # add parent
            positions[adj]['parent'].add((posDir))
            # add new positions
            heapq.heappush(queue, (positions[adj]['cost'], adj))

endVisited = set()
endQueue = set()
endPos = (1, len(grid[1]) - 2)
# add direction of final
if (endPos, 'N') in positions:
    endQueue.add((endPos, 'N'))
if (endPos, 'E') in positions:
    endQueue.add((endPos, 'E'))

# traverse backwards and count all possible optimal paths
while len(endQueue):
    current = endQueue.pop()
    pos = current[0]
    # print(pos)
    if current not in endVisited:
        diff = set(positions[current]['parent']).difference(endVisited)
        endQueue = endQueue.union(diff)
    endVisited.add(pos)

print(len(endVisited))
