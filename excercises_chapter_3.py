# 3-1 Names:
names=["Pietertje", 'Sjaak', 'Jan']
print(f"{names[0]}, {names[1]}, {names[2]}")
# 3-2 Greetings
print(f"Greetings, {names[0]}!")
print(f"Greetings, {names[1]}!")
print(f"Greetings, {names[2]}!")
# 3-4 Guest list
# 3-5 Changing guest list
print(f"{names[1]} gaat weg")
names.remove("Sjaak")
print(f"{names}")
names.insert(1, "Klaas")
print(f"{names}")
# 3-6 More Guests
names.insert(0, "Jeffrey")
names.insert(2, "Tim")
names.append("John")
print(f"{names}")
# 3-7 Shrinking guest list
names.pop()
names.pop()
names.pop()
names.pop()
del names[0]
del names[0]
print(f"{names}")
# 3-8 Seeing the world
places=["Hongarije", "Brazilie", "Nieuw-Zeeland", "Maleisie"]
print(f"OG: {places}")
print(f"Sorted: {sorted(places)}")
print(f"OG: {places}")
print(f"Sorted: {sorted(places, reverse=True)}")
print(f"OG: {places}")
places.reverse()
print(f"OG-reversed: {places}")
places.reverse()
print(f"OG: {places}")
places.sort()
print(f"OG sorted: {places}")
places.sort(reverse=True)
print(f"OG sorted-reverse: {places}")
