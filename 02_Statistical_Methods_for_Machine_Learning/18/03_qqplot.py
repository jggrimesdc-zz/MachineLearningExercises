# q-q plot
from matplotlib import pyplot
from numpy.random import randn
from numpy.random import seed
from statsmodels.graphics.gofplots import qqplot

# seed the random number generator
seed(1)
# generate univariate observations
data = 5 * randn(100) + 50
# q-q plot
qqplot(data, line='s')
pyplot.show()
