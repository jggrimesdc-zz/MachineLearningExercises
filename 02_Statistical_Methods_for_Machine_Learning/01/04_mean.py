# calculate the mean of a sample
from numpy import mean
from numpy.random import randn
from numpy.random import seed

# seed the random number generator
seed(1)
# generate univariate observations
data = 5 * randn(10000) + 50
# calculate mean
result = mean(data)
print('Mean: %.3f' % result)
