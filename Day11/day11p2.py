from math import log10, floor


def prettyPrint(array: list[str]) -> None:
    for i in array:
        print(i.strip())


def digits(number: int) -> int:
    if number == 0:
        return 1
    return floor(log10(number)) + 1


def splitNumber(number: int) -> tuple[int, int]:
    numDigits = digits(number)
    halfDigits = numDigits // 2

    firstHalf = number // (10**halfDigits)
    secondHalf = number % (10**halfDigits)

    return (firstHalf, secondHalf)


def tryAdd(dictionary: dict[int, int], number: int, value: int) -> dict[int, int]:
    newDict = dictionary

    if number in newDict:
        newDict[number] += value
    else:
        newDict[number] = value

    return newDict


## input
with open("input.txt", "r") as f:
    textIn = f.readline()

# format numbers
stones: dict[int, int] = {}
for stone in [int(x) for x in textIn.split()]:
    stones = tryAdd(stones, stone, 1)

# do iterations
iterations = 75
for i in range(iterations):
    # key: stone number | value: number of
    newStones: dict[int, int] = {}

    for stone, count in stones.items():
        # rule 1: number is 0 -> convert to 1
        if stone == 0:
            newStones = tryAdd(newStones, 1, count)
            continue

        # rule 2: number has even number of digits -> split
        numDigits = digits(stone)
        if numDigits % 2 == 0:
            for x in splitNumber(stone):
                newStones = tryAdd(newStones, x, count)
            continue

        # rule 3: other -> multiply by 2024
        newStones = tryAdd(newStones, stone * 2024, count)
    stones = newStones

total: int = 0
for i in stones:
    total += stones[i]
print(total)
