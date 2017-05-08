
# coding: utf-8

# In[1]:

import cv2
import numpy as np
cap = cv2.VideoCapture('../data/video/nhoc_trum.mp4') # Nho doi theo dung duong dan Video trong may local
i = 0
hist_new = np.array([]) 
hist_old = np.array([])
results = {}

# Doan code duoi day doc cac frame tu video, chuyen no ve dang anh gray, 
# tinh histogram cho frame do va tinh khoang cach voi frame phia truoc
# Luu y: co the khong can chuyen ve dang anh gray ma co the tinh histogram cho ca anh mau
# Truong hop SIFT, SUFT, can goi ham tinh va so sanh tuong ung voi cac dac trung nay
while(cap.isOpened()):
    # Doc cac frame trong video
    ret, frame = cap.read()
    
    # Neu khong con frame nao thi ket thuc
    if(ret != True):
        break
    # Chuyen anh ve dang gray scale
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Tinh histogram
    hist_new = cv2.calcHist([gray_image], [0], None, [256], [0,256])
    
    # Neu la frame dau tien thi chua can so sanh
    if (i == 0):
        i = i+1
        hist_old = hist_new
        continue
        
    # Neu khong phai la frame dau tien, so sanh histogram
    # Luu y: tham so thu 3 cua ham compareHist nhan 4 gia tri 0,1,2,3 tuong ung voi cac cach tinh khoang cach
    # O day dung 0, tuong ung voi cach tinh do tuong dong correlation, lay 1 - do tuong dong => khoang cach
    d = 1 - cv2.compareHist(hist_new, hist_old, 0)
    
    
    # Them vao ket qua so sanh histogram
    results[i-1] = d
    
    # Tang i, cho hist_new thanh hist_old de tinh tiep
    i = i+1
    hist_old = hist_new

print i
cap.release()

# Sau doan code nay,da lay duoc tap khoang cach cac frame ke tiep nhau 


# In[2]:

# Chuyen ve dang numpy.array de ve do thi tren matplotlib 
dist_hist = np.array(results.items(), dtype='float')
dist_hist


# In[5]:

# Ve do thi the hien su chenh lech histogram theo thu tu cac frame, o day chi lay 200 frame tu 100 den 300
import matplotlib.pyplot as plt
plt.plot(dist_hist[0:200, 0], dist_hist[0:200, 1])
plt.ylabel('distance')
plt.show()

# Tu do thi duoc ve ra, co the thay nhung diem cao dot ngot nen de dang nhan ra do la bien cua cac shot
# Tuy nhien, co nhung diem ma do cao khong qua lon, va nhieu diem ben canh co do cao tuong tu no,
# Day la truong hop can thao luan de dua ra phuong an xac dinh bien o dau

