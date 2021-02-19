# generate random integer values
from random import randint
from random import seed

# seed random number generator
seed(1)
# generate some integers
for _ in range(10):
    value = randint(0, 10)
    print(value)
