# histogram plot of data with a long tail
from matplotlib import pyplot
from numpy import append
from numpy.random import rand
from numpy.random import randn
from numpy.random import seed

# seed the random number generator
seed(1)
# generate a univariate data sample
data = 5 * randn(100) + 10
tail = 10 + (rand(10) * 100)
# add long tail
data = append(data, tail)
# trim values
data = [x for x in data if x < 25]
# histogram
pyplot.hist(data)
pyplot.show()
