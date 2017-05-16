import numpy as np
import cv2

cap = cv2.VideoCapture('../data/video/The_Good_Dinosaur.mp4')

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
cap2 = cv2.VideoCapture('../data/video/The_Good_Dinosaur.mp4')
length2 = int(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
length1 = int(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
rate = int(cap2.get(cv2.CAP_PROP_FPS))
print length1
print rate
i= 0
cap2.set(2,0)
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:

        ret2, frame2 = cap2.read()
        gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)
        frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)
        i = i+ 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
print "i ",i