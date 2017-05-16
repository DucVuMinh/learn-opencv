import cv2
import numpy as np
from matplotlib import pyplot as plt
def calConstrastGray(img_gray):
    var = np.var(img_gray)
    mean = np.mean(img_gray)
    height, width, chanels = img_gray.shape
    size = height * width
    constrast = np.sqrt(1 / size * np.sum((img_gray - mean) * (img_gray - mean)))
    #print("constrast ", constrast)
    return  constrast
#read array shot in numpy array
arrShot = np.loadtxt("../data/video/output/daddy_and_baby/choice.txt",
                     dtype= np.float, delimiter = "\n")

lengthShot = arrShot.shape[0]
img_before = []
hist_before = []
index_before = 0
winSize = (64,64)
blockSize = (16,16)
blockStride = (8,8)
cellSize = (8,8)
nbins = 9
derivAperture = 1
winSigma = 4.
histogramNormType = 0
L2HysThreshold = 2.0000000000000001e-01
gammaCorrection = 0
nlevels = 64
hog = cv2.HOGDescriptor()

for i in range(lengthShot):
    if(i==0):
        filename1 = "../data/video/output/daddy_and_baby/frame" + str(int(arrShot[0])) + ".jpg"
        print filename1
        img_before = cv2.imread(filename1)
        hist_before = hog.compute(img_before)
        index_before = arrShot[0]
    else:
        filename2 = "../data/video/output/daddy_and_baby/frame" + str(int(arrShot[i])) + ".jpg"
        img_current = cv2.imread(filename2)
        hist_current = hog.compute(img_current)
        index_current = arrShot[i]
        diff = hist_current - hist_before
        diff = np.sum(np.abs(diff))
        diff = diff/(10**6)
        print  diff
        #if the diffirent is smaller than 5, remove this current image, and continue
        if diff < 3:
            print img_before.shape
            constrast_before = calConstrastGray(img_before)
            constrast_current = calConstrastGray(img_current)

            if (constrast_before < constrast_current):
                img_before = img_current
                hist_before = hist_current
                index_before = index_current

        #else if diff >=5, store both image, then continue
        else:
            #save both image
            cv2.imwrite\
                ("../data/video/output/daddy_and_baby/rog/frame%d.jpg" % index_before, img_before)
            cv2.imwrite \
                ("../data/video/output/daddy_and_baby/rog/frame%d.jpg" % index_current, img_current)
            img_before = img_current
            hist_before = hist_current
            index_before = index_current
            diff = 0

image = cv2.imread('../data/video/output/The_Good_Dinosaur6/frame1634.jpg')
image2 = cv2.imread('../data/video/output/The_Good_Dinosaur6/frame1670.jpg')

hist1 = hog.compute(image)
hist2 = hog.compute(image2)
diff = hist1 - hist2
#print diff
#print np.sum(diff)
diff = np.sum(np.abs(diff))
print diff