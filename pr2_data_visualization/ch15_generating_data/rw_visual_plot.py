from matplotlib import pyplot
from random_walk import RandomWalk

while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk()
    rw.fill_walk()

    # Set the size of the plotting window.
    pyplot.figure(figsize=(12, 10))

    point_numbers = list(range(rw.num_points))

    pyplot.plot(rw.x_values, rw.y_values, linewidth=1)

    # Emphasize the first and last points.
    pyplot.scatter(0, 0, c='green', edgecolors='none', s=100)
    pyplot.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Remove the axes.
    pyplot.axes().get_xaxis().set_visible(False)
    pyplot.axes().get_yaxis().set_visible(False)

    pyplot.show()

    keep_running = input('Make another walk? (y/n)')
    if keep_running == 'n':
        break
