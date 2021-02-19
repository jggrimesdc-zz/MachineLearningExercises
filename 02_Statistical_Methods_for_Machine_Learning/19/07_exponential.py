# log-normal distribution
from matplotlib import pyplot
from numpy import exp
from numpy.random import randn
from numpy.random import seed

# seed the random number generator
seed(1)
# generate two sets of univariate observations
data = 5 * randn(100) + 50
# transform to be exponential
data = exp(data)
# histogram
pyplot.hist(data)
pyplot.show()
