# boxplots of time series
from matplotlib import pyplot
from pandas import DataFrame
from pandas import Grouper
from pandas import read_csv

series = read_csv('dataset.csv', header=None, index_col=0, parse_dates=True, squeeze=True)
print(series)
groups = series['1966':'1973'].groupby(Grouper(freq='A'))
years = DataFrame()
for name, group in groups:
    years[name.year] = group.values
years.boxplot()
pyplot.show()
