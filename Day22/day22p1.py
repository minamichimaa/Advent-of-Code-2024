def prettyPrint(array: list[str]):
    for i in array:
        print(i)

## input
with open("input.txt", 'r') as f:
    textIn = f.readlines()

secrets = [int(x) for x in textIn]

steps = 2000
total = 0

for originalSecret in secrets:
    x = originalSecret
    for i in range(steps):
        # step 1
        y = x << 6          # multiply by 64
        z = x ^ y           # mix
        x = z & 16777215    # prune     
        
        # step 2
        y = x >> 5          # divide by 32    
        z = x ^ y           # mix
        x = z & 16777215    # prune
        
        # step 3
        y = x * 2048        # multiply by 2048
        z = x ^ y           # mix
        x = z & 16777215    # prune
    total += x

print(total)