# -*- coding: utf-8 -*-
"""
Created on Sun May  3 23:23:09 2020

@author: qizhao
"""


import cv2
import numbers
import numpy as np



class MotionFilter(object):
    """Motion filter
    
    Parameters
    ----------
        ksize : int
            kernel size.

    Returns
    -------
        ndarray of shape [h, w, c].

    """
    
    def __init__(self, ksize=3):
        self.ksize = ksize
    
    def _kernel(self):
        """generate motion kernel
        

        Returns
        -------
        None.

        """
        
        kernel = np.diag([1] * self.ksize)
        kernel /= self.ksize
        
        self.kernel = kernel

    def _filter(self, img_in):
        """
        
        Parameters
        ----------
        img_in : float32 ndarray of shape [height, width, channel]
            input image.

        Returns
        -------
            None.

        """
        
        pad = self.ksize // 2
        
        img_h, img_w, img_c = img_in.shape
        
        img_out = np.zeros((img_h + pad * 2, img_w + pad * 2, img_c), 
                           dtype=np.float32)
        
        
        img_out[pad : img_h + pad, pad: img_w + pad, :] = img_in.copy()
        
        tmp = img_out.copy()
        
        for h in range(img_h):
            for w in range(img_w):
                for c in range(img_c):
                    img_out[h + pad, w + pad, c] = \
                    np.sum(self.kernel * tmp[h : h + self.ksize, w : w + sel.ksize, :])
        
        
        img_out = np.clip(img_out, 0, 255)
        img_out = img_out[pad : pad + img_h, 
                          pad : pad + img_w, :].astype(np.float32)
        
        self.img_out = img_out
    
    def fit(self, img_in):
        """
        

        Parameters
        ----------
        img_in : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        self._kernel()
        
        self._filter(img_in)
        
        img_out = self.img_out
        
        return img_out
        


















