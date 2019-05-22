#importing modules

import cv2   

import numpy as np


#capturing video through webcam
cap=cv2.VideoCapture(0)

while(1):
	_, img = cap.read()

	#converting frame(img i.e BGR) to HSV (hue-saturation-value)

	hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

	#definig the range of red color
	red_lower=np.array([136,87,111],np.uint8)
	red_upper=np.array([180,255,255],np.uint8)