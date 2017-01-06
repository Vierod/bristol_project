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
plt.imshow(image)
plt.show()
#
# Convert numpy array back to image and save
#
image_png = Image.fromarray(image,'RGB')
image_png.save('image.png')
