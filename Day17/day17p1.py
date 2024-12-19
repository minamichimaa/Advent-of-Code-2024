import re

def prettyPrint(array: list[str]):
    for i in array:
        print(i.strip())

def operand(combo: int, A: int, B: int, C: int) -> int:
    match combo:
        case 4:
            return A
        case 5:
            return B
        case 6:
            return C
        case _:
            return combo

regex = re.compile(r'([0-9]+)')
regexRegister = re.compile(r'Register ([A-C]{1}): ([0-9]+)')

## input
with open("test2.txt", 'r') as f:
    textIn = f.readlines()
    
prettyPrint(textIn)

registers = {}
program = []

for line in textIn:
    if line.startswith('Register'):
        found = regexRegister.findall(line)[0]
        registers[found[0]] = int(found[1])
    elif line.startswith('Program'):
        found = regex.findall(line)
        program = [int(x) for x in found]
        
print(registers, program)
output = []
currentIndex = 0
while True:
    if currentIndex >= len(program):
        break
    opcode = program[currentIndex]
    combo = program[currentIndex+1]
    
    match opcode:
        case 0:
            registers['A'] = registers['A'] // 2**operand(combo, registers['A'], registers['B'], registers['C'])
        case 1:
            registers['B'] = registers['B'] ^ combo
        case 2:
            registers['B'] = operand(combo, registers['A'], registers['B'], registers['C']) % 8
        case 3:
            if registers['A'] != 0:
                currentIndex = combo % 8
                continue
        case 4:
            registers['B'] =  registers['B'] ^ registers['C']
        case 5:
            output.append(str(operand(combo, registers['A'], registers['B'], registers['C']) % 8))
        case 6:
            registers['B'] = registers['A'] // 2**operand(combo, registers['A'], registers['B'], registers['C'])
        case 7:
            registers['C'] = registers['A'] // 2**operand(combo, registers['A'], registers['B'], registers['C'])
            
    currentIndex += 2

print(','.join(output))