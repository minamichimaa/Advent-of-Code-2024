from typing import TypeAlias
from itertools import combinations

def prettyPrint(array: list[str]) -> None:
    for i in array:
        print(i.strip())

Point: TypeAlias = complex

## input
with open("input.txt", 'r') as f:
    textIn = f.readlines()

'''    
......#....#
...#....0...
....#0....#.
..#....0....
....0....#..
.#....A.....
...#........
#......#....
........A...
.........A..
..........#.
..........#.
'''

graph = [x.strip() for x in textIn]

# find antennas
antennas: dict[str, list[tuple[int, int]]] = {}
for r in range(len(graph)):
    for c in range(len(graph[0])):
        # not empty
        if graph[r][c] != '.':
            # make new freqency
            if graph[r][c] not in antennas:
                antennas[graph[r][c]] = [(r, c)]
            # freqency already established
            else:
                antennas[graph[r][c]].append((r, c))

# print(antennas)
antinodes: set[Point] = set()
bounds = len(graph)

# check each frequency
for freq in antennas:
    # all cominations of antennas in freq
    combs = combinations(antennas[freq], 2)
    for p1, p2 in combs:
        diff: Point = complex(*p1) - complex(*p2)

        # get antinode position
        p1New: Point = complex(*p1) + diff
        p2New: Point = complex(*p2) - diff

        # check if in bounds
        if 0 <= p1New.real < bounds and 0 <= p1New.imag < bounds:
            antinodes.add(p1New)

        if 0 <= p2New.real < bounds and 0 <= p2New.imag < bounds:
            antinodes.add(p2New)


# print(antinodes)
print(len(antinodes))