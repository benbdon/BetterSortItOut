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
from Tkinter import *
from PIL import ImageTk, Image
import os
import subprocess

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

def recyclable(string1):
    
    log_functions.log(string1+' recyclable')

def trash(string1):
    
    log_functions.log(string1+' trash')
    
def callback(panel, newString):
    path2="/home/bendon/Dropbox/Side Project/TrashProject/images"+newString+".jpg"
    img2 = ImageTk.PhotoImage(Image.open(path2))
    panel.configure(image=img2)
    panel.image = img2
    lbl.config(text = "New Image. Classify as 'Recyclable' or 'Trash'. Close window to view next trash item.")
    lbl.pack()
    
def close_window(window): 
    window.destroy()

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
                print "Next image captured"

                #Get user feedback through Tkinter GUI on the image and log
                root = Tk()
                root.title("Better Sort It Out")
                root.geometry("500x500")#Width x Height

                #old trash image 
                img = ImageTk.PhotoImage(Image.open("/home/bendon/Dropbox/Side Project/TrashProject/images"+oldString+".jpg"))
                panel = Label(root, image = img)
                panel.pack(side="top", fill = "both", expand = "yes")

                app = Frame(root)
                app.pack(side='bottom',pady=10)
                lbl = Label(app,text="Previous Image. Hit 'Enter' to view new image",font=("Comic Sans", 16))
                lbl.pack()
                button1 = Button(app, text = "Recyclable",font=("Comic Sans", 16), command= lambda: recyclable(string),bg='#00FA9A')
                button1.pack()
                button2 = Button(app, text = "   Trash    ",font=("Comic Sans", 16),command= lambda: trash(string),bg='#FA8072')
                button2.pack()
                button3 = Button(app, text = "Close and view next image", font=("Comic Sans", 16),command = lambda: close_window(root), bg = '#FFFAF0')
                button3.pack()
                
                root.bind("<Return>", lambda e: callback(panel,string,lbl))
                root.mainloop()
                
    except KeyboardInterrupt:
        print "\n\nTrashcan OUT!"

if __name__ == '__main__':
    main()
