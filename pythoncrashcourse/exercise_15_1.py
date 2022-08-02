import matplotlib.pyplot as plt

max_val = 10
x_values = range(-max_val, max_val)
y_values = [x**2 for x in range(-max_val, max_val)]
c_map = [y for y in y_values]

fix, ax = plt.subplots()
#ax.plot(x_values, y_values, c=c_map, cmap=plt.cm.Blues, s=100)
ax.plot(x_values, y_values)
plt.show()