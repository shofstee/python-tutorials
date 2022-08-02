# 5-1 Conditional tests en 5-2 More conditional tests
naam = "Piet"
print(naam == "Piet")  # True
print("Piet" in [naam])  # True
print(naam.lower() == "piet")  # True, case sensitive
print(naam == "Piet" and 1 == 1)  # True, allebei waar
print(naam == "Piet" or 1 == 2)  # True want 1e is waar

print(naam == "piet")  # False, case sensitive
print(naam == "Piet" and 1 != 1)  # False, tweede is niet waar
print(naam == "piet" or 1 != 1)  # False, allebei niet waar

# 5-3. Alien Colors #1
alien_color = 'red'

# check passes
if alien_color == 'red':
    print("It's red")

# check fails
if alien_color == 'green':
    print("It's green")

# 5-4. Alien Colors #2-1
alien_color = 'red'
if alien_color == 'green':
    print("It's green")
elif alien_color == 'red':
    print("It's red")
else:
    print("It's color is unknown")

# 5-4. Alien Colors #2-2
alien_color = 'green'
if alien_color == 'green':
    print("It's green")
elif alien_color == 'red':
    print("It's red")
else:
    print("It's color is unknown")

# 5-4. Alien Colors #2-3
alien_color = 'yellow'
if alien_color == 'green':
    print("It's green")
elif alien_color == 'red':
    print("It's red")
else:
    print("It's color is unknown")

# 5-11. Ordinal Numbers
num = [value for value in range(1, 10)]
for curr in num:
    if curr == 1:
        print(f"{curr}st")
    elif curr == 2:
        print(f"{curr}nd")
    elif curr == 3:
        print(f"{curr}rd")
    else:
        print(f"{curr}th")

