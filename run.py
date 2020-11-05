# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 21:26:24 2020

@author: aadit
"""


import cv2
from matplotlib import pyplot as plt
import easyocr
reader = easyocr.Reader(['en'])

car_cascade = cv2.CascadeClassifier('cars.xml')


vid = cv2.VideoCapture(0) 
  
while(True): 
      
    # Capture the video frame 
    # by frame 
    ret, frame = vid.read() 
    # Display the resulting frame 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 2)
        print(reader.readtext(frame, detail = 0));
        cars = cars + 1

    plt.figure(figsize=(10,20))
    plt.imshow(frame)
    cv2.imshow('frame', frame) 
    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 