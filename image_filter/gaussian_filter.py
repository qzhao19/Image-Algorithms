# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 23:04:43 2020

@author: qizhao
"""


import cv2
import numbers
import numpy as np
from utils.utils import display_image

def _gaussian_fn(x, y, sigma):
    """compute 2D gaussian function
    
    Parameters
    ----------
        x : TYPE
            DESCRIPTION.
        y : TYPE
            DESCRIPTION.
        sigma : TYPE
            DESCRIPTION. The default is 1.5.

    Returns
    -------
        result : float
            gaussian function value.

    """
    
    # result = np.exp( -(x ** 2 + y ** 2) / (2 * (sigma ** 2)))

    result = (1 / (2 * np.pi * np.power(sigma, 2))) * \
        np.exp(-(np.power(x, 2) + np.power(y, 2)) / (2 * np.power(sigma, 2)))   
    
    return result


def _gaussian_kernel(ksize, sigma):
    """
    

    Parameters
    ----------
        ksize : TYPE
            DESCRIPTION.
        sigma : TYPE
            DESCRIPTION.

    Returns
    -------
    kernel : TYPE
        DESCRIPTION.

    """
    
    pad = ksize // 2
    kernel = np.zeros((ksize, ksize), dtype=np.float32)
    
    for y in range(-pad, -pad + ksize):
        for x in range(-pad, -pad + ksize):
            kernel[y + pad, x + pad] = _gaussian_fn(x, y, sigma=sigma)
    
    kernel /= kernel.sum()
    
    return kernel


def _gaussian_filter(img_in, ksize, sigma):
    """Compute gaussian filter

    Parameters
    ----------
        img_in : np.ndarray
            input image of shape [height, width, channel].
        ksize : int
            kernel size.
        sigma : float
            standard deviation.

    Returns
    -------
    None.

    """
    
    
    if len(img_in.shape) == 3:
        img_h, img_w, img_c = img_in.shape
        
    else:
        img_in = np.expand_dims(img_in, axis=-1)
        img_h, img_w, img_c = img_in.shape
        
    
    # zeros padding
    pad = ksize // 2
    img_out = np.zeros((img_h + pad * 2, img_w + pad * 2, img_c), dtype=np.float32)
    img_out[pad : pad + img_h, pad : pad + img_w, :] = img_in.copy().astype(np.float32)    
    
    # temp image 
    tmp = img_out.copy()
    
    
    # prepare kernel
    kernel = _gaussian_kernel(ksize, sigma)
    
    for y in range(img_h):
        for x in range(img_w):
            for z in range(img_c):
                img_out[y + pad, x + pad, z] = np.sum(kernel * tmp[y : y + ksize, x : x + ksize, z])
    
    img_out = np.clip(img_out, 0, 255)
    
    img_out = img_out[pad : pad + img_h, pad : pad + img_w, :].astype(np.uint8)
    
    return img_out
    
    
    
def gaussian_filter(img_path, ksize = 3, sigma = 1.5):
    """
    

    Parameters
    ----------
        img_path : strings
            input image path.
            
        ksize : int, optional
            kernel size. The default is 3.
        sigma : integer, optional
            DESCRIPTION. The default is 1.5.

    Raises
    ------
        ValueError
            DESCRIPTION.

    Returns
    -------
        result.

    """
    if not isinstance(ksize, numbers.Number):
        raise ValueError('{} is not an Integer')
        
    else:
        if not isinstance(ksize, int):
            ksize = int(ksize)
            
    if not isinstance(sigma, numbers.Number):
        raise ValueError('{} is not an Integer')
     
    
    try:
        img_in = cv2.imread(img_path)
    except:
        raise ValueError('Cannot read image from {}, check input path!'.format(img_path))
    
    
    if len(img_in.shape) == 1:
        img_in = cv2.cvtColor(img_in, cv2.COLOR_GRAY2RGB)
    elif len(img_in.shape) == 3:
        img_in = cv2.cvtColor(img_in, cv2.COLOR_BGR2RGB)
    else:
        raise ValueError('The dimensions of image must be one or three '
                         'but got %s' %str(len(img_in.shape)))
        
    
    if not isinstance(img_in, np.ndarray):
        img_in = np.asarray(img_in)
    
    if img_in.dtype.type != np.float32:
        img_in = img_in.astype(np.float32)
    
    
    result = _gaussian_filter(img_in, ksize, sigma)
    
    
    return result   
    
    
if __name__ == '__main__':
    res = gaussian_filter('./image/lenna.png')
    display_image(res)   
    
    
    
    