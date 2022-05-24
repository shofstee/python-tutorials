import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk.
    rw = RandomWalk(num_points=1_000, distance_x=[0, 5, 10, 50], distance_y=[0, 100, 200])
    rw.fill_walk()
    # Plot the points in the walk.
    plt.style.use('classic')

    # Adjust the figsize to the monitor resolution
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)

    # Plot the random walk
    # ax.plot(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)
    ax.plot(rw.x_values, rw.y_values)

    # Emphasize the first and last points.
    # ax.plot(0, 0, c='green', edgecolors='none', s=100)
    ax.plot(0, 0, c='green')
    # ax.plot(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    ax.plot(rw.x_values[-1], rw.y_values[-1], c='red')
    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
