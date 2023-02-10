numLines = int(input())

english = 0
french = 0

for line in range(0, numLines):
    text = input()
    for i in text:
        if i == 's' or i == 'S':
            french = french + 1
        elif i == 't' or i == 'T':
            english = english + 1

if english > french:
    print('English')
else:
    print('French')