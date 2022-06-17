import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

def f_abs(f, x):
    """Return modified function, basically absolute value."""
    # Create y points given x points based on fxn.
    y = f(x)
    # switch y to positive if it is negative.
    for i in range(len(x)):
        if y[i] < 0:
            y[i] = -y[i]
    return y

def show_abs_fxn():
    x = np.arange(0, 10, 0.01)
    y = f_abs(f, x)
    plt.scatter(x, y, s=10)
    plt.show()

def f_get bounds(f):
    """Based on f(x), return neg and pos lists with bounds."""

def integrate(f, x0, x1, N):
    # Generate x and y points, determine fmax.
    x = np.arange(x0, x1, 0.01)
    y = f_abs(f, x)
    fmax = max(y)

    # Create N random points of x and y witin the rectangular area.
    x_rand = x0 + np.random.random(N) * (x1 - x0)
    y_rand = np.random.random(N) * fmax

    # where() returns list in a tuple in the form ([a, b]), use i_below[0] to
    # access the list in the tuple
    i_below = np.where(y_rand < f(x_rand))
    i_above = np.where(y_rand >= f(x_rand))

    plt.plot(x, y, color="red")
    plt.scatter(x_rand[i_below], y_rand[i_below], color='green', s=1)
    plt.scatter(x_rand[i_above], y_rand[i_above], color='red', s=1)
    plt.show()

    # Probability of under curve is (# of points under/total)
    p = len(i_below[0])/N
    # Area = (width * height * probability)
    auc = p * fmax * (x1 - x0)
    print("Area Under Curve: " + str(auc))

integrate(f, 0, 10, 100000)

# show_abs_fxn()
