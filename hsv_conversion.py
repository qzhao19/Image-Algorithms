# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 23:18:20 2020

@author: qizhao
"""


import cv2
import numpy as np




# BGR -> HSV
def BGR2HSV(image):
    """Convert bgr image to hsv image
    

    Parameters
    ----------
        image : TYPE
            DESCRIPTION.

    Returns
    -------
        None.

    """
    if not isinstance(image, np.float32):
        image = image.astype(np.float32)
    
    rgb_image = image.copy() / 255.
    
    hsv_image = np.zeros_like(rgb_image, dtype=np.float32)
    
    # get max et min value
    max_c = np.max(rgb_image, axis=2).copy()
    min_c = np.min(rgb_image, axis=2).copy()
    min_arg_c = np.argmin(rgb_image, axis=2)
    
    
    
    return rgb_image
    
    
    
if __name__ == "__main__":
    im = cv2.imread('./image/lenna.png')
    # print(im.dtype)
    
    h = np.zeros_like(im, dtype=np.float32)
    
    print(h[:, :, 0][5].shape)
    