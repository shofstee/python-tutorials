# 4-1 Pizzas
pizzas = ['Tonno', 'Salami', 'Hawaii']
for pizza in pizzas:
    print(f"Hmmm... pizza {pizza}!")
print("Pizza is the best!")

# 4-2 Animals
animals = ['rhino', 'hippo', 'lion']
for animal in animals:
    print(f"A {animal} would be a great pet.")
print("Or would they?")

# 4-3 Counting to twenty
for num in range(1, 21):
    print(num)

# 4-4 One million (implemented one thousand)
one_to_million = [value for value in range(1, 1_001)]
for num in one_to_million:
    print(num)

# 4-5 Summing a million
print(f"min {min(one_to_million)}, max {max(one_to_million)}, sum {sum(one_to_million)}")

# 4-6 Odd numbers
odds = [value for value in range(1, 20, 2)]
for num in odds:
    print(num)

# 4-7 Threes
threes = [value for value in range(3, 31, 3)]
for num in threes:
    print(num)

# 4-8 Cubes + 4-9 Cubes Comprehension
cubes = [value**3 for value in range(1, 11)]
for num in cubes:
    print(num)

# 4-10 Slices
letters = ["A", "B", "C", "D", "E", "F", "G"]
print(f"The first three items are {letters[:3]}")
print(f"The three items in the middle are {letters[2:5]}")
print(f"The last three items are {letters[-3:]}")

# 4-11 My pizzas, your pizzas
my_pizzas = ['Tonno', 'Salami', 'Hawaii']
friend_pizzas = pizzas[:]
my_pizzas.append('Fantastico')
friend_pizzas.append('Dissapointmentico')
print(my_pizzas)
print(friend_pizzas)

# 4-12 More Loops
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
for mine in my_foods:
    print(f"Mine: {mine}")
for his in friend_foods:
    print(f"His: {his}")

# 4-13 Tuples
foodz = ('Brood', 'Pizza', 'Rijst', 'Macaroni', 'Couscous')
for food in foodz:
    print(food)
foodz = ('Pindakaas', 'Pizza', 'Rijst', 'Macaroni', 'Couscous')
for food in foodz:
    print(food)