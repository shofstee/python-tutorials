# https://dmoj.ca/problem/coci18c3p1
honiBlock = 'HONI'
testString = input()

honiIndex = 0
numHonis = 0

for i in range(0, len(testString)):
    if testString[i] == honiBlock[honiIndex]:
        honiIndex = honiIndex + 1
        if honiIndex >= len(honiBlock):
            numHonis = numHonis + 1
            honiIndex = 0
print(numHonis)