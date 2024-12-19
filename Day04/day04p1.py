def prettyPrint(array: list[str]):
    for i in array:
        print(i.strip())

directions: dict[str, tuple[int, int]] = {
    'up': (-1, 0),
    'upRight': (-1, 1),
    'right': (0, 1),
    'downRight': (1, 1),
    'down': (1, 0),
    'downleft': (1, -1),
    'left': (0, -1),
    'upLeft': (-1, -1),
}

def letterSearch(array: list[list[str]], startingPos: tuple[int, int], direction: str, letter: str) -> tuple[int, int] | None:
    r, c = startingPos
    r1, c1 = directions[direction]
    
    r += r1
    c += c1
    
    # check if out of bounds
    if r < 0 or r >= len(array) or c < 0 or c >= len(array[0]):
        return None

    # check if letter is correct
    if array[r][c] == letter:
        return (r, c)

    # not right letter
    return None

## input
with open("input.txt", 'r') as f:
    textIn = f.readlines()

wSearch: list[str] = [x.strip() for x in textIn]

count: int = 0
# rows
for i in range(len(wSearch)):
    # columns
    for j in range(len(wSearch[i])):
        ## search for X
        if wSearch[i][j] == 'X':
            # do each direction
            for dir in directions:
                # find M
                mReturn = letterSearch(wSearch, (i,j), dir, 'M')
                if mReturn:
                    # find A
                    aReturn = letterSearch(wSearch, mReturn, dir, 'A')
                    if aReturn:
                        # find S
                        sReturn = letterSearch(wSearch, aReturn, dir, 'S')
                        if sReturn:
                            count += 1

print(count)