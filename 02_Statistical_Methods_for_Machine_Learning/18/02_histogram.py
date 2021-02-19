# histogram plot
from matplotlib import pyplot
from numpy.random import randn
from numpy.random import seed

# seed the random number generator
seed(1)
# generate univariate observations
data = 5 * randn(100) + 50
# histogram plot
pyplot.hist(data)
pyplot.show()
