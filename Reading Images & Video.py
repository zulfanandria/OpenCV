import cv2 as cv

# img = cv.imread('OpenCV/Photo/123.jpg')

# cv.imshow('gambar', img)

# cv.waitKey(0)

capture = cv.VideoCapture('OpenCV/Video/HBD.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(5) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
