# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 21:38:01 2020

@author: qizhao
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_image(image):
    plt.figure()
    plt.imshow(image)
    plt.show()
    # plt.close()