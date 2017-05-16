from  __future__ import  print_function
from  __future__ import  division
import cv2
import numpy as np
from matplotlib import pyplot as plt

cv2.HOGDescriptor()
img = cv2.imread('../data/video/output/The_Good_Dinosaur4/frame3654.jpg')
print (img.shape)
cv2.imshow('image',img)
plt.hist(img.ravel(),256,[0,256]); plt.show()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
var = np.var(gray)
mean = np.mean(gray)
print (gray.shape)
height, width = gray.shape
size = height * width
print ("mean ",mean)
print ("size ", size)
print (gray - mean)
print (1/float(size))
constrast = np.sqrt(1/size * np.sum((gray - mean)*(gray - mean)))
print ("constrast ", constrast)

cv2.waitKey(0)
cv2.destroyAllWindows()