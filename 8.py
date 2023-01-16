import cv2
import numpy as np

cam = cv2.VideoCapture(0)

#video writer
vid = cv2.VideoWriter("MyVideo.avi",cv2.VideoWriter_fourcc(*'XVID'),10,(640,480))

while True:
    myret, CapFrame =cam.read()
    cv2.imshow('CapFrame',CapFrame)

    #gray image
    grayImg= cv2.cvtColor(CapFrame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray Image', grayImg)

    #write video frame
    vid.write(CapFrame)

    if cv2.waitKey(10) & 0xFF==ord('c'):
        cv2.imwrite('CapFrame.jpg', CapFrame)
        break
    if cv2.waitKey(10) & 0xFF==27:
        break

cam.release()
vid.release()
cv2.destroyAllWindows()
