
import sys
import os
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import copy
import cv2
import time 
from datetime import *
from PIL import Image

# time.sleep(5)

cap = cv2.VideoCapture(1)

#setting image size
cap.set(3,1280)
cap.set(4,1024)

ret, img = cap.read()
img = cv2.flip(img, 1)
if ret:
    # x1, y1, x2, y2 = 175, 175, 375, 375
    # img_cropped = img[y1:y2, x1:x2]
    # cv2.imwrite( "/home/ahalyamandana/Desktop/test.jpg", img_cropped);
    filename = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    path = "/home/ahalyamandana/Desktop/" + filename +".jpg"
    cv2.imwrite(path, img);

        
           
# Following line should appear but is not working with opencv-python package
cap.release()
cv2.destroyAllWindows()
