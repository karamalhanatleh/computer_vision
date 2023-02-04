# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 18:15:41 2023

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
img= cv2.imread("data/apple.jpg",1)
print(img)


#show image
cv2.imshow("apple",img)
k=cv2.waitKey(3000) # second * 1000
cv2.destroyAllWindows()  


    