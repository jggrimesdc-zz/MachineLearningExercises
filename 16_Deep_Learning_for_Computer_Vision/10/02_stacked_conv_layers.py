# example of stacked convolutional layers
from keras.layers import Conv2D
from keras.models import Sequential

# create model
model = Sequential()
model.add(Conv2D(1, (3, 3), input_shape=(8, 8, 1)))
model.add(Conv2D(1, (3, 3)))
# summarize model
model.summary()
