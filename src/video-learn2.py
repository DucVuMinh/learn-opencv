import numpy as np
import cv2

cap = cv2.VideoCapture('../data/video/The_Good_Dinosaur.mp4')

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
cap2 = cv2.VideoCapture('../data/video/The_Good_Dinosaur.mp4')
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        cap2.set(2, 1)
        ret2, frame2 = cap2.read()
        cv2.imshow('frame', frame2)
        frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()