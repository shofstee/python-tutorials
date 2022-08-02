import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
fibonacci = [1, 2, 3, 5, 8]
fix, ax = plt.subplots()

ax.plot(input_values, squares, color='red')
ax.plot(input_values, fibonacci)
ax.scatter(2, 4)

scatter_x_values = [1, 2, 3, 4, 5]
scatter_y_values = [1, 4, 9, 16, 25]
ax.scatter(scatter_x_values, scatter_y_values, s=10,  c=scatter_y_values, cmap=plt.cm.Blues)

ax.set_title("Numbers", fontsize=14)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Something", fontsize=14)
ax.tick_params(axis='both', labelsize=14)
plt.style.use('seaborn-darkgrid')
plt.show()
