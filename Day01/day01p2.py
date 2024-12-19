from collections import defaultdict

def prettyPrint(array: list[str]):
    for i in array:
        print(i.strip())

## input
with open("input.txt", 'r') as f:
    textIn = f.readlines()

## format input
leftList: list = []
rightList: defaultdict[dict[int, int]] = defaultdict(int)
for line in textIn:
    l, r = line.strip().split()
    leftList.append(int(l))

    ## count right appearance
    newB = int(r)
    rightList[newB] += 1

## calulate
totalSimilarity = 0
for x in leftList:
    if x in rightList:
        totalSimilarity += x * rightList[x]
        
print(totalSimilarity)
