# generate random integer values
from numpy.random import randint
from numpy.random import seed

# seed random number generator
seed(1)
# generate some integers
values = randint(0, 10, 20)
print(values)
