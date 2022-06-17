import numpy as np 
import matplotlib.pyplot as plt 

def f(x):
    return np.cos(x)

def differentiate(f, x0, xf, dx):
    # Generate x and y points.
    x = np.arange(x0, xf, dx)
    y = f(x)
    # Generate dy and dx points.
    dy = []
    dx = [dx for num in range(len(x)-1)]
    for i in range(len(y)-1):
        diff = y[i+1] - y[i]
        dy.append(diff)
    m = [dy/dx for dy, dx in zip(dy, dx)]
    plt.scatter(x[1:], m, color='red', s=2)
    plt.scatter(x, y, color='blue', s=2)
    plt.show()

differentiate(f, -2*3.14, 2*3.14, 0.001)
