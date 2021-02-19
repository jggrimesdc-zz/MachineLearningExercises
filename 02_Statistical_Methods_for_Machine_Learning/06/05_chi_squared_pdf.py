# plot the chi-squared pdf
from matplotlib import pyplot
from numpy import arange
from scipy.stats import chi2

# define the distribution parameters
sample_space = arange(0, 50, 0.01)
dof = 20
# calculate the pdf
pdf = chi2.pdf(sample_space, dof)
# plot
pyplot.plot(sample_space, pdf)
pyplot.show()
