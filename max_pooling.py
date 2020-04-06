# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 23:02:07 2020

@author: qizhao
"""



import cv2
import numpy as np


def max_pooling(img_path, pool_size=8):
    """
        
    Parameters
    ----------
    img_path : TYPE
        DESCRIPTION.
    pool_size : TYPE, optional
        DESCRIPTION. The default is 8.

    Returns
    -------
    None.

    """
    
    try:
        img_in = cv2.imread(img_path)
        img_in = cv2.cvtColor(img_in, cv2.COLOR_BGR2RGB)
    except:
        raise ValueError('Cannot read image, check input path!')
    
    img_out = img_in.copy()
    
    img_h, img_w, img_c = img_in.shape
    
    N_h, N_w = int(img_h / pool_size), int(img_w / pool_size)
    
    for x in range(N_h):
        for y in range(N_w):
            for c in range(img_c):
                img_out[pool_size * x : pool_size * (x + 1), 
                        pool_size * y : pool_size * (y + 1), c] = np.max(img_out[pool_size * x : pool_size * (x + 1), 
                                                                                  pool_size * y : pool_size * (y + 1), c]).astype(np.int8)
                    
    return img_out

