from matplotlib import pyplot

# pyplot.scatter(2, 4, s=200)

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# pyplot.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolors='none', s=40)
pyplot.scatter(x_values, y_values, c=y_values, cmap=pyplot.cm.Blues, edgecolors='none', s=40)

pyplot.title("Square Numbers", fontsize=24)
pyplot.xlabel("Value", fontsize=14)
pyplot.ylabel("Square of Value", fontsize=14)

pyplot.tick_params(axis='both', which='major', labelsize=14)

pyplot.axis([0, 1100, 0, 1100000])

# pyplot.show()
pyplot.savefig('squares_plot.png', bbox_inches='tight')
