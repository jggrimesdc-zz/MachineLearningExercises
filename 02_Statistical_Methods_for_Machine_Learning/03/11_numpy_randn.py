# generate random Gaussian values
from numpy.random import randn
from numpy.random import seed

# seed random number generator
seed(1)
# generate some Gaussian values
values = randn(10)
print(values)
