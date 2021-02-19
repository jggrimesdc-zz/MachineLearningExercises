# plot the chi-squared cdf
from matplotlib import pyplot
from numpy import arange
from scipy.stats import chi2

# define the distribution parameters
sample_space = arange(0, 50, 0.01)
dof = 20
# calculate the cdf
cdf = chi2.cdf(sample_space, dof)
# plot
pyplot.plot(sample_space, cdf)
pyplot.show()
