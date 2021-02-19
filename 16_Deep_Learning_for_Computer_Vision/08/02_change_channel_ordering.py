# change image from channels last to channels first format
from PIL import Image
from numpy import asarray
from numpy import moveaxis

# load the color image
img = Image.open('penguin_parade.jpg')
# convert to numpy array
data = asarray(img)
print(data.shape)
# change channels last to channels first format
data = moveaxis(data, 2, 0)
print(data.shape)
# change channels first to channels last format
data = moveaxis(data, 0, 2)
print(data.shape)
