# example of a bimodal data sample
from matplotlib import pyplot
from numpy import hstack
from numpy.random import normal

# generate a sample
sample1 = normal(loc=20, scale=5, size=300)
sample2 = normal(loc=40, scale=5, size=700)
sample = hstack((sample1, sample2))
# plot the histogram
pyplot.hist(sample, bins=50)
pyplot.show()
