width = int(input())
percentage_cheese = int(input())

if width == 3 and percentage_cheese >= 95:
    statisfaction = 'absolutely'
elif width == 1 and percentage_cheese <= 50:
    statisfaction = 'fairly'
else:
    statisfaction = 'very'

print(f'C.C. is {statisfaction} satisfied with her pizza.')
