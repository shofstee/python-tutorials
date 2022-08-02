from random import choice


def get_step(distance_options):
    direction = choice([1, -1])
    distance = choice(distance_options)
    return direction * distance


class RandomWalk:

    def __init__(self, num_points=5000, distance_x=None, distance_y=None):
        """Initialize attributes of a walk."""
        if distance_x is None:
            distance_x = [0, 1, 2, 3, 4]
        if distance_y is None:
            distance_y = [0, 1, 2, 3, 4]
        self.num_points = num_points
        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]
        self.distance_x = distance_x
        self.distance_y = distance_y

    def fill_walk(self):
        """Calculate all the points in the walk."""
        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:
            # Decide which direction to go and how far to go in that direction.

            x_step = get_step(self.distance_x)
            y_step = get_step(self.distance_y)

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue
            # Calculate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            self.x_values.append(x)
            self.y_values.append(y)
