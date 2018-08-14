# DeepDream
Deep dream implementation with inception model 
-----------------------------------------------------------------------------------
DeepDream is an artistic image-modification technique that uses the representations
learned by convolutional neural networks. It was first released by Google in the summer
of 2015, as an implementation written using the Caffe deep-learning library (this
was several months before the first public release of TensorFlow).4 It quickly became
an internet sensation thanks to the trippy pictures it could generate (see, for example,
figure 8.3), full of algorithmic pareidolia artifacts, bird feathers, and dog eyes—a
byproduct of the fact that the DeepDream convnet was trained on ImageNet, where
dog breeds and bird species are vastly overrepresented.

What is really happening
-----------------------------------------------------------------------------------------
1- With DeepDream, you try to maximize the activation of entire layers rather
than that of a specific filter, thus mixing together visualizations of large numbers
of features at once.

2- You start not from blank, slightly noisy input, but rather from an existing
image—thus the resulting effects latch on to preexisting visual patterns, distorting
elements of the image in a somewhat artistic fashion.

3- The input images are processed at different scales (called octaves), which
improves the quality of the visualizations.

Code describtion
-----------------------------------------------------------------------------------------
After importing the packages we will be using

    import numpy as np
    import PIL.Image
    import cv2
    import os
from deepdreamer import model, load_image, recursive_optimize #import some functions from the other file

next line determine that we are going to use the contribution of only layer 3 loss from the inception model(responsible for detection of edges)
x_size and y_size are just the dimensions of the picture i picked
inside the loop 
load the image and zoom to a certain ratio
        
        x_trim = 2
        y_trim = 1
        
        img_result = img_result[0+x_trim:y_size-y_trim,0+y_trim:x_size-x_trim]
        
then resize it to its original size
tune the colors in the image
        img_result[:,:,0] +=2
        img_result[:,:,1] +=2
        img_result[:,:,2] +=2
you can tune it we any value you like
and then restrict the values of the tensor from 0 to 255, then call the recersive function (described inside the other file)
perfome same steps as before and then save it, the loop will run 50 times generating 50 pictures and then you can easily put them
as frames together resulting in a video and the code for that provided ^


