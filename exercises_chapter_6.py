# Dictionary
professions = {"Piet": "Bakker", "Jan": "Slager", "Klaas": "Boer"}

for name, profession in professions.items():
    print(f"Name: {name}, Profession: {profession}")

for name in sorted(professions.keys()):
    print(f"Name: {name}")

for profession in sorted(professions.values(), reverse=True):
    print(f"Profession: {profession}")

