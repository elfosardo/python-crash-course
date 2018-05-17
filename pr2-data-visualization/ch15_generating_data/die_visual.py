import pygal
from die import Die

# Create a D6.
die = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze the results.
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)

# Visualize the results.
histogram = pygal.Bar()

histogram.title = "Results of rolling one D6 1000 times."
histogram.x_labels = [x for x in range(1, die.num_sides+1)]
histogram.x_title = "Result"
histogram.y_title = "Frequency of Result"

histogram.add('D6', frequencies)
histogram.render_to_file('die_visual.svg')
