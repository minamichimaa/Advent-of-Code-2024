from collections import defaultdict


def prettyPrint(array: list[str]):
    for i in array:
        print(i.strip())


def xSearch(array: list[str], startingPos: tuple[int, int]) -> bool:
    r = startingPos[0]
    c = startingPos[1]

    # A is on the edge (of glory)
    if r in (0, len(array) - 1) or c in (0, len(array[0]) - 1):
        return False

    directions = [
        (-1, -1),  # topLeft
        (-1, 1),  # topRight
        (1, -1),  # bottomLeft
        (1, 1),  # bottomRight
    ]

    # count Ms and Ss
    letterCount = defaultdict(int)
    for r1, c1 in directions:
        letterCount[array[r + r1][c + c1]] += 1
    # 2 Ms and 2 Ss
    if letterCount["M"] == letterCount["S"] == 2:
        # opposing letters need to be opposite
        if array[r - 1][c - 1] != array[r + 1][c + 1]:
            return True
    # no X-MAS
    return False


## input
with open("input.txt", "r") as f:
    textIn = f.readlines()

wSearch: list[str] = [x.strip() for x in textIn]

count: int = 0
# rows
for i in range(len(wSearch)):
    # columns
    for j in range(len(wSearch[i])):
        ## search for A
        if wSearch[i][j] == "A":
            if xSearch(wSearch, (i, j)):
                count += 1

print(count)
