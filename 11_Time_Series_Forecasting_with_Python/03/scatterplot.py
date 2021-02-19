# create a scatter plot
from matplotlib import pyplot
from pandas import read_csv
from pandas.plotting import lag_plot

series = read_csv('daily-minimum-temperatures.csv', header=0, index_col=0, parse_dates=True, squeeze=True)
lag_plot(series)
pyplot.show()
