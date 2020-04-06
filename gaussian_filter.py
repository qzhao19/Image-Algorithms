# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 23:04:43 2020

@author: qizhao
"""


import cv2
import numpy as np

def _gaussian_fn(x, y, mu = 0, sigma = 1):
    """
    

    Parameters
    ----------
    x : float
        DESCRIPTION.
    y: float

    Returns
    -------
    None.

    """
    result = np.exp( -(x ** 2 + y ** 2) / (2 * (sigma ** 2)))
    
    
    return result


def gaussian_filter(img_path, ksize = 3, sigma = 1):
    """
    

    Parameters
    ----------
    img_path : TYPE
        DESCRIPTION.
    ksize : TYPE, optional
        DESCRIPTION. The default is 3.
    sigma : TYPE, optional
        DESCRIPTION. The default is 1.

    Returns
    -------
    None.

    """
    
    
    
    
    
    return 0
    
    
    
    
    
    
    
    
    
    
    
    
    
    