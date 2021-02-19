# example of simple cnn model
from keras.layers import Conv2D
from keras.models import Sequential

# create model
model = Sequential()
model.add(Conv2D(512, (3, 3), padding='same', activation='relu', input_shape=(256, 256, 3)))
# summarize model
model.summary()
