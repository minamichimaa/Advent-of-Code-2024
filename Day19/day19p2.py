def prettyPrint(array: list[str]):
    for i in array:
        print(i.strip())


myCache = {}
patterns = tuple()


def isValidPattern(design) -> list:
    # previously found
    if design in myCache:
        return myCache[design]

    # new
    validArrangements = 0

    # split substrings
    for i in range(1, len(design)):
        part1 = design[:i]
        part2 = design[i:]

        # recursively check substrings
        if part1 in patterns:
            # if exists in patterns
            if part2 in patterns:
                validArrangements += 1
            # find num of patterns from the substring
            validArrangements += isValidPattern(part2)

    # cache and return
    myCache[design] = validArrangements
    return validArrangements


## input
with open("input.txt", "r") as f:
    textIn = f.readlines()

# parse input
patterns = tuple([x for x in textIn[0].strip().split(", ")])
designs = tuple([x.strip() for x in textIn[2:]])

# count variations of designs
valid = 0
for design in designs:
    valid += isValidPattern(design)

print(valid)
