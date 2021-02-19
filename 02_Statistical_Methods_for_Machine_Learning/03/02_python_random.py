# generate random floating point values
from random import random
from random import seed

# seed random number generator
seed(1)
# generate random numbers between 0-1
for _ in range(10):
    value = random()
    print(value)
