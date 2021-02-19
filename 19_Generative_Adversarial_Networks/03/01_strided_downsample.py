# example of downsampling with strided convolutions
from keras.layers import Conv2D
from keras.models import Sequential

# define model
model = Sequential()
model.add(Conv2D(64, (3, 3), strides=(2, 2), padding='same', input_shape=(64, 64, 3)))
# summarize model
model.summary()
