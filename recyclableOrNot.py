#!/usr/bin/env python
# this program captures an image every time the trash can lid opens and closes
import sys
import os
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import copy
import cv2
import time as t
from datetime import *
from PIL import Image
import log_functions
import serial

def webcam():
    cap = cv2.VideoCapture(1)

    #setting image size
    cap.set(3,1280)
    cap.set(4,1024)

    ret, img = cap.read()
    img = cv2.flip(img, 1)
    if ret:

        #TODO fix file path, change to relative path
        filename = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        path = "/home/bendon/Dropbox/Side Project/TrashProject/images" + filename +".jpg"
        cv2.imwrite(path, img);

    cap.release()
    cv2.destroyAllWindows
    return filename



def main():

    #establish serial connection to Arduino
    ser = serial.Serial('/dev/ttyACM1', 9600, timeout = 1.0)

    #necessary evil to let the Arduino reboot after establishing a connection
    ser.setDTR(0)
    ser.flush()
    ser.flushInput()
    ser.flushOutput()
    t.sleep(1.0)

    #initialize the lid to closed
    lidCondition = "c\n"

    #Capture a baseline photo
    string = webcam()
    print "Image captured"

    #Get user feedback on the image and log
    isRecyclable = raw_input("Is this recyclable? Type y or n.\n")
    if (isRecyclable == 'y'):
        log_functions.log(string + " " + isRecyclable)
    elif (isRecyclable == 'n'):
        log_functions.log(string + " " + isRecyclable)

    #MAIN LOOP
    try:
        while (True):

            prevLidCondition = lidCondition #Hold prev condition
            lidCondition = ser.readline() #Get new lid condition

            #Check if the lid went from open to close
            if (prevLidCondition != lidCondition and lidCondition == "c\n"):
                oldString = string
                #Take image
                string = webcam()
                print "Image captured"

                #Get user feedback on the image and log
                isRecyclable = raw_input("Is this recyclable? Type y or n.\n")
                if (isRecyclable == 'y'):
                    log_functions.log(string + " " + isRecyclable)
                elif (isRecyclable == 'n'):
                    log_functions.log(string + " " + isRecyclable)
    except KeyboardInterrupt:
        print "\n\nTrashcan OUT!"

if __name__ == '__main__':
    main()
