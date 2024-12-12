import re

def prettyPrint(array: list[str]) -> None:
    for i in array:
        print(i.strip())

regex = re.compile(r'([0-9]+)')

## input
with open("input.txt", 'r') as f:
    textIn = f.readlines()
    
total = 0

# calculate
for line in textIn:
    # seperate numbers
    numbers = [int(x) for x in regex.findall(line)]
    target = numbers[0]
    sequence = numbers[1:]
    print(target, sequence)

    # current queue
    nums = {sequence[0]}

    # next numbers
    for seq in sequence[1:]:
        newNums = set()
        # try operators
        for num in nums:
            add = num + seq
            mult = num * seq

            # value not tooo big
            if add <= target:
                newNums.add(add)
            if mult <= target:
                newNums.add(mult)
            # new queue
            nums = newNums
            
    # found target
    if target in nums:
        total += target

print(total)