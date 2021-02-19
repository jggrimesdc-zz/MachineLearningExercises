# plot the gaussian cdf
from matplotlib import pyplot
from numpy import arange
from scipy.stats import norm

# define the distribution parameters
sample_space = arange(-5, 5, 0.001)
# calculate the cdf
cdf = norm.cdf(sample_space)
# plot
pyplot.plot(sample_space, cdf)
pyplot.show()
