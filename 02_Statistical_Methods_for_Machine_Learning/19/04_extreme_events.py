# histogram plot of data with outliers
from matplotlib import pyplot
from numpy import append
from numpy import zeros
from numpy.random import randn
from numpy.random import seed

# seed the random number generator
seed(1)
# generate a univariate data sample
data = 5 * randn(100) + 10
# add extreme values
data = append(data, zeros(10))
# histogram
pyplot.hist(data)
pyplot.show()
