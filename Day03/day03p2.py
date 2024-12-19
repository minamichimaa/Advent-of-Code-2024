import re

def prettyPrint(array: list[str]):
    for i in array:
        print(i.strip())

## input
with open("input.txt", 'r') as f:
    textIn = f.readlines()

# find instructions
regex: re.Pattern = re.compile(r'mul\([0-9]{1,3}\,[0-9]{1,3}\)|don\'t\(\)|do\(\)')

total: int = 0
doing: bool = True
for line in textIn:
    # find instructions
    matches = regex.findall(line)

    # instructions
    for match in matches:
        print(match)
        # don't() instruction
        if match.startswith('don\'t'):
            doing = False
        # do() instruction
        elif match.startswith('do'):
            doing = True
        # do() and mult() instruction
        elif doing:
            a, b = (int(x) for x in match[4:-1].split(','))
            total += a * b

print(total)
