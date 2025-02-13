import copy
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


regex = re.compile(r"([0-9]+)")
regexRegister = re.compile(r"Register ([A-C]{1}): ([0-9]+)")

## input
with open("input.txt", "r") as f:
    textIn = f.readlines()

prettyPrint(textIn)

registers = {}
program = []

for line in textIn:
    if line.startswith("Register"):
        found = regexRegister.findall(line)[0]
        registers[found[0]] = int(found[1])
    elif line.startswith("Program"):
        found = regex.findall(line)
        program = [int(x) for x in found]

print(registers, program)

i = 0
numMatches = 0
while True:
    newRegisters = copy.deepcopy(registers)
    newRegisters["A"] = i
    # print(newRegisters)

    output = []
    currentIndex = 0
    while True:
        if currentIndex >= len(program):
            break
        opcode = program[currentIndex]
        combo = program[currentIndex + 1]

        match opcode:
            case 0:
                newRegisters["A"] = newRegisters["A"] >> operand(
                    combo, newRegisters["A"], newRegisters["B"], newRegisters["C"]
                )
            case 1:
                newRegisters["B"] = newRegisters["B"] ^ combo
            case 2:
                newRegisters["B"] = (
                    operand(
                        combo, newRegisters["A"], newRegisters["B"], newRegisters["C"]
                    )
                    % 8
                )
            case 3:
                if newRegisters["A"] != 0:
                    currentIndex = combo % 8
                    continue
            case 4:
                newRegisters["B"] = newRegisters["B"] ^ newRegisters["C"]
            case 5:
                output.append(
                    operand(
                        combo, newRegisters["A"], newRegisters["B"], newRegisters["C"]
                    )
                    % 8
                )
            case 6:
                newRegisters["B"] = newRegisters["A"] >> operand(
                    combo, newRegisters["A"], newRegisters["B"], registers["C"]
                )
            case 7:
                newRegisters["C"] = newRegisters["A"] >> operand(
                    combo, newRegisters["A"], newRegisters["B"], newRegisters["C"]
                )

        currentIndex += 2
        if len(output) == len(program):
            break

    isSame = True
    if len(output) != len(program):
        isSame = False
    newNumMatches = 0
    for p, o in zip(program, output):
        if p != o:
            isSame = False
            break
        else:
            newNumMatches += 1
    if newNumMatches > numMatches:
        print(i, bin(i))
        numMatches = newNumMatches

    if isSame:
        print(i)
        break

    i += 1
