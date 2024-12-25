from collections import defaultdict

def prettyPrint(array: list[str]):
    for i in array:
        print(i)

def findInterConnected(connDict: dict) -> set[tuple['str', 'str', 'str']]:
    interconnections = set()
    
    # check each computer (1)
    for first in connDict:
        # check each connected computer (2)
        for second in connDict[first]:
            # check each connected connected computer (3)
            for third in connDict[second]:
                # check if computer (1) in computer (3)
                if first in connDict[third]:
                    interconnections.add(tuple(sorted((first, second, third))))
    
    return interconnections

def computersStartsWithT(interconnection: tuple[str, str, str]) -> bool:
    for computer in interconnection:
        if computer.startswith('t'):
            return True
    return False

## input
with open("input.txt", 'r') as f:
    textIn = f.readlines()

connections = tuple([tuple(x.strip().split('-')) for x in textIn])

connDict = defaultdict(set)

for conn in connections:
    a, b = conn
    connDict[a].add(b)
    connDict[b].add(a)

interConn = findInterConnected(connDict)

total = 0
for i in interConn:
    if computersStartsWithT(i):
        total += 1

print(total)
