def prettyPrint(array: list[str]):
    for i in array:
        print(i.strip())

## input
with open("input.txt", 'r') as f:
    textIn = f.readlines()
    prettyPrint(textIn)

## format input
leftList: list[int] = []
rightList: list[int] = []
for line in textIn:
    a, b = line.strip().split('  ')
    leftList.append(int(a))
    rightList.append(int(b))

## sort
leftList.sort()
rightList.sort()

print(leftList)
print(rightList)

## calculate
totalDiff = 0
for i in range(len(leftList)):
    diff = abs(leftList[i] - rightList[i])
    totalDiff += diff
    print(totalDiff)
