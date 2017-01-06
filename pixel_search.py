#
# Script that takes reference images and uses the pixel values in these to 
# apply a mask to an image. Here only pixel values that are present in the
# reference images are kept. All other pixels are changed to black.
#
from scipy import misc
import matplotlib.pyplot as plt
import glob
import numpy as np
#
# Read in image to numpy array
#
image = misc.imread("bristol_tree_1.png")
imageR1 = misc.imread("reference_images/bristol_reference_1.png")
imageR2 = misc.imread("reference_images/bristol_reference_2.png")
imageR = []
#
# New image that the tree pixels will be added to.

new_image = np.zeros(image.shape)
#
# What to search the image for - keeping unique values.
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
        if tuple(image[x,y,:]) in imageR:
            new_image[x,y,:] = image[x,y,:]
        else:
            new_image[x,y,:] = [255., 255., 255.]
#
# Write new image
#
misc.toimage(new_image, cmin=0.0, cmax=255.0).save('bristol_tree_output.png')
