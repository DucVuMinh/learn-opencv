import numpy as np
import cv2
cap = cv2.VideoCapture('../data/video/nhoc_trum.mp4')
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print( length )
for i in range(length):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()