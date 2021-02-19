# create and plot an exponential time series
from math import exp

from matplotlib import pyplot

series = [exp(i) for i in range(1, 100)]
pyplot.figure(1)
# line plot
pyplot.subplot(211)
pyplot.plot(series)
# histogram
pyplot.subplot(212)
pyplot.hist(series)
pyplot.show()
