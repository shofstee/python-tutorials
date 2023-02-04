perMonth = int(input())
months=int(input())

totalUnused = 0
for month in range(months):
    used = int(input())
    totalUnused = totalUnused + (perMonth - used)

print(totalUnused + perMonth)
