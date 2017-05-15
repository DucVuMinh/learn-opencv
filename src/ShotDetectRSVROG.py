"""
Createb by DucVM
"""


import numpy as np
import cv2
from matplotlib import pyplot as plt


#def fucntion to read video and then output image that represent for each shot
def dectUsingRSV(inputfile, outputfolder, S):
    pass

#def function to read ouput from first step using RSV,
# then continue filtering using ROG

def dectUsingROG(inputfolder, outputfolder, T):
    pass
cap = cv2.VideoCapture('../data/video/The_Good_Dinosaur.mp4')
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print( length )
old_frame = []
new_frame = []
res = np.array([], dtype= np.float)

for i in range(length):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if (ret != True):
        break
    # Our operations on the frame come here
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    hist_new = cv2.calcHist([hsv], [0,1,2], None, [16, 8, 8], [0, 180, 0, 1, 0, 256])
    #print hist_new.shape
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if i ==0:
        #print hist_new[0,0,:]
        old_frame = hist_new
        new_frame = hist_new
    else:
        old_frame = new_frame
        new_frame = hist_new
    #diffrent between two frame using chi-square formular
    diffChiSquare = cv2.compareHist(new_frame, old_frame, 1)

    #different between two frame using norm1 formular
    diff = [np.sum( np.absolute(old_frame - new_frame) ) ]

    res = np.append(res, [diffChiSquare], axis = 0)
print res.shape

plt.plot(res,color = 'r')
#plt.xlim([0,256])
plt.ylabel('distance')
plt.show()


var = np.var(res)
mean = np.mean(res)
T = mean + np.sqrt(var)
print T
shotDect = [index for index in range(length) if res[index] >= T]
for frame in shotDect:
    cap.set(2, frame)
    f = cap.get(int(frame))
    print frame
    cv2.imshow('frame', f)
    print f.shape
    cv2.imwrite("../data/video/output/The_Good_Dinosaur/frame%d.jpg" % frame, f)
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
