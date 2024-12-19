import re

def prettyPrint(array: list[str]):
    for i in array:
        print(i.strip())

## input
with open("input.txt", 'r') as f:
    textIn = f.readlines()

regex: re.Pattern = re.compile(r'mul\(([0-9]{1,3})\,([0-9]{1,3})\)')

total: int = 0
for line in textIn:
    # find instructions
    matches = regex.findall(line)
    # calculate multiplication
    for match in matches:
        total += int(match[0]) * int(match[1])

print(total)