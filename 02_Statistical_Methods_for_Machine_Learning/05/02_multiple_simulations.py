# demonstration of the central limit theorem
from matplotlib import pyplot
from numpy import mean
from numpy.random import randint
from numpy.random import seed

# seed the random number generator
seed(1)
# calculate the mean of 50 dice rolls 1000 times
means = [mean(randint(1, 7, 50)) for _ in range(1000)]
# plot the distribution of sample means
pyplot.hist(means)
pyplot.show()
