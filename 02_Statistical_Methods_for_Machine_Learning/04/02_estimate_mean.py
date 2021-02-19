# demonstrate the law of large numbers
from matplotlib import pyplot
from numpy import array
from numpy import mean
from numpy.random import randn
from numpy.random import seed

# seed the random number generator
seed(1)
# sample sizes
sizes = list()
for x in range(10, 20000, 200):
    sizes.append(x)
# generate samples of different sizes and calculate their means
means = [mean(5 * randn(size) + 50) for size in sizes]
# plot sample mean error vs sample size
pyplot.scatter(sizes, array(means) - 50)
pyplot.show()
