import re
password = input()

length = len(password)
pattern = re.compile('^[a-zA-Z0-9]{8,12}$')
valid = pattern.match(password)

countLower = 0
countUpper = 0
countDigit = 0
for char in password:
    if char.islower():
        countLower = countLower + 1
    elif char.isupper():
        countUpper = countUpper + 1
    elif char.isdigit():
        countDigit = countDigit + 1

if valid and countLower >= 3 and countUpper >= 2 and countDigit >= 1:
    print('Valid')
else:
    print('Invalid')