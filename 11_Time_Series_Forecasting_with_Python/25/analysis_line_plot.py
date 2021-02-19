# line plots of time series
from matplotlib import pyplot
from pandas import read_csv

series = read_csv('dataset.csv', header=None, index_col=0, parse_dates=True, squeeze=True)
series.plot()
pyplot.show()
