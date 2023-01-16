import cv2
import numpy as np

cam = cv2.VideoCapture(0)
while True:
    myret, CapFrame =cam.read()
    cv2.imshow('CapFrame',CapFrame)
    if cv2.waitKey(10) & 0xFF==ord('c'):
        cv2.imwrite('CapFrame.jpg', CapFrame)
        break
    if cv2.waitKey(10) & 0xFF==27:
        break
cam.release()
cv2.destroyAllWindows()