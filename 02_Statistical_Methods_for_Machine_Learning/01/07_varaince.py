# calculate the variance of a sample
from numpy import var
from numpy.random import randn
from numpy.random import seed

# seed the random number generator
seed(1)
# generate univariate observations
data = 5 * randn(10000) + 50
# calculate variance
result = var(data)
print('Variance: %.3f' % result)
