# example of a line plot
from matplotlib import pyplot
from numpy import sin

# consistent interval for x-axis
x = [x * 0.1 for x in range(100)]
# function of x for y-axis
y = sin(x)
# create line plot
pyplot.plot(x, y)
# show line plot
pyplot.show()
