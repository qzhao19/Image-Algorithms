# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 23:42:41 2020

@author: qizhao
"""


import cv2
import numbers
import numpy as np



def _median_filter(img_in, ksize):
    """
    

    Parameters
    ----------
        img : ndarray of shape [height, width, channel]
            input image.
        ksize : int
            kernel size.

    Returns
    -------
    None.

    """


    if len(img_in.shape) == 3:
        img_h, img_w, img_c = img_in.shape
        
    else:
        img_in = np.expand_dims(img_in, axis=-1)
        img_h, img_w, img_c = img_in.shape

    # get height, width, and channel if image
    img_h, img_w, img_c = img_in.shape
    
    # zero padding, get padding size
    pad = ksize // 2
    img_out = np.zeros((img_h + pad * 2, img_w + pad * 2, img_c), 
                       dtype=np.float32)
    
    
    img_out[pad : pad + img_h, pad : pad + img_w, :] = img_in.copy().astype(np.float32)
    
     # temp image 
    tmp = img_out.copy()
    
    for y in range(img_h):
        for x in range(img_w):
            for z in range(img_c):
                img_out[y + pad, x + pad, z] = np.median(tmp[y : y + ksize, x : x + ksize, z])

    img_out = np.clip(img_out, 0, 255)
    
    img_out = img_out.astype(np.uint8) 
    
    return img_out

















