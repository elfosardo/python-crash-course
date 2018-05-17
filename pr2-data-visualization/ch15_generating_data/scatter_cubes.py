from matplotlib import pyplot

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 8, 27, 64, 125]

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

pyplot.scatter(x_values, y_values, c=y_values, cmap=pyplot.cm.Reds, edgecolors='none', s=20)

pyplot.title("Cube Numbers", fontsize=24)
pyplot.xlabel("Value", fontsize=14)
pyplot.ylabel("Cube of Value", fontsize=14)

pyplot.tick_params(axis='both', which='major', labelsize=14)

pyplot.axis([0, 5100, 0, 150000000000])

pyplot.show()
