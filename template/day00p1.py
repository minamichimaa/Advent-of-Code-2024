def prettyPrint(array: list):
    for i in array:
        print(i.strip())

## input
with open("test.txt", 'r') as f:
    textIn = f.readlines()
    
prettyPrint(textIn)