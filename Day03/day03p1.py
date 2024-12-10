import re

def prettyPrint(array: list):
    for i in array:
        print(i.strip())

## input
with open("input.txt", 'r') as f:
    textIn = f.readlines()

regex = re.compile(r'mul\(([0-9]{1,3})\,([0-9]{1,3})\)')

total = 0
for line in textIn:
    # find instructions
    matches = regex.findall(line)
    # calculate multiplication
    for match in matches:
        result = int(match[0]) * int(match[1])
        total += result

print(total)