def prettyPrint(array: list):
    for i in array:
        print(i.strip())

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def depth(self):
        if len(self.children) == 0:
            return 1
        return max(x.depth() + 1 for x in self.children)

    def optimalOrder(self):
        if len(self.children) == 0:
            return (1, self.value)
        childDepths = []
        for child in self.children:
            childDepth, childValues = child.optimalOrder()
            childDepths.append((childDepth+1, f'{self.value} {childValues}'))
        childDepths.sort(key = lambda x: x[0], reverse=True)
        return childDepths[0]

    def __repr__(self):
        return str(self.value)
        string = ''
        for child in self.children:
            string += str(child)
        return f'<{self.value}: {string}>'

## input
with open("input.txt", 'r') as f:
    textIn = f.readlines()

# parse input
rules = {}
updates = []

for line in textIn:
    # rules
    if '|' in line:
        a,b = [int(x) for x in line.strip().split('|')]
        # add to dictionary
        if a in rules:
            rules[a].add(b)
        else:
            rules[a] = {b}
    # updates
    elif ',' in line:
        updates.append([int(x) for x in line.strip().split(',')])

needReorder = []

# check each update
for update in updates:
    correctOrder = True
    pastNums = set()
    queue = update
    # check each number in current update
    for q in queue:
        # has rules
        if q in rules:
            qRules = rules[q]
        # no rules
        else:
            pastNums.add(q)
            continue
        # find if rules overlap with previous numbers
        intersection = pastNums & qRules
        pastNums.add(q)
        if len(intersection) > 0:
            correctOrder = False
            break
    if not correctOrder:
        needReorder.append(update)
        
total = 0
for fix in needReorder:
    # trim rules
    newRules = {}
    for q in fix:
        if q in rules:
            newRules[q] = rules[q] & set(fix)

    # make nodes
    nodeDict = {}
    for rule in newRules:
        # node not already made
        if rule not in nodeDict:
            node = TreeNode(rule)
            nodeDict[rule] = node
        # add children
        for subrule in newRules[rule]:
            if subrule not in nodeDict:
                node = TreeNode(subrule)
                nodeDict[subrule] = node
            nodeDict[rule].children.append(nodeDict[subrule])

    # get longest order of pages
    orders = []
    for node in nodeDict:
        orders.append(nodeDict[node].optimalOrder())
    orders.sort(key = lambda x: x[0], reverse=True)

    # get middle number
    optimalString = orders[0][1].split()
    middleIndex = len(optimalString) // 2
    total += int(optimalString[middleIndex])

print(total)
