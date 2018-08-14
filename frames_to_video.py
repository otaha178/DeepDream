# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 05:36:11 2018

@author: Ziggby
"""

import cv2
import os
path = "images"
fourcc = cv2.VideoWriter_fourcc(*'XVID')

out = cv2.VideoWriter('video.avi',fourcc,5,(1024,819))

for i in range(0,41):
    img_path = os.path.join(path,"img{}.jpg".format(i))
    print(img_path)
    frame = cv2.imread(img_path)
    out.write(frame)
out.release()