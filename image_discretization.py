# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 22:28:04 2020

@author: qizhao
"""


# import cv2
import numpy as np

def discretization(img_in):
    """Image discretization of color
    

    Parameters
    ----------
        img_in : ndarray
            input image.

    Returns
    -------
        output image

    """
    
    if not isinstance(img_in, np.ndarray):
        raise ValueError('Input image need to be an array type')
        
    img_out = img_in.copy()
    
    for i in range(4):
        idx = np.where(((64 * i - 1) <= img_out) & ((64 * (i + 1) - 1)))
        img_out[idx] = 32 * (2 * 1 + 1)
        
    return img_out