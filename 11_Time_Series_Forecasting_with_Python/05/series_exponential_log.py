# log transform a contrived exponential time series
from math import exp

from matplotlib import pyplot
from numpy import log

series = [exp(i) for i in range(1, 100)]
transform = log(series)
pyplot.figure(1)
# line plot
pyplot.subplot(211)
pyplot.plot(transform)
# histogram
pyplot.subplot(212)
pyplot.hist(transform)
pyplot.show()
