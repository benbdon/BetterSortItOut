#!/usr/bin/env python
# this program takes user input from a keyboard (y/n)
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
import log_functions

def webcam():
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
    
        #TODO fix file path, change to relative path
        filename = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        path = "/home/ahalyamandana/Desktop/" + filename +".jpg"
        cv2.imwrite(path, img);

        
           
# Following line should appear but is not working with opencv-python package
    cap.release()
    cv2.destroyAllWindows
    return filename

def main():
    lidCondition = "c"
    string
    while (True):
        #Hold prev condition
        prevLidCondition = lidCondition

        #"Manual" open/close switch
        lidCondition = raw_input("Type o and c\n")

        #Check if the lid went from open to close
        if (prevLidCondition != lidCondition and lidCondition == "c"):

            #Take image
            string = webcam()
            print "Taking image"
            isRecyclable = raw_input("Is this recyclable?\n")
            if (isRecyclable == 'y'):
                print("This is recyclable\n")
                log_functions.log(string+isRecyclable)
            elif (isRecyclable == 'n'):
                print("This is not recyclable\n")
                log_functions.log(string+isRecyclable)
                
            

if __name__ == '__main__':
    main()
