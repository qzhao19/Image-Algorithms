import math
import copy
import pylab 
import random
import numpy as np
from PIL import Image


class ImageNoise(object):
    """Class GenerateImageNoise allows to generate image noise, there are 2 type noise: gaussian noise and salt&pepper noise 
       Attributs:
           src_im: an 2D array containing input sorce image which is no-noise image
       Method:
           gaussNoise: gaussian noise image
           saltPepperNoise: 
    """
    def __init__(self, src_im):
        self.src_im=np.array(src_im, dtype=float)
        
    def gaussNoise(self, snr_db=3):
        """Function gaussNoise allows to generate gaussain noise and add these into source image
           Parameters:
               rsb: SNR(db) signal-to-noise ration be expressed  in decibels, that compares the level of a desired signal 
               to the level of background noise.
           Returns:
               noise_im: image noised that is the image added gaussain noise
        """
        # calculate source image variance 
        # SNR=var(image)/var(noise)
        # SNR(db)=10*log(SNR) ==> SNR=10**(SNR(db)/10)
        im_var=np.var(self.src_im)
        noise_var=im_var/(10**(snr_db/10))
        # get square root of noise
        sigma=np.sqrt(noise_var)
        im_rows, im_cols=np.shape(self.src_im)
        # get the number of noise which is number of rows multiply the number of cols
        num_noise=im_rows*im_cols
        noise_im=copy.deepcopy(self.src_im)
        for i in range(num_noise):
            random_x=random.randint(0, im_rows-1)
            random_y=random.randint(0, im_cols-1)
            noise_im[random_x, random_y]=noise_im[random_x, random_y]+random.gauss(0, sigma)
            if noise_im[random_x, random_y]<=0:
                noise_im[random_x, random_y]=0
            elif noise_im[random_x, random_y]>=255:
                noise_im[random_x, random_y]=255
        return noise_im
        
    def saltPepperNoise(self, prob):
        cur_im=self.src_im
        im_rows, im_cols=np.shape(self.src_im)
        noise_im=np.zeros((im_rows, im_cols), dtype=float)
        for i in range(im_rows):
            for j in range(im_cols):
                x=random.random()
                if x<prob:
                    noise_im[i,j]=0
                elif x>(1-prob):
                    noise_im[i,j]=255
                else:
                    noise_im[i,j]=cur_im[i,j]
        return noise_im
                    