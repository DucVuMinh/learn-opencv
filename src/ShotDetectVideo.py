import numpy as np
import cv2
from matplotlib import pyplot as plt

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
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hist_new = cv2.calcHist([gray], [0], None, [64], [0, 256])

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if i ==0:
        old_frame = hist_new
        new_frame = hist_new
    else:
        old_frame = new_frame
        new_frame = hist_new

    diff = [np.sum( np.absolute(old_frame - new_frame) ) ]
    res = np.append(res, diff, axis = 0)
print res.shape

plt.plot(res,color = 'r')
#plt.xlim([0,256])
plt.ylabel('distance')
plt.show()
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()