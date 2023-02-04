# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 18:06:48 2023

@author: Karam Alhanatlh
"""

#import
import cv2

#version cv2
print(cv2.__version__)

"""
0  grayscale
1  color
-1 alpha channel
"""

#read image
img= cv2.imread("data/apple.jpg",0)
print(img)
#show image
cv2.imshow("apple",img)
k=cv2.waitKey(0)
if k ==27:  #Esc
    cv2.destroyAllWindows()
elif k==ord("s"):
    cv2.imwrite("data/sec image.jpg",img)
    cv2.destroyAllWindows()    
    
    
    
    
    
    
    
    