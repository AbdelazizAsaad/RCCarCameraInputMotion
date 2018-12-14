#!/usr/bin/python
# coding: utf-8

#---------------------------------------------------------------
# Autor: Saymon C. A. Oliveira and Modifed by Abdelaziz Asaad and Shourouq Mohamed
# Description: This algorithm describes the sim- ple implementation of OpenCV
# Functions: Digital Image -> HSV Transformation -> Binary Image -> Binary Erosion -> Find Area -> Find Coordinates
# Functions 2: draw circle in the centroid (x, y) -> pin declaration -> declaration of motor movement functions
# Functions 3: perform depth movement robot (area)
# Tecnologias: OpenCV, Python, GPIO e NumPy
#---------------------------------------------------------------

import cv2 as cv
import cv2 as cv2
import time
import numpy as np
import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)
# Turn off alerts
gpio.setwarnings(False)
#---------------------------------------
#Declares pins as output GPIO - Motor A
 
#motor A activation pin on the RPi
gpio.setup(7, gpio.OUT)
 
#motor A activation pin on the RPi
gpio.setup(11, gpio.OUT)
 
#Start Pin 13 as output - Motor A
gpio.setup(13, gpio.OUT)
 
#Start Pin 15 as output - Motor A
gpio.setup(15, gpio.OUT)
 
#---------------------------------------
#Declares pins as output GPIO - Motor B
 
#motor B activation pin on the RPi
gpio.setup(26, gpio.OUT)
 
#motor B activation pin on the RPi 
gpio.setup(16, gpio.OUT)
 
# Start Pin 18 as output - Motor B
gpio.setup(18, gpio.OUT)
 
#Start Pin 22 as output - Motor B
gpio.setup(22, gpio.OUT)

#-----------------------------------------
# Allow the L298N to be controlled by the GPIO
#---------------------------------------
#Initial Values ??- True - Motor A Enabled
gpio.output(7, True) #Motor A - RPi 1
gpio.output(11, True) #Motor A - RPi 2
#---------------------------------------
#Initial Values ??- True - Motor B Enabled
gpio.output(26, True) #Motor B - RPi 1
gpio.output(16, True) #Motor B - RPi 2
#---------------------------------------

def Front():
# Motor 1
 gpio.output(13, True)
 gpio.output(15, False)
# Motor 2
 gpio.output(18, False)
 gpio.output(22, True)
	
def Back():
# Motor 1
 gpio.output(13, False)
 gpio.output(15, True)
# Motor 2
 gpio.output(18, True)
 gpio.output(22, False)
 
 
def Stop():
# Motor 1
 gpio.output(18, False)
 gpio.output(22, False)
# Motor 2
 gpio.output(13, False)
 gpio.output(15, False)

def Right():
# Motor 1
 gpio.output(13, True)
 gpio.output(15, False)
# Motor 2
 gpio.output(18, True)
 gpio.output(22, False)


def Left(): 
# Motor 1
 gpio.output(13, False)
 gpio.output(15, True)
# Motor 2
 gpio.output(18, False)
 gpio.output(22, True)

#def Adjust(area):
 # if(area<=120):
  #    Right()
  #elif(area>=600):
   #   Left()
  #else:
   #   Stop()
	  
#---------------------------------------------------------------
#                        IMAGE PROCESSING
#------------------------------------------------------------------
# STEP1:OK
# USING FUNCTION INRANGE TO CHANGE RGB-HSV
# FOR THAT WE HAVE TO DEFINE THE LIMITS OF H, S AND VALUES

# HSV range we used to detect the colored object
# In this example, set to a green ball(green color in general)
Hmin = 42
Hmax = 92
Smin = 62
Smax = 255
Vmin = 63
Vmax = 235


#Default RED
#Hmin = 0
#Hmax = 179 
#Smin = 131
#Smax = 255
#Vmin = 126
#Vmax = 255


# An array of HSV values ??is created (minimum and maximum)
rangeMin = np.array([Hmin, Smin, Vmin], np.uint8)
rangeMax = np.array([Hmax, Smax, Vmax], np.uint8)

# Image processing function
def processing (Input):
     imgMedian = cv2.medianBlur(Input,1)
     imgHSV = cv2.cvtColor(imgMedian,cv2.COLOR_BGR2HSV)	
     imgThresh = cv2.inRange(imgHSV, rangeMin, rangeMax)
     imgErode = cv2.erode(imgThresh, None, iterations = 3)
     return imgErode
#---------------------------------------------------------------

cv.namedWindow("Input")
#cv.namedWindow("HSV")
#cv.namedWindow("Thre")
cv.namedWindow("Negactive")

capture = cv2.VideoCapture(0)

# Parametros do tamannho da imagem de captura
width = 160
height = 120

# Minimum area to be detected
minArea = 50 #close to 80 cm

#Center of axes
center = width/2


# Center Limit
may = width/3

# Define a size for the frames (discarding PyramidDown)
if capture.isOpened():
  capture.set(3, width)
  capture.set(4, height)

  
while True:
    ret, Input = capture.read()
    image_processed = processing (Input)
    moments = cv2.moments(image_processed, True)
    imgHSV = cv2.cvtColor(Input,cv2.COLOR_BGR2HSV)	
    imgThresh = cv2.inRange(imgHSV, rangeMin, rangeMax)
    imgErode = cv2.erode(imgThresh, None, iterations = 3)
    #moments = cv2.moments(imgErode, True)
    area = moments['m00']
    if moments['m00'] >= minArea:
     x = moments['m10'] / moments['m00']
     y = moments['m01'] / moments['m00']
     cv2.circle(Input, (int(x), int(y)), 5, (0, 255, 0), -1)
     if(area<=120):
      Front()
     elif(area>=600):
      Back()
     else:
      Stop()

# If the limit is greater than the distance from the center that is considered centered
      if (x - center) >= may:
         Left()
		
	   # If the limit is lower
      elif (center - x) >= may:
	 Right()

     print(area)
     #Adjust(area)    
    else:
     Stop()

    
    cv2.imshow("Input",Input)
    #cv2.imshow("HSV", imgHSV)
    #cv2.imshow("Thre", imgThresh)
    cv2.imshow("Negative", imgErode)
  
    if cv2.waitKey(10) == 27:
        break
	cv2.DestroyAllWindows()	
	gpio.cleanup()	