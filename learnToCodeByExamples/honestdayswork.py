# solution  wc18c3j1
paint = int(input())
paintPerBottlecap = int(input())
pricePerPaintedBottlecap = int(input())
pricePerLiterPaint = 1

print((paint//paintPerBottlecap) * pricePerPaintedBottlecap + (paint % paintPerBottlecap) * pricePerLiterPaint)