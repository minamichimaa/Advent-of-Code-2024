from typing import Literal


def prettyPrint(array: list[str]) -> None:
    for i in array:
        print(i.strip())


# 2333133121414131402
# 0099811188827773336446555566..............
# 1928

## input
with open("input.txt", "r") as f:
    textIn = f.readlines()

prettyPrint(textIn)

diskMap = textIn[0].strip()

# initalized blocks
blocks: list[int | Literal["."]] = []
currentID: int = 0
for i, v in enumerate(diskMap):
    eveness = i % 2

    # ID
    if eveness == 0:
        for x in range(int(v)):
            blocks.append(currentID)
        currentID += 1
    # space
    else:
        for x in range(int(v)):
            blocks.append(".")

print("".join(str(x) for x in blocks))

# reorder
beginning: int = 0
end = len(blocks) - 1

# move pointers until they meet
while beginning <= end:
    # found empty space
    if blocks[beginning] == ".":
        # move memory
        blocks[beginning] = blocks[end]
        blocks[end] = "."

        # move right pointer
        while True:
            end -= 1
            if blocks[end] != ".":
                break

    # move left pointer
    beginning += 1

# calculate result
total: int = 0
for i, v in enumerate(blocks):
    if v != ".":
        total += i * v

print(total)
