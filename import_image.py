from scipy import misc
import matplotlib.pyplot as plt
import glob
import numpy as np

image = misc.imread("IMAGE FILE HERE")
print(image.shape[2])
#print(image[0])

for i in range(image.shape[0]):
    np.savetxt('image_array.txt', image[i])

plt.imshow(image)
plt.show()
