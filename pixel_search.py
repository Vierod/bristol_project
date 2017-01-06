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
image = misc.imread("IMAGE GOES HERE")
#
# Render image
#
#plt.imshow(image)
#plt.show()
#
# Convert numpy array back to image and save
#


#New image that the tree pixels will be added to.
new_image = np.zeros(image.shape)



for x in range(image.shape[0]):
    for y in range(image.shape[1]):
        if image[x,y] == [1,2,3]:
            new_image[x,y] = image[x,y]
        else:
            pass

#image_png = Image.fromarray(image,'RGB')
#image_png.save('image.png')
