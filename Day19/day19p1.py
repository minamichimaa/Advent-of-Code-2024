def prettyPrint(array: list[str]):
    for i in array:
        print(i.strip())


myCache = {}
patterns = tuple()


def isValidPattern(design) -> bool:
    # previously found
    if design in myCache:
        return myCache[design]

    # split substrings
    for i in range(1, len(design)):
        part1 = design[:i]
        part2 = design[i:]

        # recursively check substrings
        if part1 in patterns and (part2 in patterns or isValidPattern(part2)):
            # found # cache and return
            myCache[design] = True
            return True

    # no valid pattern # cache and return
    myCache[design] = False
    return False


## input
with open("input.txt", "r") as f:
    textIn = f.readlines()

# parse input
patterns = tuple([x for x in textIn[0].strip().split(", ")])
designs = tuple([x.strip() for x in textIn[2:]])

# could valid designs
valid = 0
for design in designs:
    if isValidPattern(design):
        valid += 1

print(valid)
