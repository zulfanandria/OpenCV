import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('blank', blank)

# Gambar
# img = imread('OpenCV/Photo/123.jpg')
# cv.imshow('gambar', img)

# Warna
# blank[200:300, 300:400] = 0,255,0
# cv.imshow('green', blank)

# blank[:] = 0,0,255
# cv.imshow('red', blank)

# Segi-4
# cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)
# cv.imshow('Rectangle', blank)

# Lingkaran
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
# cv.imshow('Circle', blank)

# Garis
# cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)
# cv.imshow('Garis', blank)

# cv.line(blank, (100, 100), (300, 400), (255,255,255), thickness=3)
# cv.imshow('Garis', blank)

# Text
cv.putText(blank, 'Hello, my name is Zulfan', (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank) 

cv.waitKey(0)
