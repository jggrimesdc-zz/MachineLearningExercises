# histogram plot of a low res sample
from matplotlib import pyplot
from numpy.random import randn
from numpy.random import seed

# seed the random number generator
seed(1)
# generate a univariate data sample
data = randn(100)
# remove decimal component
data = data.round(0)
# histogram
pyplot.hist(data)
pyplot.show()
