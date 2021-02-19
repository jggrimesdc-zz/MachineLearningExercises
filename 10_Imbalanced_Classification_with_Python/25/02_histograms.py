# create histograms of numeric input variables
from matplotlib import pyplot
from pandas import read_csv

# define the dataset location
filename = 'phoneme.csv'
# load the csv file as a data frame
df = read_csv(filename, header=None)
# histograms of all variables
df.hist()
pyplot.show()
