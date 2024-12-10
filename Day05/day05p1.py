def prettyPrint(array: list):
    for i in array:
        print(i.strip())

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

total = 0

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
        
    # no overlap
    if correctOrder:
        middleIndex = len(update) // 2
        total += update[middleIndex]
    
print(total)