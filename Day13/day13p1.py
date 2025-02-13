import re
import sympy


def prettyPrint(array: list[str]):
    for i in array:
        print(i.strip())


regexA = re.compile(r"Button A: X\+([0-9]+), Y\+([0-9]+)")
regexB = re.compile(r"Button B: X\+([0-9]+), Y\+([0-9]+)")
regexPrize = re.compile(r"Prize: X=([0-9]+), Y=([0-9]+)")

## input
with open("input.txt", "r") as f:
    textIn = f.readlines()

# parse data
machines = []
prizes = []

for i, line in enumerate(textIn):
    j = i // 4

    # button A
    if i % 4 == 0:
        x, y = (int(z) for z in regexA.findall(line)[0])
        machines.append([[x], [y]])

    # button B
    elif i % 4 == 1:
        x, y = (int(z) for z in regexB.findall(line)[0])
        machines[j][0].append(x)
        machines[j][1].append(y)

    # prize
    elif i % 4 == 2:
        x, y = (int(z) for z in regexPrize.findall(line)[0])
        prizes.append((x, y))

coins = 0

for i, v in enumerate(zip(machines, prizes)):
    # solve for x and y
    x, y = sympy.symbols(["x", "y"])
    system = [
        sympy.Eq(v[0][0][0] * x + v[0][0][1] * y, v[1][0]),
        sympy.Eq(v[0][1][0] * x + v[0][1][1] * y, v[1][1]),
    ]
    solution = sympy.solve(system, [x, y])
    # check for whole numbers
    if (
        type(solution[x]) == sympy.core.numbers.Integer
        and type(solution[y]) == sympy.core.numbers.Integer
    ):
        # add number of coins
        coins += 3 * int(solution[x]) + int(solution[y])

print(coins)
