# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 21:46:09 2020

@author: qizhao
"""


def binarization(img_in, threshold=155):
    
    img = img_in.copy()
    
    img[img < threshold] = 0
    img[img > threshold] = 255
    
    return img

