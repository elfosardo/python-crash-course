import pygal
from die import Die

# Create 3 D6.
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides

for value in range(3, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)

# Visualize the results.
histogram = pygal.Bar()

histogram.title = 'Results of rolling three D6 50,000 times.'
histogram.x_labels = [x for x in range(3, max_result+1)]
histogram.x_title = 'Result'
histogram.y_title = 'Frequency of Result'

histogram.add('D6 + D6 + D6', frequencies)
histogram.render_to_file('3d6_visual.svg')
