import sys, math
import numpy as np
import glob, copy

from skimage import io
from skimage.segmentation import quickshift

import matplotlib.pyplot as plt
from matplotlib import colors
import pylab

class UniqueDict(dict):
    def __setitem__(self, key, value):
        if key not in self:
            dict.__setitem__(self, key, value)
        else:
            raise KeyError("Key already exists")

def match_segments(seg_dict, ref_pixels, threshold):
    """ Identify segments containing reference pixels """
    matched_segments = []
    for key, rgb_list in seg_dict.items():
        thresh = 0
        for pixel in rgb_list:
            if pixel in ref_pixels:
                thresh+=1
        if thresh >= len(rgb_list)*threshold:
            matched_segments.append(key)
    return matched_segments
                    
def reclass_segments(segments, matched):
    """ Reclassify segments according to matches """
    new_image = np.zeros(segments.shape)
    for x, row in enumerate(segments):
        for y, val in enumerate(row):
            if val in matched:
                new_image[x,y] = 1
    return new_image
            

class tree_classifier(object):
    """ Detects trees in images according to reference image pixel values """
    def __init__(self, im_location, ref_locations, iterations = 5, threshold = 0.1, verbose = True):
        
        # Load image and reference images
        self.im2class = io.imread(im_location)
        self.ref_images = [io.imread(l) for l in ref_locations]
        
        # Apply quickshift image segmentation algorithm
        self.segments = quickshift(self.im2class, kernel_size=7, max_dist=3, ratio=0.35, convert2lab=False)
        self.n_segments = len(np.unique(self.segments))
        if verbose: print("Detected ",self.n_segments," in input image.")
            
        # Use unique dictionary to create list of pixels within each segment
        self.segment_dict = UniqueDict()
        for x, row in enumerate(self.segments):
            for y, val in enumerate(row):
                try:
                    self.segment_dict[val] = []
                    self.segment_dict[val].append(tuple(self.im2class[x,y]))
                except KeyError:
                    self.segment_dict[val].append(tuple(self.im2class[x,y]))
         
        # Create unique set of reference pixels
        self.ref_pixels = []
        for im in self.ref_images:
            for row in im:
                for val in row:
                    self.ref_pixels.append(tuple(val))
        self.ref_pixels = set(self.ref_pixels)
        self.ref_pixels.discard((0,0,0))
                
        self.matched_segments = match_segments(self.segment_dict, self.ref_pixels, threshold)
        self.treeclass_image =reclass_segments(self.segments, self.matched_segments)
