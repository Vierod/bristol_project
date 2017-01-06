#
# Script for reading and writing images
#
from scipy import misc
import matplotlib.pyplot as plt
import glob
import numpy as np
from PIL import Image
#
# Read in image to numpy array
#
image = misc.imread("imageWR.png")
#
# Render image
#
#plt.imshow(image)
#plt.show()
#
# Convert numpy array back to image and save
#
# New image that the tree pixels will be added to.
new_image = np.zeros(image.shape)
#
# What to search the image for.
test = np.array([255,255,255])
#
# Search through image for test pixels and put them into new_image
for x in range(image.shape[0]):
    for y in range(image.shape[1]):
        if np.array_equal(image[x,y,:] , test):
            new_image[x,y] = image[x,y]
        else:
            pass
#
# Write new image.
misc.toimage(new_image, cmin=0.0, cmax=1.0).save('new_imageWR.png')
