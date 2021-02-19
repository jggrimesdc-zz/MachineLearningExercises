# histogram plot of a small sample
from matplotlib import pyplot
from numpy.random import randn
from numpy.random import seed

# seed the random number generator
seed(1)
# generate a univariate data sample
data = 50 * randn(100) + 100
# histogram
pyplot.hist(data)
pyplot.show()
