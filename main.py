import matplotlib.pyplot as plt
import matplotlib.image as mpimage
from filter import Flip, Rotate, showIntensityGraph, toBlue, toGray, toGreen, toNegative, toRed, toSepia
import numpy as np


img = mpimage.imread('SR.jpg')


#print(type(img))
#print(img.shape)
#print(img)
height = img.shape[0]
width = img.shape[1]
#print(height, width)


blue_component = img.copy()
red_component = img.copy()
green_component = img.copy()
flip_component = img.copy()
sepia_component = img.copy()
gray_component = img.copy()
rotated_componenent = img.copy()
negative_component = img.copy()


toBlue(blue_component)
toRed(red_component)
toGreen(green_component)
Flip(flip_component)
gray_component = toGray(img)
#toSepia(sepia_component, height, width)
#Sepia works but takes a lot of time, hence it is commented
rotated_componenent = Rotate(rotated_componenent)
negative_component = toNegative(negative_component)
#showIntensityGraph(img)
#The above function gives the intensity of the picture

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
#change the below argument to any of the components made from line 18 to line 25
plt.imshow(green_component)
plt.title('Processed Image')
plt.axis('off')
plt.tight_layout()
plt.show()
