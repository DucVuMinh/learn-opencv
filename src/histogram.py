import cv2
import numpy as np
from matplotlib import pyplot as plt
cv2.HOGDescriptor()
img = cv2.imread('../data/image/home.jpg',0)
print img.shape
cv2.imshow('image',img)
plt.hist(img.ravel(),256,[0,256]); plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
res = np.array([], dtype= np.float)
img = cv2.imread('home.jpg')
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    diffChiSquare = cv2.compareHist(histr, histr, 1)
    res = np.append(res, [5 - diffChiSquare], axis=0)
    print diffChiSquare
    if i==0:
        print type(histr)
        print histr
        print np.sum(histr)
    #plt.plot(diffChiSquare,color = col)
    #plt.xlim([0,256])
plt.plot(res,color = col)
plt.show()