# solution ccc18j1
phonenumber1 = input()
phonenumber2 = input()
phonenumber3 = input()
phonenumber4 = input()

firstOk = phonenumber1 == '8' or phonenumber1 == '9'
middleOk = phonenumber2 == phonenumber3
lastOk = phonenumber4 == '8' or phonenumber4 == '9'
if firstOk and middleOk and lastOk:
    print('ignore')
else:
    print('answer')
