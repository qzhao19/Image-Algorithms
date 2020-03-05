# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 21:46:09 2020

@author: qizhao
"""

import numpy as np

def binarization(image, threshold):
    image[image < threshold] = 0
    image[image > threshold] = 255
    
    return image