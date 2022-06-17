from random import choice

def get_step(direction='both', max_distance=10):
    # Set direction
    if direction == 'both':
        direction = choice([-1, 1])
    elif direction == 'left':
        direction = choice([-1])
    elif direction == 'right':
        direction = choice([1])
    
    # Set distance
    distance = choice(range(max_distance+1))

    step = direction * distance
    return step

class RandomWalk():
    """Generate random walks."""
    def __init__(self, num_points=5000):
        """Attributes of a walk."""
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until we reach the number of points we need.
        while len(self.x_values) < self.num_points:
            
            x_step = get_step('both', 10)
            y_step = get_step('both', 10)

            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)