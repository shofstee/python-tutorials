numberOfParkingSpaces = int(input())
occupiedYesterday = input()
occupiedToday = input()

sameSpaces = 0
for num in range(numberOfParkingSpaces):
    if occupiedToday[num] == 'C' and occupiedYesterday[num] == 'C':
        sameSpaces = sameSpaces + 1

print(sameSpaces)