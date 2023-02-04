# solution ccc19j1
apples_3 = int(input())
apples_2 = int(input())
apples_1 = int(input())
apples_total = (apples_3 * 3) + (apples_2 * 2) + apples_1

bananas_3 = int(input())
bananas_2 = int(input())
bananas_1 = int(input())
bananas_total = (bananas_3 * 3) + (bananas_2 * 2) + bananas_1

if apples_total > bananas_total:
    print('A')
elif apples_total < bananas_total:
    print('B')
else:
    print('T')
