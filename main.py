

#Read an image, then show the image in a window and destroy on amy key stroke

import cv2
from matplotlib import pyplot as pyplt

# Load an color image in grayscale
img = cv2.imread('C:/Users/Saumya Dabas/cat2.jpg',1)

#cv2.IMREAD_COLOR : Loads a color image; use 1
#cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode ; use 0

#cv2.imshow('my image',img)
pyplt.imshow(img,cmap='gray',interpolation='bicubic')
pyplt.show()

wk = cv2.waitKey(0)
if wk == 27: # wait for ESC key to exit
    print("quit without saving")
    cv2.destroyAllWindows()
elif wk == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('mypythonsave.png',img)
    print("image saved to disk")
    cv2.destroyAllWindows()
else:
     print("unknown key command ")


cv2.destroyAllWindows()