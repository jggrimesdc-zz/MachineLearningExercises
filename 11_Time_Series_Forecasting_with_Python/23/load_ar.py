# load the AR model from file
import numpy
from statsmodels.tsa.ar_model import AutoRegResults

loaded = AutoRegResults.load('ar_model.pkl')
print(loaded.params)
data = numpy.load('ar_data.npy')
last_ob = numpy.load('ar_obs.npy')
print(last_ob)
