# multiple line plots of time series
from matplotlib import pyplot
from pandas import DataFrame
from pandas import Grouper
from pandas import read_csv

series = read_csv('dataset.csv', header=None, index_col=0, parse_dates=True, squeeze=True)
groups = series['1964':'1970'].groupby(Grouper(freq='A'))
years = DataFrame()
pyplot.figure()
i = 1
n_groups = len(groups)
for name, group in groups:
    pyplot.subplot((n_groups * 100) + 10 + i)
    i += 1
    pyplot.plot(group)
pyplot.show()
