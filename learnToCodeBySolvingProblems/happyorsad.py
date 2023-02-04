import re

HAPPY = '\\:\\-\\)'
SAD = '\\:\\-\\('

text = input()

num_happy = len(re.findall(HAPPY, text))
num_sad = len(re.findall(SAD, text))

if num_sad == 0 and num_happy == 0:
    print('none')
elif num_sad == num_happy:
    print('unsure')
elif num_sad > num_happy:
    print('sad')
else:
    print('happy')
