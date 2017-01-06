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
image = misc.imread("bristol_tree_1.jpg")
imageR1 = misc.imread("bristol_reference_1.png")
imageR2 = misc.imread("bristol_reference_1.png")
imageR = []
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
for i in range(imageR1.shape[0]):
    for j in range(imageR1.shape[1]):
        imageR.append(tuple(imageR1[i,j,:]))

for i in range(imageR2.shape[0]):
    for j in range(imageR2.shape[1]):
        imageR.append(tuple(imageR2[i,j,:]))

test = set(imageR)
#
# Search through image for test pixels and put them into new_image
for x in range(image.shape[0]):
    for y in range(image.shape[1]):
        if tuple(image[x,y,:]) in test:
            new_image[x,y] = image[x,y]
        else:
            pass
#
# Write new image.
misc.toimage(new_image, cmin=0.0, cmax=1.0).save('bristol_tree_output.png')
