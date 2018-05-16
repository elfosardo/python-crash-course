import pygal
from die import Die

# Create a D6 and a D10
die_1 = Die()
die_2 = Die(10)

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

histogram.title = 'Results of rolling a D6 and a D10 50,000 times.'
histogram.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
                      '13', '14', '15', '16']
histogram.x_title = 'Result'
histogram.y_title = 'Frequency of Result'

histogram.add('D6 + D10', frequencies)
histogram.render_to_file('different_dice.svg')
