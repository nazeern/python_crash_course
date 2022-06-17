import matplotlib.pyplot as plt

from random_walk import RandomWalk

# cd Documents/python_work/data_visualization

while True:
    # Create instance of RandomWalk.
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Set the size of the interactive window.
    plt.figure(dpi=128, figsize=(10, 5))

    # Plot random walk with gradient.
    point_numbers = list(range(rw.num_points))
    # plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
    #     s=1)
    plt.plot(rw.x_values, rw.y_values, c='blue')

    # Start and end points (green and red, respectively).
    plt.scatter(0, 0, c='green', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)

    # Remove axes.
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
