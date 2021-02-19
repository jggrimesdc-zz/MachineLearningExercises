# box-cox transform
from matplotlib import pyplot
from numpy import exp
from numpy.random import randn
from numpy.random import seed
from scipy.stats import boxcox

# seed the random number generator
seed(1)
# generate two sets of univariate observations
data = 5 * randn(100) + 100
# transform to be exponential
data = exp(data)
# power transform
data = boxcox(data, 0)
# histogram
pyplot.hist(data)
pyplot.show()
