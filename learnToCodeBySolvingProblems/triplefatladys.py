# a3
testcases = int(input())

cases = []
for num in range(0, testcases):
    cases.append(int(input()))

for case in cases:
    for x in range(case, 20000):
        result = str(x ** 3)
        if result.endswith('888'):
            print(x)
            break


