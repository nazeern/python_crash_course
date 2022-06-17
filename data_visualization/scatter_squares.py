import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.viridis, 
    edgecolor='none', s=40)

x_values = list(range(1, 1001))
y_values = [x**3 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.viridis, 
    edgecolor='none', s=40)

# Chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set range for axis.
plt.axis([0, 1100, 0, 1100000000])

# Tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)

# Show the plot as an interactive
plt.show()

# Saves plot image to a file.
#bbox_inches trims whitespace.
# plt.savefig('squares_plot.png', bbox_inches='tight')