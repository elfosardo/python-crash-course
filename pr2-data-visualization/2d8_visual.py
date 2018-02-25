import pygal
from die import Die

# Create a D6.
die_1 = Die(8)
die_2 = Die(8)

# Make some rolls, and store results in a list.
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides

for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)

# Visualize the results.
histogram = pygal.Bar()

histogram.title = 'Results of rolling two D8 50,000 times.'
histogram.x_labels = [x for x in range(2, max_result+1)]
histogram.x_title = 'Result'
histogram.y_title = 'Frequency of Result'

histogram.add('D8 + D8', frequencies)
histogram.render_to_file('2d8_visual.svg')
