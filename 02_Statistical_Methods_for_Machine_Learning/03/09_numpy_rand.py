# generate random floating point values
from numpy.random import rand
from numpy.random import seed

# seed random number generator
seed(1)
# generate random numbers between 0-1
values = rand(10)
print(values)
