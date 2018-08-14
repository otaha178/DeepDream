# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 03:48:45 2018

@author: Ziggby
"""

import numpy as np
import PIL.Image
import cv2
import os
from deepdreamer import model, load_image, recursive_optimize
layer_tensor = model.layer_tensors[3]

image_name = 'img0.jpg'

x_size = 1024
y_size = 819

counts = 0
max_count=50

for i in range(0,999):
    if os.path.isfile('images/img{}.jpg'.format(i+1)):
        print('file exists')
    else:
        img_result = load_image(filename='images/img{}.jpg'.format(i))
        
        x_trim = 2
        y_trim = 1
        
        img_result = img_result[0+x_trim:y_size-y_trim,0+y_trim:x_size-x_trim]
        img_result = cv2.resize(img_result,(x_size,y_size))
        
        img_result[:,:,0] +=2
        img_result[:,:,1] +=2
        img_result[:,:,2] +=2
        
        img_result = np.clip(img_result,0.0,255.0)
        img_result = img_result.astype(np.uint8)
        
        img_result= recursive_optimize(layer_tensor=layer_tensor,
                                       image=img_result,
                 # how clear is the dream vs original image        
                 num_iterations=15, step_size=1.0, rescale_factor=0.7,
                 # How many "passes" over the data. More passes, the more granular the gradients will be.
                 num_repeats=1, blend=0.2)
        
        img_result = np.clip(img_result,0.0,255.0)
        img_result = img_result.astype(np.uint8)
        result = PIL.Image.fromarray(img_result, mode='RGB')
        result.save('images/img{}.jpg'.format(i+1))
        
        counts +=1
        if counts>max_count:
            break



        