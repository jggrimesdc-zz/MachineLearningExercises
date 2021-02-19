# example of upsampling with strided convolutions
from keras.layers import Conv2DTranspose
from keras.models import Sequential

# define model
model = Sequential()
model.add(Conv2DTranspose(64, (4, 4), strides=(2, 2), padding='same', input_shape=(64, 64, 3)))
# summarize model
model.summary()
