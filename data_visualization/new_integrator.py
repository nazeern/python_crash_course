import numpy as np
import matplotlib.pyplot as plt

def f(x):
    # return (x - 5)**2 - 5
    # return abs((x**2) - 4)
    # return abs(np.cos(x)) - 0.5
    # return 2*np.sin(np.sqrt(x))
    # return x
    # return abs(np.cos(x))
    # return (x - 3) * (x - 5) * (x - 7) + 85
    # return (np.cos(x)/x)+0.5
    # return np.cos(x)
    # return abs((np.sin(np.sqrt(x+1)))/(np.sqrt(x+1)))
    return 1/(np.cbrt((4*x**2)-(4*x+1)))

def show_fx_scatter(f, windxL, windxR):
    x = np.arange(windxL, windxR, 0.001)
    y = f(x)
    plt.plot(x, y)
    plt.show()

def get_bounds(f, x0, xf):
    l_bounds = [x0]
    r_bounds = []
    x = np.arange(x0, xf, 0.001)
    y = f(x)
    for i in range(len(x) - 1):
        if (y[i] > 0 > y[i + 1]) or (y[i] < 0 < y[i + 1]):
            r_bounds.append(x[i])
            l_bounds.append(x[i + 1])
    r_bounds.append(xf)
    return l_bounds, r_bounds

def get_window(f, x0, xf):
    x = np.arange(x0, xf, 0.001)
    y = f(x)
    windxL = x0
    windxR = xf
    windyL = min(y)
    windyU = max(y)
    return windxL, windxR, windyL, windyU

def integrate(f, x0, xf, N, windxL, windxR):
    x = np.arange(x0, xf, 0.001)
    y = f(x)
    # Are all positive or regative?
    is_pos = all(i >= 0 for i in y)
    is_neg = all(i < 0 for i in y)

    if is_pos:
        # Get height of area.
        fmax = max(y)
        # Create random points.
        x_rand = x0 + np.random.random(N) * (xf - x0)
        y_rand = np.random.random(N) * fmax

        # When is the random point below the line?
        i_below = np.where(y_rand < f(x_rand))
        i_above = np.where(y_rand >= f(x_rand))


        # Probability of point being under the curve?
        prob = len(i_below[0])/N

        #AUC
        integral = prob * fmax * (xf - x0)

    elif is_neg:
        # Get height of area.
        fmin = min(y)
        # Create random points.
        x_rand = x0 + np.random.random(N) * (xf - x0)
        y_rand = np.random.random(N) * fmin

        # When is the random point below the line?
        i_below = np.where(y_rand > f(x_rand))
        i_above = np.where(y_rand <= f(x_rand))

        # Probability of point being under the curve?
        prob = len(i_below[0])/N

        #AUC
        integral = prob * fmin * (xf - x0)

    plt.scatter(x_rand[i_below], y_rand[i_below], color='green', s=1)
    plt.scatter(x_rand[i_above], y_rand[i_above], color='red', s=1)
    plt.axis(get_window(f, windxL, windxR))
    plt.show()

    return integral

def tot_integration(f, windxL, windxR, N):
    xL, xR = get_bounds(f, windxL, windxR)
    x_rand = []
    y_rand = []
    i_below = []
    i_above = []
    total_sum = 0
    show_fx_scatter(f, windxL, windxR)
    for l_bound, r_bound in zip(xL, xR):
        integral = integrate(f, l_bound, r_bound, N, windxL, windxR)
        total_sum += integral
    return total_sum

print(tot_integration(f, 0, 14, 100000))
# show_fx_scatter(f, 0, 14)



