import numpy as np
import matplotlib.pyplot as plt

def crop (image,x1,y1,x2,y2):
    return image[x1:x2,y1:y2]


def toBlue(image):
    image[::, ::, 0:2]=0

def toRed(image):
    image[::, ::, 1:3]=0

def toGreen(image):
    image[::, ::, 0:1]=0
    image[::, ::, 2:3]=0

def Flip(image):
    image[:, :, :] = image[:, ::-1, :]

def toGray(image):
    return np.dot(image[...,:3], [0.299, 0.587, 0.114])


def toSepia(image, height, width):
    #print(height, width)
    for col in range(height):
        for row in range(width):
            p = image[col, row]
            R = p[0]
            G = p[1]
            B = p[2]
            
            nR = int(0.393 * R + 0.769 * G + 0.189 * B)
            nG = int(0.349 * R + 0.686 * G + 0.168 * B)
            nB = int(0.272 * R + 0.534 * G + 0.131 * B)

            if(nR > 255):
                nR = 255
            if(nG > 255):
                nG = 255
            if(nB > 255):
                nB = 255
            p[0] = nR
            p[1] = nG
            p[2] = nB       
            #print(nR, nG, nB)

def Rotate(image):
    image = np.rot90(image)
    return image

def toNegative(image):
    image = 255 - image
    return image

def showIntensityGraph(image):
    img_flat = image.flatten()
    plt.hist(img_flat, bins=200, range=[0, 256])
    plt.title("Number of pixels in each intensity value")
    plt.xlabel("Intensity")
    plt.ylabel("Number of pixels")
    plt.show()
            


            
            
            

            



    
    
    

