class Dish:

    def __init__(self, name, calories):
        self.name = name
        self.calories = calories


BURGERS = [Dish('Cheesburger', 461), Dish('Fishburger', 431), Dish('Veggieburger', 420), Dish('No burger', 0)]
DRINKS = [Dish('Soft drink', 130), Dish('Orange Juice', 160), Dish('Milk', 118), Dish('No drinks', 0)]
SIDEORDERS = [Dish('Fries', 100), Dish('Baked Potato', 57), Dish('Chef Salad', 70), Dish('No side order', 0)]
DESERTS = [Dish('Apple pie', 167), Dish('Sundae', 266), Dish('Fruit Cup', 75), Dish('No desert', 0)]

burger = int(input()) - 1
sideorder = int(input()) - 1
drink = int(input()) - 1
desert = int(input()) - 1

calories = BURGERS[burger].calories + DRINKS[drink].calories + SIDEORDERS[sideorder].calories + DESERTS[desert].calories
print(f'Your total Calorie count is {calories}.')
