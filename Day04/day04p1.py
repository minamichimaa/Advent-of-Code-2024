from typing import Literal, TypeAlias

def prettyPrint(array: list[str]):
    for i in array:
        print(i.strip())

Direction: TypeAlias = Literal['topLeft', 'up', 'topRight', 'left', 'right', 'bottomleft', 'down', 'bottomRight']

def letterSearch(array: list[list[str]], startingPos: tuple[int, int], direction: Direction, letter: str) -> tuple[int, int] | None:
    r = startingPos[0]
    c = startingPos[1]
    # update position based on direction
    if direction == 'topLeft':
        r -= 1
        c -= 1
    elif direction == 'up':
        r -= 1
    elif direction == 'topRight':
        r -= 1
        c += 1
    elif direction == 'left':
        c -= 1
    elif direction == 'right':
        c += 1
    elif direction == 'bottomleft':
        c -= 1
        r += 1
    elif direction == 'down':
        r += 1
    elif direction == 'bottomRight':
        c += 1
        r += 1
    
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

directions: list[Direction] = [
    'topLeft',
    'up',
    'topRight',
    'left',
    'right',
    'bottomleft',
    'down',
    'bottomRight'
]

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