# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 23:18:20 2020

@author: qizhao
"""


import cv2
import numpy as np
import matplotlib.pyplot as plt




# BGR -> HSV
def BGR2HSV(image_in):
    """Convert bgr image to hsv image
    

    Parameters
    ----------
        image_in : int8 of shape [h, w, c]
            DESCRIPTION.

    Returns
    -------
        None.

    """
    if not isinstance(image_in, np.float32):
        image_in = image_in.astype(np.float32)
    
    rgb = image_in.copy() / 255.
    
    hsv = np.zeros_like(rgb, dtype=np.float32)
    
    # get max et min value
    max_vals = np.max(rgb, axis=2).copy()
    min_vals = np.min(rgb, axis=2).copy()
    min_args = np.argmin(rgb, axis=2)
    
    # h
    hsv[:, :, 0][np.where(max_vals == min_vals)] = 0
    
    ## if min_vals = B
    indices = np.where(min_args == 0)
    hsv[:, :, 0][indices] = 60 * (rgb[:, :, 1][indices] - rgb[:, :, 2][indices]) / (max_vals[indices] - min_vals[indices]) + 60

    ## if min = G
    indices = np.where(min_args == 1)
    hsv[:, :, 0][indices] = 300 * (rgb[:, :, 2][indices] - rgb[:, :, 0][indices]) / (max_vals[indices] - min_vals[indices]) + 300
    
    ## if min = R
    indices = np.where(min_args == 2)
    hsv[:, :, 0][indices] = 180 * (rgb[:, :, 0][indices] - rgb[:, :, 1][indices]) / (max_vals[indices] - min_vals[indices]) + 180
    
    # S
    hsv[:, :, 1] = max_vals.copy() - min_vals.copy()
    
    # V
    hsv[:, :, 2] = max_vals.copy()
    
    return hsv
    

def HSV2BGR(img_in, hsv):
    """
    

    Parameters
    ----------
    image_in : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    img = img_in.copy() / 255.

	# get max and min
	max_v = np.max(img, axis=2).copy()
	min_v = np.min(img, axis=2).copy()

	out = np.zeros_like(img)

	H = hsv[..., 0]
	S = hsv[..., 1]
	V = hsv[..., 2]

	C = S
	H_ = H / 60.
	X = C * (1 - np.abs( H_ % 2 - 1))
	Z = np.zeros_like(H)

	vals = [[Z,X,C], [Z,C,X], [X,C,Z], [C,X,Z], [C,Z,X], [X,Z,C]]

	for i in range(6):
		ind = np.where((i <= H_) & (H_ < (i+1)))
		out[..., 0][ind] = (V - C)[ind] + vals[i][0][ind]
		out[..., 1][ind] = (V - C)[ind] + vals[i][1][ind]
		out[..., 2][ind] = (V - C)[ind] + vals[i][2][ind]

	out[np.where(max_v == min_v)] = 0
	out = np.clip(out, 0, 1)
	out = (out * 255).astype(np.uint8)

	return out

    
# if __name__ == "__main__":
#     im = cv2.imread('./image/lenna.png')
    
#     out1 = BGR2HSV(im)
#     # out2 = BGR2HSV2(im)
#     # print(out)
    
#     fig = plt.figure()
#     # plt.subplot(121)
#     plt.imshow(out1)
#     plt.title('out1') 
#     # plt.subplot(122)
#     # plt.imshow(out2)
#     # plt.title('out2') 
#     plt.show()
    
    