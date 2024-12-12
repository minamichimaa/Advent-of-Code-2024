from math import log10, floor

def prettyPrint(array: list) -> None:
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

## input
with open("input.txt", 'r') as f:
    textIn = f.readline()

# format numbers
stones = [int(x) for x in textIn.split()]

# do iterations

iterations = 25
for i in range(iterations):
    newStones = []

    for stone in stones:
        # rule 1: number is 0 -> convert to 1
        if stone == 0:
            newStones.append(1)
            continue

        # rule 2: number has even number of digits -> split
        numDigits = digits(stone)
        if numDigits % 2 == 0:
            newStones += list(splitNumber(stone))
            continue

        # rule 3: other -> multiply by 2024
        newStones.append(stone*2024)
    stones = newStones

print(len(stones))
