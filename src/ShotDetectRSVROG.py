"""
Createb by DucVM
"""

from  __future__ import  print_function
from  __future__ import  division
import numpy as np
import cv2
from matplotlib import pyplot as plt

#def function to calculating the constrast of gray image
def calConstrastGray(img_gray):
    var = np.var(img_gray)
    mean = np.mean(img_gray)
    height, width = img_gray.shape
    size = height * width
    constrast = np.sqrt(1 / size * np.sum((img_gray - mean) * (img_gray - mean)))
    #print("constrast ", constrast)
    return  constrast
#def function to calculating the constrast
def calConstrastColor(img):
    var = np.var(img)
    mean = np.mean(img)
    height, width, channels = img.shape
    size = height * width
    constrast = np.sqrt(1 / size * np.sum((img - mean) * (img - mean)))
    #print("constrast ", constrast)
    return  constrast
#def fucntion to read video and then output image that represent for each shot
def dectUsingRSV(inputfile, outputfolder, S):
    pass

#def function to read ouput from first step using RSV,
# then continue filtering using ROG

def dectUsingROG(inputfolder, outputfolder, T):
    pass
cap = cv2.VideoCapture('../data/video/doc_long_bolero.mp4')
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
print (res.shape)

plt.plot(res,color = 'r')
#plt.xlim([0,256])
plt.ylabel('distance')
plt.show()


var = np.var(res)
mean = np.mean(res)
T = mean + 0.5*np.sqrt(var)
print (T)
shotDect = [index for index in range(length) if res[index] >= T]

index = 0
lengthShot = len(shotDect)
selectedFrame = np.array([], dtype = np.int8)
for i in range(lengthShot):
    select = 0
    if i == 0:
        select = shotDect[i]/2
    else:
        select = (shotDect[i-1] + shotDect[i])/2
    selectedFrame = np.append(selectedFrame, select)
lengthSelected = len(selectedFrame)
print (lengthSelected)
cap.set(2,0)
maxConstrast = 0
imgchoice = []
indexChoice = 0
arrChoice = np.array([], dtype= np.int)
for i in range(length):
    # Capture frame-by-frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #calculate the constrast
    if (ret != True):
        break
    #if (index< lengthSelected) & (i == selectedFrame[index]):
    #    print (i)
    #    cv2.imshow('frame', frame)
    #    cv2.imwrite("../data/video/output/The_Good_Dinosaur3/frame%d.jpg" % shotDect[index], frame)
    #    index = index + 1
    print (index, "-------" ,lengthShot)
    if (index< lengthShot) & (i < shotDect[index]):

        constrast = calConstrastGray(gray)
        if (constrast > maxConstrast):
            maxConstrast = constrast
            imgchoice = gray
            indexChoice = i

    else:
        arrChoice = np.append(arrChoice, indexChoice)
        cv2.imshow('frame', imgchoice)
        cv2.imwrite("../data/video/output/doc_long_bolero/frame%d.jpg" % indexChoice, imgchoice)
        maxConstrast = calConstrastGray(gray)
        imgchoice = gray
        indexChoice = i
        index = index +1
        if (index >= lengthShot):
            break
# When everything done, release the capture
np.savetxt("../data/video/output/doc_long_bolero/choice.txt", arrChoice)
np.savetxt("../data/video/output/doc_long_bolero/shotdect.txt", shotDect)
cap.release()
cv2.destroyAllWindows()



