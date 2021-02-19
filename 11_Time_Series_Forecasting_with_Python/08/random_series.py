# create and plot a random series
from random import randrange
from random import seed

from matplotlib import pyplot

seed(1)
series = [randrange(10) for i in range(1000)]
pyplot.plot(series)
pyplot.show()
