# generate related variables
from matplotlib import pyplot
from numpy.random import rand
from numpy.random import seed

# seed random number generator
seed(1)
# prepare data
data1 = rand(1000) * 20
data2 = data1 + (rand(1000) * 10)
# plot
pyplot.scatter(data1, data2)
pyplot.show()
