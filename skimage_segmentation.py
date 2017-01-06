
# coding: utf-8

# In[1]:

import sys, math
import numpy as np

from skimage import io
from skimage.color import rgb2lab, lch2lab
from skimage.segmentation import slic, quickshift, felzenszwalb


from sklearn import metrics
import matplotlib.pyplot as plt
from matplotlib import colors
import pylab
image_location = '/home/Alex/Desktop/bristol_project/bristol_tree_1.jpg'

sys.path.append('/home/Alex/Desktop/bristol_project/mplcursor')
import mpldatacursor

images = []


# In[2]:

tree_im_rgb = io.imread(image_location)
tree_im_lab = rgb2lab(tree_im_rgb)


# In[3]:

get_ipython().magic('matplotlib inline')
pylab.rcParams['figure.figsize'] = (20.0, 8.0)

col = ['Reds_r','Greens_r','Blues_r']

ff, ax = plt.subplots(1,3)
for i in range(3):
    ax[i].imshow(tree_im_rgb[:, :, i], interpolation = None, cmap = col[i])


# In[6]:

seg_trees = quickshift(tree_im_rgb, kernel_size=7, max_dist=3, ratio=0.35, convert2lab=False)
n_segments = len(np.unique(seg_trees))
print(n_segments)


# In[7]:

get_ipython().magic('matplotlib inline')
pylab.rcParams['figure.figsize'] = (40.0, 20.0)
cmap = colors.ListedColormap(np.random.rand(n_segments, 3))
ff, ax = plt.subplots(1,2)
ax[0].imshow(seg_trees, interpolation='none', cmap=cmap)
ax[1].imshow(tree_im_rgb)


# In[12]:

class UniqueDict(dict):
    def __setitem__(self, key, value):
        if key not in self:
            dict.__setitem__(self, key, value)
        else:
            raise KeyError("Key already exists")

segment_dict = UniqueDict()            
            
for x, row in enumerate(seg_trees):
    #
    for y, val in enumerate(row):
        try:
            segment_dict[val] = []
            segment_dict[val].append(tree_im_rgb[x,y])
        except KeyError:
            segment_dict[val].append(tree_im_rgb[x,y])
        


# In[22]:

segment_dict[220]


