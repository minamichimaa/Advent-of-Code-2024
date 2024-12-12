def prettyPrint(array: list[str]):
    for i in array:
        print(i.strip())

## input
with open("input.txt", 'r') as f:
    textIn = f.readlines()

## format input
leftList: list = []
rightList: dict[int, int] = {}
for line in textIn:
    a, b = line.strip().split('  ')
    leftList.append(int(a))

    ## count right appearance
    newB = int(b)
    if newB in rightList:
        rightList[newB] += 1
    else:
        rightList[newB] = 1

print(leftList)
print(rightList)

## calulate
totalSimilarity = 0
for i in leftList:
    if i in rightList:
        totalSimilarity += i * rightList[i]
    print(totalSimilarity)
