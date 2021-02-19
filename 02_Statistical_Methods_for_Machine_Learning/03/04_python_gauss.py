# generate random Gaussian values
from random import gauss
from random import seed

# seed random number generator
seed(1)
# generate some Gaussian values
for _ in range(10):
    value = gauss(0, 1)
    print(value)
