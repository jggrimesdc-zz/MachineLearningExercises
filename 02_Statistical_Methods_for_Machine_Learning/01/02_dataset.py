# generate a sample of random gaussians
from matplotlib import pyplot
from numpy.random import randn
from numpy.random import seed

# seed the random number generator
seed(1)
# generate univariate observations
data = 5 * randn(10000) + 50
# histogram of generated data
pyplot.hist(data)
pyplot.show()
