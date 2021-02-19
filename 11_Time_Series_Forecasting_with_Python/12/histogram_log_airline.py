# histogram and line plot of log transformed time series
from matplotlib import pyplot
from numpy import log
from pandas import read_csv

series = read_csv('airline-passengers.csv', header=0, index_col=0, parse_dates=True, squeeze=True)
X = series.values
X = log(X)
pyplot.hist(X)
pyplot.show()
pyplot.plot(X)
pyplot.show()
