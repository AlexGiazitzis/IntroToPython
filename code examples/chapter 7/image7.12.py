import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

im = Image.open("landscape.jpg")
plt.imshow(im)
# removes the axes from the plot
plt.axis("off")
plt.show(block=False)

# get a numpy.ndarray from the image
# the returned array is a 3D one
# due to the picture format
imarr = np.array(im)

# mean value of the image over Z axis
# returns an array with the size of the first
# two dimensions of the original array
gray = imarr.mean(axis=2)

plt.figure()
plt.subplot(1, 2, 1)
plot = plt.imshow(gray)
plt.colorbar(plot)
plt.title("Heatmap")
plt.axis("off")

plt.subplot(1, 2, 2)
# display the image as the proper gray scale image
plt.imshow(gray, cmap="gray")
plt.title("Gray-scaled")
plt.axis("off")

plt.show()
