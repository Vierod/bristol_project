from pix_mask_utils import *

test =extract_pixel_vals(["reference_images/bristol_reference_1.png","reference_images/bristol_reference_2.png"])

pixel_value_mask("bristol_tree.png","bristol_tree_output.png",test)