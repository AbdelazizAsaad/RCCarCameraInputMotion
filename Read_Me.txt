Hi everyone if you would like to use our code please follow the following steps.
Our code works with python 2.7/3.7 and open cv ablove 3.4

First of all you need to download some libraries on ur rasberry pi:
use the following commands in the terminal:

You must install OpenCv of ur pi
please follow the steps in this link:
https://www.pyimagesearch.com/2017/09/04/raspbian-stretch-install-opencv-3-python-on-your-raspberry-pi/?fbclid=IwAR21QU3xzXmYJQHwH2aIc_Rx_qidbvn1vdZcE-1ADWBNwJId7Zw7ERPGVJk

To be able to use the gpio pins on the pi you need to use this command in your terminal:

sudo apt-get install python-rpi.gpio

next you will need to download the files available in the github folder

steps:
1)connect wires between pi and motor driver as explained in the documentation pdf
2)connect ur camera to the pi using usb if it's webcam or action camera or using the build in ribbon cable for pi cameras
3)power up your pi using good power source in pur case we used 5v 2.1A PowerBank
4)power up your motor driver with suffient power for ur motors
5)connect ur pi with your laptop using any VNC viewer to get full access to ur pi (you will need that also to download the ablove installations)
6)if u finished all the above then ur ready to go just simple few lines in terminal to run the code
    code in termial:
                      source ~/.profile
                      workon cv
                      cd directory where you downloaded your python file
                      python CarControlPython.py

ENJOY :)

Auther:Abdelaziz Asaad & Shorouq Mohamed
