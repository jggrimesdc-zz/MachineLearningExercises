# generate random dice rolls
from numpy import mean
from numpy.random import randint
from numpy.random import seed

# seed the random number generator
seed(1)
# generate a sample of die rolls
rolls = randint(1, 7, 50)
print(rolls)
print(mean(rolls))
