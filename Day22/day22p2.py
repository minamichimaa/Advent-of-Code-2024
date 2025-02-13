from collections import defaultdict


def prettyPrint(array: list[str]):
    for i in array:
        print(i)


## input
with open("input.txt", "r") as f:
    textIn = f.readlines()

secrets = [int(x) for x in textIn]

steps = 2000
prices = []
priceChanges = []

for originalSecret in secrets:
    lastPrice = originalSecret % 10
    secretPrices = [lastPrice]
    secretPriceChanges = []
    x = originalSecret

    for i in range(steps):
        # step 1
        y = x << 6  # multiply by 64
        z = x ^ y  # mix
        x = z & 16777215  # prune

        # step 2
        y = x >> 5  # divide by 32
        z = x ^ y  # mix
        x = z & 16777215  # prune

        # step 3
        y = x * 2048  # multiply by 2048
        z = x ^ y  # mix
        x = z & 16777215  # prune

        # calculate prices and price changes
        newPrice = x % 10
        secretPriceChanges.append(newPrice - lastPrice)
        secretPrices.append(newPrice)
        lastPrice = newPrice

    # add to lists of all
    prices.append(secretPrices)
    priceChanges.append(secretPriceChanges)

# find first occurance of sequences of prices changes
moneys = []

for i in range(len(priceChanges)):
    money = {}
    # do for every sequence of 4
    for j in range(0, len(priceChanges[i]) - 3):
        # only add if sequence is the first occurance
        seq = (
            priceChanges[i][j],
            priceChanges[i][j + 1],
            priceChanges[i][j + 2],
            priceChanges[i][j + 3],
        )
        if seq not in money:
            money[seq] = prices[i][j + 4]
    moneys.append(money)

# merge and add prices of each together
mergedMoneys = defaultdict(int)

for i in moneys:
    for k, v in i.items():
        mergedMoneys[k] += v

print(max(mergedMoneys.values()))
