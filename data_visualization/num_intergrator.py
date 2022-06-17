import numpy as np 
import matplotlib.pyplot as plt 

def f(x):
    return 1/((4*(x**2))-((4*x)+1)**(1/3))

def integrate(f, x0, xf, N):
    # What is the base of each rectangle?
    dx = (xf-x0)/N
    # What x and y values are on the right end of each rect?
    x = np.arange(x0+dx, xf+dx, dx)
    y = f(x)
    integration = 0
    for num in y:
        rect_area = dx * num
        integration += rect_area
    return integration

print(integrate(f, 0, 14, 1000000))