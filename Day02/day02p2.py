def prettyPrint(array: list[str]):
    for i in array:
        print(i.strip())


def isSafe(report: list[int]) -> bool:
    diff = report[0] - report[1]
    if abs(diff) < 1 or abs(diff) > 3:
        return False

    for i in range(2, len(report)):
        newDiff = report[i - 1] - report[i]
        # check if signs match
        cross = diff * newDiff
        if cross < 0:
            return False
        # check if change is within 1 and 3 (inclusive)
        if abs(newDiff) < 1 or abs(newDiff) > 3:
            return False
        # set new
        diff = newDiff

    return True


## input
with open("input.txt", "r") as f:
    textIn = f.readlines()

## format data
reports: list[list[int]] = []
for line in textIn:
    report = [int(x) for x in line.split()]
    reports.append(report)

## count safe reports
safeCount: int = 0
for report in reports:
    # remove nth item from list
    for i in range(len(report)):
        newReport = report[:i] + report[i + 1 :]
        # check if this iteration works
        if isSafe(newReport):
            safeCount += 1
            break

print(safeCount)
