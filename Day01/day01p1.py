def prettyPrint(array: list[str]):
    for i in array:
        print(i.strip())


## input
with open("input.txt", "r") as f:
    textIn = f.readlines()

# format input
leftList: list[int] = []
rightList: list[int] = []
for line in textIn:
    l, r = line.strip().split()
    leftList.append(int(l))
    rightList.append(int(r))

## sort
leftList.sort()
rightList.sort()

## calculate
totalDiff = 0
for l, r in zip(leftList, rightList):
    totalDiff += abs(l - r)

print(totalDiff)
