import re

def prettyPrint(array: list[str]):
    for i in array:
        print(i.strip())

## input
with open("input.txt", 'r') as f:
    textIn = f.readlines()

# find numbers in mult instruction
regex: re.Pattern = re.compile(r'mul\(([0-9]{1,3})\,([0-9]{1,3})\)')
# find instructions
regexAll: re.Pattern = re.compile(r'mul\([0-9]{1,3}\,[0-9]{1,3}\)|don\'t\(\)|do\(\)')

total: int = 0
doing: bool = True
for line in textIn:
    # find instructions
    matches = regexAll.findall(line)
    print(matches)

    # instructions
    for match in matches:
        # don't() instruction
        if match.startswith('don\'t'):
            doing = False
        # do() instruction
        elif match.startswith('do'):
            doing = True
        # do() and mult() instruction
        elif doing == True:
            multMatch = regex.findall(match)
            result = int(multMatch[0][0]) * int(multMatch[0][1])
            total += result

print(total)
