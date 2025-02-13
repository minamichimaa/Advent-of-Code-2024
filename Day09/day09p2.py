from typing import Literal, TypedDict


def prettyPrint(array: list[str]) -> None:
    for i in array:
        print(i.strip())


# 2333133121414131402

# 00...111...2...333.44.5555.6666.777.888899
# 0099.111...2...333.44.5555.6666.777.8888..
# 0099.1117772...333.44.5555.6666.....8888..
# 0099.111777244.333....5555.6666.....8888..
# 00992111777.44.333....5555.6666.....8888..

# 2858

BlockObject = TypedDict("BlockObject", {"startingIndex": int, "length": int})

## input
with open("input.txt", "r") as f:
    textIn = f.readlines()

prettyPrint(textIn)

diskMap = textIn[0].strip()

# initalized blocks
blocks: list[int | Literal["."]] = []
currentID: int = 0
ids: dict[int, BlockObject] = {}
for i, v in enumerate(diskMap):
    eveness = i % 2

    # ID
    if eveness == 0:
        # write memory
        currentIndex = len(blocks)
        for x in range(int(v)):
            blocks.append(currentID)

        # save in dictionary
        blockObj: BlockObject = {"startingIndex": currentIndex, "length": int(v)}
        ids[currentID] = blockObj
        # increment id for next
        currentID += 1

    # space
    else:
        # write space
        for x in range(int(v)):
            blocks.append(".")

# reorder
for id in reversed(ids):
    # initialize
    startingSpace = None
    currentLengthSpace = 0
    # iterate through blocks
    for i, v in enumerate(blocks):
        # if reached starting postion of id, reset
        if i == ids[id]["startingIndex"]:
            startingSpace = None
            currentLengthSpace = 0
            break
        # save position and current length of space
        if v == ".":
            if startingSpace == None:
                startingSpace = i
            currentLengthSpace += 1
        # otherwise reset position
        else:
            startingSpace = None
            currentLengthSpace = 0
        # if length is long enough, move
        if currentLengthSpace == ids[id]["length"]:
            # write new memory
            for x in range(startingSpace, startingSpace + currentLengthSpace):
                blocks[x] = id
            # free memory
            for x in range(
                ids[id]["startingIndex"], ids[id]["startingIndex"] + ids[id]["length"]
            ):
                blocks[x] = "."
            # reset space
            startingSpace = None
            currentLengthSpace = 0
            break

# calculate result
total: int = 0
for i, v in enumerate(blocks):
    if v != ".":
        total += i * v

print(total)
