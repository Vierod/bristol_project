def pixel_value_mask(image, out_file, pix_vals, mono=False):
    """A function to use the v"""
    from scipy import misc
    import numpy as np
    
    im = misc.imread(image)

    new_img = np.zeros(im.shape)
    
    for x in range(im.shape[0]):
        for y in range(im.shape[1]):
            if tuple(im[x,y,:]) in pix_vals:
                new_img[x,y,:] = im[x,y,:]
            else:
                new_img[x,y,:] = [255., 255., 255.]
    if mono == False:
        misc.toimage(new_img, cmin=0.0, cmax=255.0).save(out_file)
    else:
        misc.toimage(new_img, cmin=0.0, cmax=1.0).save(out_file)