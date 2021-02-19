# example of gaussian weight initialization in a generator model
from keras.initializers import RandomNormal
from keras.layers import Conv2DTranspose
from keras.models import Sequential

# define model
model = Sequential()
init = RandomNormal(mean=0.0, stddev=0.02)
model.add(Conv2DTranspose(64, (4, 4), strides=(2, 2), padding='same', kernel_initializer=init, input_shape=(64, 64, 3)))
