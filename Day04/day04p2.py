def prettyPrint(array: list):
    for i in array:
        print(i.strip())

def xSearch(array, startingPos):
    r = startingPos[0]
    c = startingPos[1]

    # A is on the edge (of glory)
    if r == 0 or r == len(array)-1 or c == 0 or c == len(array[0])-1:
        return False
            
    topLeft = array[r-1][c-1]
    topRight =  array[r-1][c+1]
    bottomLeft = array[r+1][c-1]
    bottomRight = array[r+1][c+1]

    # Ms on Top
    if topLeft == "M" and topRight == "M" and bottomLeft == "S" and bottomRight == "S":
        return True
    # Ms on Left
    if topLeft == "M" and topRight == "S" and bottomLeft == "M" and bottomRight == "S":
        return True
    # Ms on Right
    if topLeft == "S" and topRight == "M" and bottomLeft == "S" and bottomRight == "M":
        return True
    # Ms on Bottom
    if topLeft == "S" and topRight == "S" and bottomLeft == "M" and bottomRight == "M":
        return True
    # no X-MAS
    return False

## input
with open("input.txt", 'r') as f:
    textIn = f.readlines()

wSearch = [x.strip() for x in textIn]

count = 0
# rows
for i in range(len(wSearch)):
    # columns
    for j in range(len(wSearch[i])):
        ## search for A
        if wSearch[i][j] == 'A':
            if xSearch(wSearch, (i, j)):
                count += 1

print(count)