def pixel_value_mask(image, out_file, pix_vals, mono=False, blk_inc=True):
    """
    A function that masks an image keeping only pixels with specified RGB values
    
    Usage: pixel_value_mask(image,out_file,pix_values, mono=False)
	   
	image:    An image file name as a string. This is the file the mask will be 
              applied to. Only guaranteed to work if this format matches the 
              format of the pixel values supplied - !built for 24 bit png!
    out_file: File name for output image as a string.
    pix_vals: A list of tuples, each representing RGB pixel values to be kept. 
              Must be same format as supplied image. Can be created from 
              reference images with extract_pixels_vals
    mono:     A boolean input deciding if output should monochrome instead of
              retaining original colours. (Kept pixels will be black)
    
    returns: Nothing, ouput is saved to specified path
    """
    
    from scipy import misc
    import numpy as np
    
    im = misc.imread(image)
    
    new_img = np.full(im.shape,255.)
    
    if blk_inc == True:    
        for x in range(im.shape[0]):
            for y in range(im.shape[1]):
                if tuple(im[x,y,:]) in pix_vals:
                    new_img[x,y,:] = im[x,y,:]
                else:
                   pass
    else:
        for x in range(im.shape[0]):
            for y in range(im.shape[1]):
                if tuple(im[x,y,:]) == (0., 0., 0.):
                    pass
                if tuple(im[x,y,:]) in pix_vals:
                    new_img[x,y,:] = im[x,y,:]
                else:
                   pass
    
    if mono == False:
        misc.toimage(new_img, cmin=0.0, cmax=255.0).save(out_file)
    else:
        misc.toimage(new_img, cmin=254.5, cmax=255.0).save(out_file)
		
def extract_pixel_vals(ref_img_list):
    """
    A function that produces a list of unique pixel values for a set of images
	   
    Usage: extract_pixel_vals(ref_img_list)
    
	ref_img_list:    A list of image file names as strings.
                     !built for 24 bit png!

    
    returns: List conatining unique pixel RGB values as tuples
    """
    from scipy import misc
    import numpy as np
    
    imRef = []
    for ref in range(len(ref_img_list)):
        tmpRef = misc.imread(ref_img_list[ref])
        for i in range(tmpRef.shape[0]):
            for j in range(tmpRef.shape[1]):
                imRef.append(tuple(tmpRef[i,j,:]))
    
    test = set(imRef)
    
    return test