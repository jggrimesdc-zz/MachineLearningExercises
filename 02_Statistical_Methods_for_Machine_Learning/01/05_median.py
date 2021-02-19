# calculate the median of a sample
from numpy import median
from numpy.random import randn
from numpy.random import seed

# seed the random number generator
seed(1)
# generate univariate observations
data = 5 * randn(10000) + 50
# calculate median
result = median(data)
print('Median: %.3f' % result)
