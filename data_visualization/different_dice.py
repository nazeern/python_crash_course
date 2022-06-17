from die import Die 
import pygal

# Initialize D6 die.
die1 = Die()
die2 = Die(10)

# Create rolls and store in a list
results = []
for roll_num in range(50000):
    result = die1.roll() + die2.roll()
    results.append(result)

# Analyze results.
frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling a D6 and D10 50,000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
    '13', '14', '15', '16']
hist.x_title = "Result"
hist.y_title = "Frequency of result"

# Pass label and list of values to graph.
hist.add('D6 + D10', frequencies)
# renders to SVG, so pass .svg file extension.
hist.render_to_file('different_dice_visual.svg')
